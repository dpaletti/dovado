import os
from pathlib import Path
from pydantic import ValidationError
import pytest
import toml

from dovado_rtl.input import Input


def test_input():
    path_prexif: str = os.curdir + "/resources"

    to_parse_broken = Path(path_prexif + "/broken_test_config.toml")
    with pytest.raises(ValidationError):
        Input(**toml.load(to_parse_broken))

    to_parse = Path(path_prexif + "/test_config.toml")
    input_data = Input(**toml.load(to_parse))

    assert input_data.board == "some_board_name"
    assert input_data.target_file == Path(
        "./resources/neorv32/rtl/core/neorv32_top.vhd"
    )
    assert input_data.task_file == Path(
        "./resources/neorv32/test_exploration_file.json"
    )
    assert input_data.target_module == "neorv32_top"
    assert input_data.clock_port == "clk_port_identifier"

    assert input_data.synthesis_directives == ["RuntimeOptimized"]
    assert input_data.implementation_directives == ["RuntimeOptimized"]
