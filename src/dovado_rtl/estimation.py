from collections import OrderedDict
from functools import lru_cache
from typing import Tuple, List, Optional
from pathlib import Path
from random import randint, shuffle
import numpy as np
import skmultiflow as skm
from sklearn.kernel_ridge import KernelRidge
from scipy import stats
from dovado_rtl.enums import RegressionModel
from sklearn.model_selection import ShuffleSplit, RandomizedSearchCV
from dovado_rtl.config import Configuration
from dovado_rtl.abstract_classes import (
    AbstractEstimator,
    AbstractDesignPointEvaluator,
)
from dovado_rtl.simple_types import DesignValue, Example, Metric


class Estimator(AbstractEstimator):
    def __init__(
        self,
        regression_model: RegressionModel,
        design_point_evaluator: AbstractDesignPointEvaluator,
        free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
        dataset_size: int,
        config: Configuration,
        testing_estimation: bool,
        recording_design_values: bool,
        reading_design_values: bool,
    ):
        self.__regression_model = regression_model
        self.__reg = None
        self.__last_design_point = None
        self.__last_len = None
        self.__examples: List[Example] = []
        self.__design_point_evaluator: AbstractDesignPointEvaluator = design_point_evaluator
        self.__dataset_size: int = dataset_size
        self.__free_parameters_range = free_parameters_range
        self.__config: Configuration = config
        self.__testing_estimation: bool = testing_estimation
        self.__recording_design_values = recording_design_values
        self.__reading_design_values = reading_design_values
        self.__design_point_evaluator.set_estimator(self)
        self.__metrics: Optional[List[Metric]] = None
        if testing_estimation:
            self.__estimation_fname = str(
                self.__config.get_config("WORK_DIR")
            ) + str(self.__config.get_config("EST_TEST_CSV"))
            Path(self.__estimation_fname).open("w").close()
            Path(self.__estimation_fname).open("a").write(
                "Real, Estimated, Metric\n"
            )
        if self.__recording_design_values:
            self.__sample_fname = str(
                self.__config.get_config("WORK_DIR")
            ) + str(self.__config.get_config("SAMPLE_RECORD_CSV"))
            Path(self.__sample_fname).open("w").close()
            top_line = ""
            for k in free_parameters_range.keys():
                top_line += k + ","
            Path(self.__sample_fname).open("a").write(top_line)

        self.__generate_dataset()

    @lru_cache()
    def estimate(self, design_point: Tuple[int, ...], metric: Metric) -> float:
        if self.__regression_model is RegressionModel.KERNEL_RIDGE:
            estimate = self.__kernel_ridge(list(design_point), metric)
        elif self.__regression_model in {
            RegressionModel.STREAM_LEARNING_ISOUP,
            RegressionModel.STREAM_LEARNING_STACKED,
        }:
            estimate = self.__stream_learner(list(design_point), metric)
        else:
            raise Exception(
                "Learinig method "
                + str(self.__regression_model)
                + " is not implemented"
            )

        if self.__testing_estimation and len(self.__examples) > max(
            len(list(design_point)), 5
        ):
            evaluated = self.__design_point_evaluator.evaluate(
                tuple(design_point)
            )
            line = (
                str(evaluated.value[metric])
                + ","
                + str(estimate)
                + ","
                + (
                    str(metric.utilisation[0])
                    + "-"
                    + str(metric.utilisation[1])
                    if not metric.is_frequency
                    else "Frequency"
                )
            )

            Path(self.__estimation_fname).open("a").writelines([line + "\n"])

        return estimate

    def __prepare_data(
        self, design_point: List[int], metric: Optional[Metric] = None,
    ):
        X = self.__get_independent_variables()
        X = X.astype("int64").reshape(-1, len(design_point))
        if metric:
            y = self.__get_dependent_variables(metric=metric)
            y = y.astype("float64").reshape(-1, 1)
        else:
            y = self.__get_dependent_variables(metric=metric)
            if self.__metrics:
                y = y.astype("float64").reshape(-1, len(self.__metrics))
            else:
                raise Exception(
                    "Metrics not set while building data for estimator"
                )
        return X, y

    def __stream_learner(
        self, design_point: List[int], metric: Metric
    ) -> float:
        X, y = None, None
        if self.__last_design_point != design_point:
            X, y = self.__prepare_data(design_point)
        if not self.__last_design_point:
            if (
                self.__regression_model
                is RegressionModel.STREAM_LEARNING_ISOUP
            ):
                self.__reg = skm.trees.iSOUPTreeRegressor()
            elif (
                self.__regression_model
                is RegressionModel.STREAM_LEARNING_STACKED
            ):
                self.__reg = (
                    skm.trees.StackedSingleTargetHoeffdingTreeRegressor()
                )
            else:
                Exception("Streaming regression model not implemented")
            self.__reg.fit(X, y)
            self.__last_design_point = design_point
            self.__last_len = len(X)
        elif self.__last_design_point != design_point:
            if self.__last_len != len(X):
                start_index = -(self.__last_len - len(X))
                Xl = X[start_index:]
                yl = y[start_index:]
                Xl = Xl.astype("int64").reshape(-1, len(design_point))
                if self.__metrics:
                    yl = yl.astype("float64").reshape(-1, len(self.__metrics))
                else:
                    raise Exception(
                        "Metrics not initialized while partially fitting streaming learner"
                    )
                self.__reg.partial_fit(Xl, yl)
                self.__last_len = len(X)
            self.__last_design_point = design_point
        design_point = np.reshape(design_point, (1, -1))
        return self.__reg.predict(design_point)[0][
            self.__metrics.index(metric)
        ]

    def __kernel_ridge(self, design_point: List[int], metric: Metric) -> float:
        X, y = None, None
        if self.__last_design_point != design_point:
            X, y = self.__prepare_data(design_point)

        if (
            self.__last_design_point != design_point
            and self.__last_len != len(X)
        ):
            self.__reg = KernelRidge()
            parameters = {
                "alpha": stats.loguniform(a=1e-4, b=1e2),
                "gamma": stats.expon(scale=0.1),
                "kernel": ["rbf"],
            }
            cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
            self.__reg = RandomizedSearchCV(
                self.__reg,
                parameters,
                cv=cv,
                n_iter=50,
                scoring="neg_root_mean_squared_error",
                n_jobs=-1,
            )
            self.__reg.fit(X, y)
            self.__last_design_point = design_point
            self.__last_len = len(X)
        design_point = np.reshape(design_point, (1, -1))
        return self.__reg.predict(design_point)[0][
            self.__metrics.index(metric)
        ]

    def add_example(self, example: Example) -> None:
        if not self.__metrics:
            self.__metrics = self.__design_point_evaluator.get_metrics()
        self.__examples.append(example)
        shuffle(self.__examples)
        self.__examples_updated = True
        if self.__recording_design_values:
            opened_file = Path(self.__sample_fname).open("a")
            if Path(self.__sample_fname).read_text()[-1] == ",":
                top_line = ""
                for m in example.design_value.value.keys():
                    top_line += (
                        m.utilisation[0] + "-" + m.utilisation[1]
                        if not m.is_frequency
                        else "Frequency"
                    ) + ","
                opened_file.write(top_line[:-1] + "\n")
            line = ""
            for i in example.design_point:
                line += str(i) + ","
            for j in example.design_value.value.values():
                line += str(j) + ","
            opened_file.write(line[:-1] + "\n")
            opened_file.close()

    @staticmethod
    def evaluate_random_design_point(
        free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
        evaluator: AbstractDesignPointEvaluator,
    ) -> Tuple[List[int], DesignValue]:

        design_point = []
        for k in free_parameters_range.keys():
            design_point.append(
                randint(
                    free_parameters_range[k][0], free_parameters_range[k][1],
                )
            )
        return design_point, evaluator.evaluate(tuple(design_point))

    def __generate_dataset(self) -> None:
        design_value = None
        if self.__reading_design_values:
            lines = (
                Path(
                    str(self.__config.get_config("WORK_DIR"))
                    + str(self.__config.get_config("SAMPLE_RECORD_CSV"))
                )
                .read_text()
                .split("\n")
            )
            splitted_top_line = lines[0].split(",")
            metrics_to_set = True
            metrics = []
            for line in lines[1:]:
                try:
                    design_point = []
                    splitted_line = line.split(",")
                    i = 0
                    for _ in self.__free_parameters_range.keys():
                        design_point.append(float(splitted_line[i]))
                        i += 1

                    design_value = DesignValue({})
                    for v in splitted_line[i:]:
                        if splitted_top_line[i] == "Frequency":
                            metric = Metric(None, True)
                        else:
                            util = splitted_top_line[i].split("-")
                            metric = Metric((util[0], util[1]), False)
                        if metrics_to_set:
                            metrics.append(metric)
                        design_value.value[metric] = float(v)
                        i += 1
                    if metrics_to_set:
                        self.__design_point_evaluator.set_metrics(metrics)
                        metrics_to_set = False

                    self.add_example(
                        Example(
                            design_point=design_point,
                            design_value=design_value,
                        )
                    )
                except Exception:
                    print(
                        "Error while parsing line '" + str(line) + "' skipping"
                    )
            return

        for _ in range(0, self.__dataset_size):
            (
                design_point,
                design_value,
            ) = Estimator.evaluate_random_design_point(
                self.__free_parameters_range, self.__design_point_evaluator
            )
            if design_value:
                self.add_example(
                    Example(
                        design_point=design_point, design_value=design_value
                    )
                )
        if not design_value:
            raise Exception(
                "Could not find any valid design point while sampling from the given ranges"
                + " please make sure the ranges are correct. You may try again or modify dataset size if ranges are correct."
            )

    def __get_dependent_variables(
        self, metric: Optional[Metric] = None
    ) -> "np.ndarray":
        dependent_variable = []
        if not metric:
            for example in self.__examples:
                dependent_variable.append(
                    list(example.design_value.value.values())
                )
        else:
            for example in self.__examples:
                dependent_variable.append(example.design_value.value[metric])
        return np.array(dependent_variable)

    def __get_independent_variables(self) -> "np.ndarray":
        independent_variables = []
        for example in self.__examples:
            independent_variables.append(example.design_point)
        return np.array(independent_variables)

    def get_examples(self):
        return self.__examples
