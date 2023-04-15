from dovado_rtl.generators.generator import Generator
from dovado_rtl.explorers.utilities.design_points import DesignPoint
import subprocess
from pathlib import Path
from importlib.resources import files
from typing import Optional
from nacolla.models import ImmutableModel


class VitisProject(ImmutableModel):
    project_root: str
    target_file: str
    target_module: str
    clock_port: Optional[str] = None
    target_clock: Optional[float] = None


class VitisGenerator(Generator):
    _tcl_file_name = "csynth.tcl"
    _generated_folder_name = "hls_generated"

    def generate(self, design_point: DesignPoint) -> DesignPoint:
        if design_point.extra is None or design_point.extra.get("vitis") is None:
            raise ValueError(
                "Please provide an extra.vitis section in the configuration file"
            )
        vitis_project = VitisProject(**design_point.extra["vitis"])

        target_path = Path(
            design_point.project_root, design_point.target_file
        ).relative_to(design_point.work_directory)

        tcl_path = str(
            files("dovado_rtl.generators.vitis").joinpath(VitisGenerator._tcl_file_name)
        )

        target_clock: float = (
            vitis_project.target_clock
            if vitis_project.target_clock is not None
            else design_point.target_clock
        )

        vitis_subcommands: list[str] = [
            "vitis_hls " + str(tcl_path),
            "-tclargs",
            "empty",
            "empty",
            VitisGenerator._generated_folder_name,  # output folder
            str(target_path),
            design_point.board,
            format(1000 / target_clock, "f"),  # target clock in nanoseconds
            vitis_project.target_module,
            str(
                design_point.project_root.relative_to(design_point.work_directory)
            ),  # directory to include
        ]

        vitis_command = " ".join(vitis_subcommands)

        vitis = subprocess.Popen(
            vitis_command,
            shell=True,
            stdout=subprocess.PIPE,
            cwd=design_point.work_directory,
        )
        vitis.wait()

        vitis_project_no_clock = {
            k: v for k, v in dict(vitis_project).items() if k != "target_clock"
        }

        generated_project_root = Path(
            design_point.work_directory,
            VitisGenerator._generated_folder_name,
            vitis_project.project_root,
        )
        return DesignPoint(
            **(
                dict(design_point)
                | vitis_project_no_clock
                | {"project_root": generated_project_root}
            )
        )
