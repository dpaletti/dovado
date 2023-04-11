from dovado_rtl.generators.generator import Generator
from nacolla.models import ImmutableModel
from dovado_rtl.explorers.utilities.design_points import DesignPoint
import subprocess
from pathlib import Path


class GeneratedProject(ImmutableModel):
    command: str
    project_root: str
    target_file: str
    target_module: str


class BashGenerator(Generator):
    def generate(self, design_point: DesignPoint) -> DesignPoint:
        if design_point.extra is None or design_point.extra["generate"] is None:
            raise ValueError(
                "Please add an extra.generate section with the command to run and the new project root"
            )
        generated_project = GeneratedProject(**design_point.extra["generate"])

        bash_command = subprocess.Popen(
            generated_project.command,
            shell=True,
            stdout=subprocess.PIPE,
            cwd=design_point.work_directory,
        )
        bash_command.wait()

        return DesignPoint(
            **(
                dict(design_point)
                | {
                    "project_root": Path(
                        design_point.work_directory, generated_project.project_root
                    ),
                    "target_file": generated_project.target_file,
                    "target_module": generated_project.target_module,
                }
            )
        )
