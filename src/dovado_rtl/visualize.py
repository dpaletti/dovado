from typing import Optional
from pathlib import Path
import typer
import pickle


def visualize(
    file_path: Path = typer.Option(  # pylint: disable=unused-argument
        ...,
        exists=True,
        file_okay=True,
        readable=True,
        resolve_path=True,
        help=("path of the file to visualize"),
    ),
    graph: Optional[str] = typer.Option(
        None, help="input which graph you would like to see"
    ),
):
    if file_path.suffix == ".pkl":
        f = open(file_path, "rb")
        try:
            res, algorithm = pickle.load(f)

        except Exception:
            raise Exception(
                "Could not unpack two values from pickled value, ensure pickle file is produced by dovado"
            )

    else:
        raise Exception("Unsupported file extension: " + str(file_path.stem))


def run_visualize():
    typer.run(visualize)
