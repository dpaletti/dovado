from dovado_rtl.input import Input
import shutil
from pathlib import Path
import os


def project_copy(project: Input) -> Input:
    copied_project = Path(project.work_directory, project.project_root.parts[-1])
    if copied_project.exists():
        if copied_project.is_dir():
            shutil.rmtree(copied_project)
        else:
            os.remove(copied_project)

    shutil.copytree(project.project_root, copied_project, dirs_exist_ok=False)
    return Input(
        **{k: v for k, v in dict(project).items() if k != "project_root"},
        project_root=copied_project
    )
