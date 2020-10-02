from unittest.mock import patch
import dovado.point_evaluation as test
from dovado.src_parsing import StopStep, RTL


def test_evaluate():
    with patch("dovado.vivado_interaction.source", return_value=("", True)):
        with patch(
            "dovado.global_user_selections.METRICS",
            [("some_metric", "some_paragraph")],
        ):
            with patch(
                "dovado.report_parsing.get_utilisation", return_value=23,
            ):
                with patch("dovado.report_parsing.get_wns", return_value=100):
                    with patch(
                        "dovado.point_evaluation.evaluation_setup",
                        test.EvaluationSetup(
                            StopStep.SYNTHESIS,
                            RTL.VHDL,
                            True,
                            "rbs",
                            "examples/vhdl_ripple_borrow_subtractor",
                            "rbs.vhd",
                            250,
                        ),
                    ):

                        with patch(
                            "dovado.global_user_selections.FREE_PARAMETERS",
                            ["Nbit_rbs"],
                        ):
                            assert test.evaluate(
                                tuple([4])
                            ) == test.DesignValue(
                                utilisation={
                                    ("some_metric", "some_paragraph"): 23
                                },
                                negative_max_frequency=10.025062656641603,
                            )
                with patch("dovado.report_parsing.get_wns", return_value=100):
                    with patch(
                        "dovado.point_evaluation.evaluation_setup",
                        test.EvaluationSetup(
                            StopStep.SYNTHESIS,
                            RTL.VHDL,
                            True,
                            "rbs",
                            "examples/vhdl_ripple_borrow_subtractor",
                            "rbs.vhd",
                            250,
                        ),
                    ):

                        with patch(
                            "dovado.global_user_selections.FREE_PARAMETERS",
                            ["fake"],
                        ):
                            assert test.evaluate(
                                tuple([5])
                            ) == test.DesignValue(
                                utilisation={
                                    ("some_metric", "some_paragraph"): 23
                                },
                                negative_max_frequency=10.025062656641603,
                            )
