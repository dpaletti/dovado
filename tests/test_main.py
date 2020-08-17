from unittest.mock import patch
import dovado.main as test
import pytest


@patch("dovado.user_input.ask_code_dir", lambda: "examples/vhdl_fifo_memory")
@patch("dovado.user_input.ask_top_module", lambda x: ("box", "boxed_fifo"))
@patch("dovado.user_input.ask_part", lambda: "xc7k70tfbv676-1")
@patch("dovado.user_input.ask_stop_step", lambda: "synthesis")
@patch(
    "dovado.user_input.ask_incremental_mode",
    lambda x: {"is synthesis incremental": True},
)
@patch(
    "dovado.user_input.ask_directives",
    lambda x, y: ("runtimeoptimized", None, None),
)
@patch("dovado.user_input.ask_clock", lambda: 250)
@patch(
    "dovado.user_input.ask_utilization_metrics",
    lambda x: ["Slice LUTs", "Slice Registers", "Block RAM Tile"],
)
@pytest.mark.skip("Time consuming and dependent on environment")
def test_synthesis_incremental():
    test.main()
