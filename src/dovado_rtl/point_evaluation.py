from functools import lru_cache
from genericpath import exists
from typing import Tuple, Dict, List, Optional
from pathlib import Path

from numpy.lib.function_base import append

import dovado_rtl.vivado_interaction as vivado
import dovado_rtl.report_parsing as report
import numpy as np
from dovado_rtl.frame_handling import (
    HdlBoxFrameHandler,
    TclFrameHandler,
)
from dovado_rtl.config import Configuration
from dovado_rtl.simple_types import IsIncremental, DesignValue, Metric
from dovado_rtl.enums import StopStep
from dovado_rtl.user_input import ask_utilization_metrics
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
        self.__estimator: Optional[AbstractEstimator] = None

    @lru_cache()
    def evaluate(self, design_point: Tuple[int, ...]) -> DesignValue:

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
            self.__metrics = ask_utilization_metrics(
                get_available_indices(
                    str(self.__config.get_config("WORK_DIR"))
                    + str(
                        self.__config.get_config(
                            self.__stop_step.name + "_UTILISATION"
                        )
                    )
                )
            )
            self.__is_first_evaluation = False

        if not success:
            met: Dict[Metric, float] = {}
            for i in self.__metrics:
                if i.is_frequency:
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
                    for i in self.__metrics
                    if not i.is_frequency and i.utilisation
                },
            )
            for i in self.__metrics:
                if i.is_frequency:
                    design_value.value[i] = -report.get_wns(
                        str(self.__config.get_config("WORK_DIR"))
                        + (
                            str(
                                self.__config.get_config(
                                    self.__stop_step.name + "_TIMING"
                                )
                            )
                        )
                    )
                    break

        return design_value

    def get_max_frequency(self, wns: float) -> float:

        return 1000 / ((1 / 1000 * self.__target_clock) - wns)

    def __write_csv(
        self, estimated_value: float, real_value: float, metric: str
    ):
        Path(
            str(self.__config.get_config("WORK_DIRECTORY"))
            + str(self.__config.get_config("EST_TEST_CSV"))
        ).open(mode="a+").writelines(
            [str(estimated_value) + "," + str(real_value) + "," + metric]
        )

    def set_estimator(self, estimator: AbstractEstimator) -> None:
        self.__estimator = estimator

    def get_metrics(self):
        return self.__metrics
