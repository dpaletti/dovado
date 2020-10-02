import dovado.estimation as test
from dovado.point_evaluation import DesignValue
from dovado.global_user_selections import set_free_parameters, FREE_PARAMETERS
from unittest.mock import patch

example = test.Example(
    design_point={
        "test_parameter_1": 1,
        "test_parameter_2": 3,
        "test_parameter_3": 45,
    },
    design_value=DesignValue(
        utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34},
        negative_max_frequency=-128,
    ),
)

parameters_range = {
    "test_parameter_1": (1, 100),
    "test_parameter_2": (0, 20),
    "test_parameter_3": (-123, 123),
}


def test_add_example():
    test.examples = []
    test.add_example(example)
    assert test.examples == [example]


def test_generate_dataset():
    test.examples = []
    global example
    with patch("dovado.estimation.evaluate", return_value=example):
        test.generate_dataset(
            4,
            parameters_range,
            ["test_parameter_1", "test_parameter_2", "test_parameter_3",],
        )
        for example in test.examples:
            for parameter in example.design_point.keys():
                for ex in test.examples:
                    for parameter in ex.design_point.keys():
                        assert (
                            parameters_range[parameter][0]
                            <= ex.design_point[parameter]
                            <= parameters_range[parameter][1]
                        )


def test_get_dependent_variable():
    example = test.Example(
        design_point={
            "test_parameter_1": 1,
            "test_parameter_2": 3,
            "test_parameter_3": 45,
        },
        design_value=DesignValue(
            utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34},
            negative_max_frequency=-128,
        ),
    )
    test.examples = []
    assert test.get_dependent_variable([example] * 2, "metric_1").tolist() == [
        -123,
        -123,
    ]


def test_get_independent_variable():
    example = test.Example(
        design_point={
            "test_parameter_1": 1,
            "test_parameter_2": 3,
            "test_parameter_3": 45,
        },
        design_value=DesignValue(
            utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34},
            negative_max_frequency=-128,
        ),
    )
    test.examples = []
    assert test.get_independent_variables(
        [example] * 2,
        ["test_parameter_1", "test_parameter_2", "test_parameter_3"],
    ).tolist() == [[1, 1], [3, 3], [45, 45]]


def test_design_point():
    design_point = [2.2, 4.2, 42.2]
    example1 = test.Example(
        design_point={
            "test_parameter_1": 1,
            "test_parameter_2": 3,
            "test_parameter_3": 45,
        },
        design_value=DesignValue(
            utilisation={"metric_1": -123, "metric_2": 12, "metric_3": 34},
            negative_max_frequency=-128,
        ),
    )
    example2 = test.Example(
        design_point={
            "test_parameter_1": 2,
            "test_parameter_2": 4,
            "test_parameter_3": 46,
        },
        design_value=DesignValue(
            utilisation={"metric_1": -122, "metric_2": 13, "metric_3": 35},
            negative_max_frequency=-130,
        ),
    )
    test.examples = [example1] + [example2]
    set_free_parameters(
        ["test_parameter_1", "test_parameter_2", "test_parameter_3"]
    )
    print("FREE_PARAMETERS: " + str(FREE_PARAMETERS))
    assert test.estimate(design_point, "metric_1") == -10.554285714285697
