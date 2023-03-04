from pathlib import Path
from dovado_rtl.input import Input
from dovado_rtl.vivado import Vivado
import toml
import sys


def main() -> None:
    vivado = Vivado()
    input_data = Input(**toml.load(parse_config_path()))

    check_board(vivado, input_data.board)


def parse_config_path() -> Path:
    if len(sys.argv) == 1:
        raise ValueError("Missing the path to the configuration file")
    return Path(sys.argv[1])


def check_board(vivado: Vivado, board: str) -> None:
    if not vivado.is_board_valid(board):
        raise ValueError(
            "Board '"
            + str(board)
            + "' is invalid. Please pick one among:\n"
            + str(set(vivado.get_boards().keys()))
        )
