from cmath import pi
from collections import OrderedDict
from typing import Tuple, List, Optional
from pathlib import Path
from random import randint, shuffle
import numpy as np
from sklearn.kernel_ridge import KernelRidge
from scipy import stats
from dovado_rtl.enums import RegressionModel
from sklearn.model_selection import LeaveOneOut, RandomizedSearchCV
from dovado_rtl.config import Configuration
from dovado_rtl.abstract_classes import (
    AbstractEstimator,
    AbstractDesignPointEvaluator,
)
from dovado_rtl.simple_types import Example, Metric


class Estimator(AbstractEstimator):
    def __init__(
        self,
        regression_model: RegressionModel,
        design_point_evaluator: AbstractDesignPointEvaluator,
        free_parameters_range: "OrderedDict[str, Tuple[int, int]]",
        dataset_size: int,
        config: Configuration,
    ):
        self.__regression_model = regression_model
        self.__examples: List[Example] = []
        self.__examples_updated: bool = True
        self.__estimator = None
        self.__design_point_evaluator: AbstractDesignPointEvaluator = design_point_evaluator
        self.__dataset_size: int = dataset_size
        self.__config: Configuration = config
        self.__design_point_evaluator.set_estimator(self)
        self.__metrics: Optional[List[Metric]] = None
        if self.__config.get_config("ESTIMATION_TESTING"):
            self.__fname = str(self.__config.get_config("WORK_DIR")) + str(
                self.__config.get_config("EST_TEST_CSV")
            )
            Path(self.__fname).open("w").close()
        self.__generate_dataset(free_parameters_range,)

    def estimate(self, design_point: List[int], metric: Metric) -> float:
        if self.__regression_model is RegressionModel.KERNEL_RIDGE:
            estimate = self.__kernel_ridge(design_point, metric)
        else:
            raise Exception("Other models still need to be implemented")

        if self.__config.get_config("ESTIMATION_TESTING") and len(
            self.__examples
        ) > max(len(list(design_point)), 5):
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

            Path(self.__fname).open("a").writelines([line + "\n"])

        return estimate

    def __kernel_ridge(self, design_point: List[int], metric: Metric) -> float:
        X = self.__get_independent_variables()
        X = X.astype("int64").reshape(-1, len(design_point))
        y = self.__get_dependent_variables(metric)
        y = y.astype("float64").reshape(-1, 1)
        reg = KernelRidge()
        parameters = {
            "alpha": stats.reciprocal(a=1e-7, b=1e2, size=10),
            "gamma": stats.expon(scale=0.1),
            "kernel": ["rbf"],
        }
        cv = LeaveOneOut()
        cv_reg = RandomizedSearchCV(
            reg,
            parameters,
            cv=cv,
            scoring="neg_root_mean_squared_error",
            n_jobs=-1,
        )
        cv_reg.fit(X, y)
        design_point = np.reshape(design_point, (1, -1))
        return cv_reg.predict(design_point)[0][0]

    def add_example(self, example: Example) -> None:
        if not self.__metrics:
            self.__metrics = self.__design_point_evaluator.get_metrics()
        self.__examples.append(example)
        shuffle(self.__examples)
        self.__examples_updated = True

    def __generate_dataset(
        self, parameters_range: "OrderedDict[str, Tuple[int, int]]",
    ) -> None:
        for _ in range(0, self.__dataset_size):
            design_point = []
            for k in parameters_range.keys():
                design_point.append(
                    randint(parameters_range[k][0], parameters_range[k][1])
                )
            design_value = self.__design_point_evaluator.evaluate(
                tuple(design_point)
            )
            self.add_example(
                Example(design_point=design_point, design_value=design_value)
            )

    def __get_dependent_variables(self, metric: Metric) -> "np.ndarray":
        dependent_variable = []
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
