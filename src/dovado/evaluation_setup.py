from dataclasses import dataclass


@dataclass
class EvaluationSetup:
    src_folder: str
    top_module: str
    synthesis_part: str
    synthesis_directive: str
    incremental_mode: str
    stop_step: str
    top_suffix: str
    target_clock: str
    place_directive: str = ""
    route_directive: str = ""
