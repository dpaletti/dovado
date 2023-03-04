from pathlib import Path
from typing import Optional
from nacolla import ImmutableModel
from pydantic import DirectoryPath, FilePath


class Input(ImmutableModel):
    project_root: DirectoryPath  # all paths in the exploration file are appended to this path
    target_file: Path  # the full path for the target file is computed by appending this to the project root.
    task_file: FilePath  # the full path to the task file
    board: str
    clock_port: str
    target_module: Optional[str] = None
    implementation: bool = False
    incremental: bool = False
    synthesis_directives: list[str] = ["RuntimeOptimized"]
    implementation_directives: list[str] = ["RuntimeOptimized"]
    target_clock: int = 1000
    metrics: Optional[list[int]] = None
