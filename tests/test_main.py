from unittest.mock import patch
import dovado.main as test
from dovado.src_parsing import IsIncremental
import pytest


@pytest.skip
def test_arm4u():
    with patch(
        "dovado.user_input.ask_code_dir", result_value="examples/arm4u/hdl/"
    ):
        with patch(
            "dovado.user_input.ask_top_module",
            result_value=["cpu", "examples/arm4u/hdl/cpu.vhd"],
        ):
            with patch(
                "dovado.user_input.ask_part", result_value="xc7k70tfbv676-1"
            ):
                with patch(
                    "dovado.user_input.ask_stop_step", result_value="synthesis"
                ):
                    with patch(
                        "dovado.user_input.ask_identifiers", result_value="clk"
                    ):
                        with patch(
                            "dovado.user_input.ask_incremental_mode",
                            result_value=IsIncremental(True, True),
                        ):
                            with patch(
                                "dovado.user_input.ask_directives",
                                result_value=("runtimeoptimized", None, None),
                            ):
                                with patch(
                                    "dovado.user_input.ask_clock",
                                    result_value=1000,
                                ):
                                    with patch(
                                        "dovado.user_input.ask_parameters",
                                        result_value="CACHE_BLOCK_BITWIDTH",
                                    ):
                                        with patch(
                                            "dovado.user_input.ask_utilization_metrics",
                                            result_value=[
                                                ("Slice Logic", "LUT as Logic")
                                            ],
                                        ):
                                            with patch(
                                                "dovado.estimation.generate_dataset",
                                                result_value="any",
                                            ):
                                                with patch(
                                                    "dovado.genetic_algorithm.optimize",
                                                    result_value="optimization_result",
                                                ):
                                                    test.main()
