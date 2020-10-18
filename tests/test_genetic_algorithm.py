from unittest.mock import patch, Mock
import dovado.genetic_algorithm as test
import dovado.estimation as es
import dovado.point_evaluation as pe
import pytest


@pytest.mark.skip("To Fix")
def test_optimize():
    example1 = es.Example(
        design_point={
            "test_parameter_1": 1,
            "test_parameter_2": 3,
            "test_parameter_3": 45,
        },
        design_value=pe.DesignValue(
            utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34},
            negative_max_frequency=-128,
        ),
    )

    example2 = es.Example(
        design_point={
            "test_parameter_1": 2,
            "test_parameter_2": 4,
            "test_parameter_3": 46,
        },
        design_value=pe.DesignValue(
            utilisation={
                ("paragraph_1, metric_1"): -122,
                ("paragraph_2", "metric_1"): 13,
                ("paragraph_3", "metric_2"): 35,
            },
            negative_max_frequency=-130,
        ),
    )
    with patch(
        "dovado.global_user_selections.FREE_PARAMETERS",
        ["test_parameter_1", "test_parameter_2", "test_parameter_3"],
    ):
        with patch(
            "dovado.global_user_selections.METRICS",
            [
                ("paragraph_1, metric_1"),
                ("paragraph_2", "metric_1"),
                ("paragraph_3", "metric_2"),
            ],
        ):
            with patch(
                "dovado.global_user_selections.FREE_PARAMETERS_RANGE",
                {
                    "test_parameter_1": (0, 100),
                    "test_parameter_2": (20, 200),
                    "test_parameter_3": (30, 40),
                },
            ):
                with patch("dovado.estimation.examples", [example1, example2]):
                    with patch(
                        "dovado.point_evaluation.evaluate",
                        return_value=pe.DesignValue(
                            utilisation={
                                ("paragraph_1, metric_1"): -123,
                                ("paragraph_2", "metric_1"): 12,
                                ("paragraph_3", "metric_2"): 34,
                            },
                            negative_max_frequency=-128,
                        ),
                    ):
                        assert test.optimize("00:00:01").tolist() == [
                            -123,
                            12,
                            34,
                        ]
