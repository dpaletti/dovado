from functools import lru_cache
from typing import Tuple, Dict, List
import dovado_rtl.vivado_interaction as vivado
import dovado_rtl.report_parsing as report
import numpy as np
from dovado_rtl.frame_handling import HdlBoxFrameHandler, TclFrameHandler
from dovado_rtl.src_parsing import SourceFile
from dovado_rtl.config import Configuration
from dovado_rtl.utility_classes import IsIncremental, StopStep


class DesignValue:
    def __init__(
        self,
        utilisation: Dict[Tuple[str, str], float],
        negative_max_frequency: float,
    ):
        self.utilisation: Dict[Tuple[str, str], float] = utilisation
        self.negative_max_frequency: float = negative_max_frequency


class DesignPointEvaluator:
    def __init__(
        self,
        config: Configuration,
        parsed_source: SourceFile,
        hdl_handler: HdlBoxFrameHandler,
        tcl_handler: TclFrameHandler,
        to_box: bool,
        target_clock: float,
        is_incremental: IsIncremental,
        stop_step: StopStep,
        free_parameters: List[str],
        metrics: List[Tuple[str, str]],
    ):
        self.hdl_handler: HdlBoxFrameHandler = hdl_handler
        self.stop_step: StopStep = stop_step
        self.parsed_file = parsed_source
        self.is_boxed: bool = to_box
        self.target_clock: float = target_clock
        self.is_incremental: IsIncremental = is_incremental
        self.is_first_evaluation: bool = True
        self.free_parameters: List[str] = free_parameters
        self.metrics: List[Tuple[str, str]] = metrics
        self.config: Configuration = config
        self.tcl_handler: TclFrameHandler = tcl_handler

    @lru_cache()
    def evaluate(self, design_point: Tuple[int]) -> DesignValue:
        if not self.is_boxed:
            self.parsed_file.write_parameter_values(
                self.hdl_handler,
                dict(zip(self.free_parameters, design_point)),
            )
        else:
            # TODO revise or delete unboxed evaluation
            # for parameter, value in zip(gus.FREE_PARAMETERS, design_point):
            #     src.map_parameter(
            #         Path(get_config("VHDL_DIR") + get_config("VHDL_BOX"))
            #         if evaluation_setup.top_lang is src.RTL.VHDL
            #         else Path(
            #             get_config("VERILOG_DIR") + get_config("VERILOG_BOX")
            #         ),
            #         "box",
            #         parameter,
            #         value,
            #     )
            raise Exception("Unboxed evaluation not implemented")

        vivado_out, success = vivado.source(
            self.config.get_config("TCL_DIR")
            + self.config.get_config(self.stop_step.name)
        )

        print(vivado_out)
        if self.is_first_evaluation:
            self.is_first_evaluation = False
            self.tcl_handler.setup_incremental(self.is_incremental)

        return (
            DesignValue(
                utilisation={i: np.inf for i in self.metrics},
                negative_max_frequency=np.inf,
            )
            if not success
            else DesignValue(
                utilisation={
                    i: report.get_utilisation(
                        self.config.get_config("VIVADO_OUTPUT_DIR")
                        + self.config.get_config(
                            self.stop_step.name + "_UTILISATION"
                        ),
                        i[0],
                        i[1],
                    )
                    for i in self.metrics
                },
                negative_max_frequency=-float(
                    self.get_max_frequency(
                        report.get_wns(
                            self.config.get_config("VIVADO_OUTPUT_DIR")
                            + self.config.get_config(
                                self.stop_step.name + "_TIMING"
                            )
                        )
                    )
                ),
            )
        )

    def get_max_frequency(self, wns):

        return 1000 / ((1 / 1000 * self.target_clock) - wns)

    @staticmethod
    def get_metric(design_value, metric):
        if metric == "max_frequency":
            return design_value.negative_max_frequency
        else:
            try:
                return design_value.utilisation[metric]
            except Exception as e:
                raise Exception(
                    "Invalid metric passed to the fitness function: "
                    + str(metric)
                    + "\n"
                    + str(e)
                )
