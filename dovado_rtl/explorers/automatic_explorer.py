from pathlib import Path
from typing import Any, Callable, Iterable, Literal, Optional, Union
from movado import approximate
from pymoo.core.problem import ElementwiseProblem, Problem
from pymoo.core.repair import Repair
from pymoo.core.algorithm import Algorithm
from pymoo.core.result import Result
from pymoo.core.termination import Termination
from pymoo.factory import get_crossover, get_mutation, get_sampling, get_termination
from pymoo.optimize import minimize
from dovado_rtl.explorers.utilities.design_points import (
    DesignPoint,
    EvaluatedDesignPoint,
)
from dovado_rtl.explorers.explorer import EndExploration, Explorer
import numpy as np
from dovado_rtl.explorers.utilities.spaces import SOURCE_PATH
from dovado_rtl.explorers.utilities.tasks import (
    AutomaticExplorationProject,
    ParsedProject,
)

from threading import Lock

from dovado_rtl.parsers.utilities.parsed import MODULE_NAME_STR, PARAMETER_NAME_STR

from queue import SimpleQueue

import importlib
from threading import Thread


class EndResult(EndExploration):
    result: Result


class AutomaticExplorer(Explorer):
    __pymoo_package_structure = "pymoo.algorithms.moo"
    __seed = 0
    __parameter_file_name = "parameters"
    __metrics_file_name = "metrics"

    def __init__(self) -> None:
        super().__init__()
        self._approximation_to_initialize = True
        self._parameters_structure: dict[
            SOURCE_PATH, dict[MODULE_NAME_STR, list[PARAMETER_NAME_STR]]
        ] = {}
        self._parsed_project: Optional[ParsedProject] = None

        self._evaluated_points: list[tuple[list[int], EvaluatedDesignPoint]] = []
        self._points_under_evaluation: list[tuple[list[int], Lock]] = []
        self._points_queue: SimpleQueue[
            Union[list[Union[list[int], bool]], EndResult]
        ] = SimpleQueue()
        self._metrics: list[str] = []
        self._task: Optional[AutomaticExplorationProject] = None

    def update(
        self, evaluated_design_point: Union[EvaluatedDesignPoint, EndExploration]
    ) -> Union[DesignPoint, EndExploration]:
        if isinstance(evaluated_design_point, EndExploration):
            return EndExploration()

        self._evaluated_points.append(
            (evaluated_design_point.vectorized(), evaluated_design_point)
        )

        self._release(evaluated_design_point)

        point = self._get_next_design_point()

        if isinstance(point, EndResult):
            self._save_results(point.result)
            return EndExploration()

        if self._task is None:
            raise ValueError("Please save the task in explore, found it None")

        self._set_point(point, self._task)

        if self._parsed_project is None:
            raise ValueError(
                "Found None parsed_project in automatic explorer, please save it in the explore method"
            )

        return DesignPoint.make_design_point_from_vector(
            vector=point,
            parameters_structure=self._parameters_structure,
            parsed_project=self._parsed_project,
        )

    def explore(self, task: AutomaticExplorationProject) -> DesignPoint:
        self._task = task
        self._parsed_project = self._task.get_parsed_project()
        self._metrics = self._task.default_metrics + list(
            self._task.custom_metrics.keys()
        )
        self._parameters_structure = self._task.space.get_structure()

        problem = ApproximatedProblem(self, task)
        genetic_algorithm = self._make_genetic_algorithm(task)
        termination = self._make_genetic_setting(task.termination, get_termination)

        Thread(
            target=self._run_optimization,
            args=(problem, genetic_algorithm, termination),
        ).start()

        point = self._get_next_design_point()
        if isinstance(point, EndResult):
            raise ValueError(
                "Exploration stopped before starting, found 'End' as first point to evaluate."
            )
        self._set_point(point, self._task)

        design_point = DesignPoint.make_design_point_from_vector(
            vector=point,
            parameters_structure=self._parameters_structure,
            parsed_project=self._parsed_project,
        )

        return design_point

    def _evaluate(self, point: list[int]) -> list[float]:
        evaluation = self._get_evaluation(point)
        if evaluation is not None:
            return evaluation

        lock = Lock()
        lock.acquire()
        self._points_under_evaluation.append((point, lock))
        point_to_evaluate = [point, True]
        self._points_queue.put(point_to_evaluate)
        lock.acquire()

        point_to_evaluate[1] = False
        self._points_under_evaluation.remove((point, lock))

        evaluation = self._get_evaluation(point)

        if evaluation is None:
            raise ValueError("Cannot find evaluation for point " + str(point))

        return evaluation

    def _release(self, evaluated_design_point: EvaluatedDesignPoint):
        for (point, lock) in self._points_under_evaluation:
            if point == evaluated_design_point.vectorized():
                lock.release()
                return
        raise ValueError(
            "Could not find "
            + str(evaluated_design_point.vectorized())
            + " among points under evaluation."
        )

    def _save_results(self, result: Result):
        best_parameters_set: Optional[Iterable] = result.X
        best_metrics_set: Optional[Iterable] = result.F

        if self._task is None:
            print(best_parameters_set)
            print(best_metrics_set)
            raise ValueError("Cannot save results, found None task")

        Path(self._task.work_directory).mkdir(exist_ok=True)
        parameter_file = Path(
            self._task.work_directory,
            self._get_file_name(self._task.work_directory, self.__parameter_file_name),
        )
        metrics_file = Path(
            self._task.work_directory,
            self._get_file_name(self._task.work_directory, self.__metrics_file_name),
        )
        parameter_file.touch()
        metrics_file.touch()

        Explorer._add_row_to_output(self._task.space.get_parameters(), parameter_file)
        Explorer._add_row_to_output(self._metrics, metrics_file)

        if best_parameters_set is None or best_metrics_set is None:
            print("Optimization did not converge")
            return

        for best_parameters in best_parameters_set:
            Explorer._add_row_to_output(best_parameters, parameter_file)

        for best_metrics in best_metrics_set:
            Explorer._add_row_to_output(best_metrics, metrics_file)

    def _set_point(self, point: list[int], task: AutomaticExplorationProject) -> None:
        to_write = {}
        current_parameter = -1
        for source, module_to_parameter in self._parameters_structure.items():
            for module, parameters in module_to_parameter.items():
                to_write[module] = {}
                for parameter in parameters:
                    current_parameter += 1
                    if len(point) == current_parameter:
                        raise ValueError(
                            "Found a point dimensionally smaller than the number of parameters "
                            + str(point)
                        )
                    to_write[module][parameter] = str(point[current_parameter])

            parsed = task.parameter_sources[source]
            Path(task.project_root, source).open("w").write(parsed.replace(to_write))

    def _run_optimization(
        self, problem: Problem, algorithm: Algorithm, termination: Termination
    ) -> None:
        result = minimize(
            problem,
            algorithm,
            termination,
            seed=self.__seed,
            save_history=False,  # this cannot be turne on due to threading
            verbose=True,
        )
        self._points_queue.put(EndResult(result=result))

    def _get_next_design_point(self) -> Union[list[int], EndResult]:
        queue_item = self._points_queue.get()
        if isinstance(queue_item, EndResult):
            return queue_item
        point, to_be_evaluated = tuple(queue_item)
        while not to_be_evaluated:
            queue_item = self._points_queue.get()
            if isinstance(queue_item, EndResult):
                return queue_item
            point, to_be_evaluated = tuple(queue_item)

        if type(point) is list:
            return point
        raise ValueError(
            "Found a point " + str(point) + " which is not a list of integers."
        )

    def _make_genetic_algorithm(self, task: AutomaticExplorationProject) -> Algorithm:
        pop_size = task.options.get("pop_size")
        optional_n_offspring = task.options.get("n_offspring")
        if pop_size is None:
            raise ValueError(
                "Population size None, it is mandatory to initalize genetic algorithm"
            )

        return self._get_algorithm_class(task.algorithm)(
            repair=StepRepair(task.space.steps()),
            pop_size=pop_size * task.space.number_of_parameters(),
            n_offsprings=optional_n_offspring * task.space.number_of_parameters()
            if optional_n_offspring is not None
            else None,
            sampling=self._make_genetic_setting(task.sampling, get_sampling),
            crossover=self._make_genetic_setting(task.crossover, get_crossover),
            mutation=self._make_genetic_setting(task.mutation, get_mutation),
        )

    @staticmethod
    def _make_genetic_setting(
        settings_dict: dict[str, Any], factory: Callable[..., Any]
    ) -> Any:
        method = settings_dict.get("method")
        if method is None:
            return None
        kwargs = {k: v for k, v in settings_dict.items() if k != "method"}
        return factory(method, **kwargs)

    def _get_algorithm_class(self, algorithm_name: str) -> type[Algorithm]:
        algorithm_module = importlib.import_module(
            self.__pymoo_package_structure + "." + algorithm_name.lower()
            if algorithm_name.lower() != "agemoea"
            else "age"
        )
        return getattr(algorithm_module, algorithm_name.upper())

    def _get_evaluation(self, point: list[int]) -> Optional[list[float]]:
        for stored_point, evaluation in self._evaluated_points:
            if stored_point == point:
                self._evaluated_points.remove((stored_point, evaluation))
                return [evaluation.design_value[metric] for metric in self._metrics]
        return None


class ApproximatedProblem(ElementwiseProblem):
    def __init__(self, explorer: AutomaticExplorer, task: AutomaticExplorationProject):
        ranges = [range for _, range in task.space.get_ranges()]
        self._explorer = explorer
        self._objectives = len(task.default_metrics) + len(task.custom_metrics)
        self._fitness = approximate(
            outputs=self._objectives,
            controller=task.approximation_options["controller"],
            estimator=task.approximation_options["estimator"],
            disabled=not task.approximate,
            debug=True,
        )(self._explorer._evaluate)
        super().__init__(
            n_var=task.space.number_of_parameters(),
            n_obj=self._objectives,
            xl=[range.start for range in ranges],
            xu=[range.end for range in ranges],
            type_var=np.int_,
        )

    def _evaluate(self, x: Iterable[int], out, **kwargs) -> None:
        # kwargs accomodates pymoo abstraction, do not remove
        fitness = self._fitness(list(x))
        out["F"] = fitness


class StepRepair(Repair):
    def __init__(self, repairs: list[Union[int, Literal["powers_of_two"]]]) -> None:
        self.__repairs = repairs
        super().__init__()

    def _do(self, problem, pop, **kwargs):
        # The signature accomodates pymoo abstraction do not remove unused parameters
        for k, _ in enumerate(pop):
            point = pop[k].X
            for parameter, repair in enumerate(self.__repairs):
                if repair == "powers_of_two":
                    point[parameter] = self._repair_to_power_of_two(point[parameter])
                else:
                    point[parameter] = self._repair_to_step(point[parameter], repair)
        return pop

    @staticmethod
    def _repair_to_step(value_to_repair: int, step: int):
        if step <= 1:
            return value_to_repair

        larger_multiple: int = np.floor(value_to_repair / step) * step
        smaller_multiple: int = np.ceil(value_to_repair / step) * step
        larger_to_value_distance: int = larger_multiple - value_to_repair
        smaller_to_value_distance: int = value_to_repair - smaller_multiple

        if larger_to_value_distance == smaller_to_value_distance:
            if np.random.random() < 0.5:
                return smaller_multiple

            return larger_multiple

        if larger_to_value_distance < smaller_to_value_distance:
            return larger_multiple

        return smaller_multiple

    @staticmethod
    def _repair_to_power_of_two(value_to_repair: int):
        next_power_of_two = value_to_repair
        next_power_of_two -= 1
        next_power_of_two |= next_power_of_two >> 1
        next_power_of_two |= next_power_of_two >> 2
        next_power_of_two |= next_power_of_two >> 4
        next_power_of_two |= next_power_of_two >> 8
        next_power_of_two |= next_power_of_two >> 16
        next_power_of_two += 1

        previous_power_of_two = next_power_of_two >> 1
        if np.random.random() < 0.5:
            return previous_power_of_two
        else:
            return next_power_of_two
