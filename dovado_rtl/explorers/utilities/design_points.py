from dovado_rtl.explorers.utilities.spaces import SOURCE_PATH
from dovado_rtl.explorers.utilities.tasks import ParsedProject
from dovado_rtl.parsers.utilities.parsed import MODULE_NAME_STR, PARAMETER_NAME_STR


class DesignPoint(ParsedProject):
    points: dict[SOURCE_PATH, dict[MODULE_NAME_STR, dict[PARAMETER_NAME_STR, str]]]

    def vectorized(self) -> list[int]:
        output_vector = []
        for _, module_to_parameters in self.points.items():
            for _, parameter_to_value in module_to_parameters.items():
                for _, value in parameter_to_value.items():
                    output_vector.append(int(value))
        return output_vector

    def get_sources(self) -> list[SOURCE_PATH]:
        return list(self.points.keys())

    def get_modules(self, source: SOURCE_PATH) -> list[MODULE_NAME_STR]:
        return list(self.points[source].keys())

    def get_parameters(
        self, source: SOURCE_PATH, module: MODULE_NAME_STR
    ) -> list[PARAMETER_NAME_STR]:
        return list(self.points[source][module].keys())

    def get_parameter_value(
        self,
        source: SOURCE_PATH,
        module: MODULE_NAME_STR,
        parameter: PARAMETER_NAME_STR,
    ) -> str:
        return self.points[source][module][parameter]

    @staticmethod
    def make_design_point_from_vector(
        vector: list[int],
        parameters_structure: dict[
            SOURCE_PATH, dict[MODULE_NAME_STR, list[PARAMETER_NAME_STR]]
        ],
        parsed_project: ParsedProject,
    ) -> "DesignPoint":
        points = {}
        current_vector_position = -1
        for source, module_to_parameter in parameters_structure.items():
            points[source] = {}
            for module, parameters in module_to_parameter.items():
                points[source][module] = {}
                for parameter in parameters:
                    current_vector_position += 1
                    if current_vector_position == len(vector):
                        raise ValueError(
                            "The vector provided to build the design point '"
                            + str(vector)
                            + "' is shorter than the number of available parameters."
                        )
                    points[source][module][parameter] = str(
                        vector[current_vector_position]
                    )

        if current_vector_position != len(vector) - 1:
            raise ValueError(
                "The design point vector has length "
                + str(len(vector))
                + " but only "
                + str(current_vector_position)
                + " parameters can be explored."
            )
        return DesignPoint(**(dict(parsed_project) | {"points": points}))


class EvaluatedDesignPoint(DesignPoint):
    design_value: dict[str, float]

    class Config:
        extra = "allow"
