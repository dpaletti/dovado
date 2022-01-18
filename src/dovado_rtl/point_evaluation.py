from functools import lru_cache
from typing import Tuple, Dict, List, Optional
from pathlib import Path

import dovado_rtl.vivado_interaction as vivado
import dovado_rtl.report_parsing as report
from dovado_rtl.frame_handling import (
    HdlBoxFrameHandler,
    TclFrameHandler,
)
from dovado_rtl.config import Configuration
from dovado_rtl.simple_types import IsIncremental, DesignValue, Metric
from dovado_rtl.enums import StopStep
from dovado_rtl.cli_utility import ask_utilization_metrics
from dovado_rtl.report_parsing import get_available_indices
from dovado_rtl.abstract_classes import (
    AbstractDesignPointEvaluator,
    AbstractEstimator,
    AbstractSourceParser,
)


class DesignPointEvaluator(AbstractDesignPointEvaluator):
    def __init__(
        self,
        config: Configuration,
        parsed_source: AbstractSourceParser,
        hdl_handler: HdlBoxFrameHandler,
        tcl_handler: TclFrameHandler,
        target_clock: float,
        is_incremental: IsIncremental,
        stop_step: StopStep,
        free_parameters: List[str],
        int_metrics: Optional[List[int]],
    ):
        self.__hdl_handler: HdlBoxFrameHandler = hdl_handler
        self.__stop_step: StopStep = stop_step
        self.__parsed_file = parsed_source
        self.__target_clock: float = target_clock
        self.__is_incremental: IsIncremental = is_incremental
        self.__is_first_evaluation: bool = True
        self.__free_parameters: List[str] = free_parameters
        self.__config: Configuration = config
        self.__tcl_handler: TclFrameHandler = tcl_handler
        self.__metrics: Optional[List[Metric]] = None
        self.__int_metrics: Optional[List[int]] = int_metrics
        self.__estimator: Optional[AbstractEstimator] = None

        self.__out_file = Path(config.get_config("WORK_DIR")).joinpath(
            "space_exploration.csv"
        )
        self.__out_file_mapping: Dict[str, Metric] = {}
        self.__out_file.open("w").close()
        self.__is_file_header_to_write = True

    @lru_cache()
    def evaluate(self, design_point: Tuple[int, ...]) -> Optional[DesignValue]:
        self.__parsed_file.write_parameter_values(
            self.__hdl_handler,
            dict(zip(self.__free_parameters, design_point)),
        )

        vivado_out, success = vivado.source(
            str(self.__config.get_config("WORK_DIR"))
            + str(self.__config.get_config(self.__stop_step.name))
        )

        print(vivado_out)
        if self.__is_first_evaluation:
            if not success:
                return None
            if not self.__metrics:
                self.__metrics = ask_utilization_metrics(
                    get_available_indices(
                        str(self.__config.get_config("WORK_DIR"))
                        + str(
                            self.__config.get_config(
                                self.__stop_step.name + "_UTILISATION"
                            )
                        )
                    ),
                    Path(str(self.__config.get_config("CUSTOM_METRICS_DIR"))),
                    self.__int_metrics,
                )
            self.__is_first_evaluation = False
        if not success:
            met: Dict[Metric, float] = {}
            for i in self.__metrics:
                if i.is_frequency or i.custom_metric:
                    met[i] = float(0)
                else:
                    met[i] = float(100)
            design_value = DesignValue(met)
        else:
            design_value = DesignValue(
                value={
                    i: report.get_utilisation(
                        str(self.__config.get_config("WORK_DIR"))
                        + (
                            str(
                                self.__config.get_config(
                                    self.__stop_step.name + "_UTILISATION"
                                )
                            )
                        ),
                        i.utilisation[0],
                        i.utilisation[1],
                    )
                    if i.utilisation
                    else -self.get_max_frequency(
                        report.get_wns(
                            str(self.__config.get_config("WORK_DIR"))
                            + (
                                str(
                                    self.__config.get_config(
                                        self.__stop_step.name + "_TIMING"
                                    )
                                )
                            )
                        )
                    )
                    if not i.custom_metric
                    else self.compute_custom_metric(i, design_point)
                    for i in self.__metrics
                },
            )
        self.__write_csv(design_point, design_value)
        return design_value

    def get_max_frequency(self, wns: float) -> float:

        return 1000 / (1 / (1 / 1000 * self.__target_clock) - wns)

    def compute_custom_metric(
        self, metric: Metric, design_point: Tuple[int, ...]
    ):
        if not metric.custom_metric:
            raise Exception(
                "Trying to execute metric '" + str(metric) + "' as custom"
            )

        all_metrics = get_available_indices(
            str(self.__config.get_config("WORK_DIR"))
            + str(
                self.__config.get_config(
                    self.__stop_step.name + "_UTILISATION"
                )
            )
        )

        metrics_value = {}
        for section in all_metrics.keys():
            for m in all_metrics[section]:
                metrics_value[m] = report.get_utilisation(
                    str(self.__config.get_config("WORK_DIR"))
                    + (
                        str(
                            self.__config.get_config(
                                self.__stop_step.name + "_UTILISATION"
                            )
                        )
                    ),
                    section,
                    m,
                )
        metrics_value["frequency"] = self.get_max_frequency(
            report.get_wns(
                str(self.__config.get_config("WORK_DIR"))
                + (
                    str(
                        self.__config.get_config(
                            self.__stop_step.name + "_TIMING"
                        )
                    )
                )
            )
        )

        params_value = {
            fp: dp for fp, dp in zip(self.__free_parameters, design_point)
        }

        return metric.custom_metric[1](**{**metrics_value, **params_value})

    def set_metrics(self, metrics: List[Metric]):
        if self.__metrics:
            raise Exception(
                "Metrics already set with value: "
                + str(self.__metrics)
                + " resetting forbidden. Trying to reset with value "
                + str(metrics)
            )
        self.__metrics = metrics

    def __write_csv(
        self, design_point: Tuple[int, ...], design_value: DesignValue
    ):
        if self.__is_file_header_to_write and self.__metrics:
            header = ",".join(self.__free_parameters)
            for m in self.__metrics:
                header += ","
                if m.utilisation:
                    header += m.utilisation[1]
                    self.__out_file_mapping[m.utilisation[1]] = m
                elif m.is_frequency:
                    header += "Frequency"
                    self.__out_file_mapping["Frequency"] = m
                elif m.custom_metric:
                    header += m.custom_metric[0]
                    self.__out_file_mapping[m.custom_metric[0]] = m

            header += "\n"
            self.__is_file_header_to_write = False
            self.__out_file.open(mode="a+").writelines(header)
        with open(self.__out_file) as file:
            header = file.readline()
        line = ",".join([str(d) for d in design_point])
        header = header[:-1].split(",")[len(design_point) :]
        for metric in header:
            line += ","
            line += str(design_value.value[self.__out_file_mapping[metric]])
        line += "\n"
        self.__out_file.open(mode="a+").writelines(line)

    def set_estimator(self, estimator: AbstractEstimator) -> None:
        self.__estimator = estimator

    def get_metrics(self):
        return self.__metrics

    def get_parsed_src(self):
        return self.__parsed_file
