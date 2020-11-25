import dovado.fitness as test
import dovado.estimation as es
import dovado.point_evaluation as pe
from unittest.mock import patch
import yaml
from pathlib import Path
import pytest

CONFIG = yaml.safe_load(Path("config.yaml").open())
threshold = 4


@pytest.mark.skip("To Fix")
def test_fitness():

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
        is_infinite=False,
    )

    example2 = es.Example(
        design_point={
            "test_parameter_1": 2,
            "test_parameter_2": 4,
            "test_parameter_3": 46,
        },
        design_value=pe.DesignValue(
            utilisation={"metric_1": -122, "metric_2": 13, "metric_3": 35},
            negative_max_frequency=-130,
        ),
        is_infinite=False,
    )

    example3 = es.Example(
        design_point={
            "test_parameter_1": 1 - (threshold + 1),
            "test_parameter_2": 3,
            "test_parameter_3": 45,
        },
        design_value=pe.DesignValue(
            utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34,},
            negative_max_frequency=-128,
        ),
        is_infinite=False,
    )
    with patch("dovado.estimation.examples", [example1, example2]):
        with patch(
            "dovado.point_evaluation.evaluate",
            return_value=pe.DesignValue(
                utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34},
                negative_max_frequency=-128,
            ),
        ):
            assert test.fitness(tuple([1, 3, 45]), "metric_1") == -123
            assert (
                test.fitness(tuple(example3.design_point.values()), "metric_1")
                == -123
            )
            assert example3 in es.__examples
        with patch("dovado.estimation.estimate", return_value=-120):

            assert test.fitness(tuple([0, 3, 44]), "metric_1") == -120


def test__distance():
    with pytest.raises(ValueError):
        test.__distance([1, 2, 3], [1, 2])
