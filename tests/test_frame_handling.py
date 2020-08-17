import dovado.frame_handling as test
import yaml
from pathlib import Path

CONFIG = yaml.safe_load(Path("config.yaml").open())


def test_fill():
    out = "tests/resources/fill_out"
    test.fill(
        CONFIG["XDC_DIR"] + CONFIG["CONSTRAINT_FRAME"],
        [str(1000 / 250)],
        CONFIG["PLACEHOLDER"],
        out,
    )
    assert (
        Path("tests/resources/fill_out").read_text()
        == "create_clock -period 4.0 [get_ports clk]\n"
    )
