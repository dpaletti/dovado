import dovado.report_parsing as test
import tests.vivado_2019_2_mock_data as version_dependent
import pytest


def test_get_utilisation():
    assert (
        test.get_utilisation(
            "./examples/vhdl_fifo_memory/post_synth_util.xml",
            "Slice Logic",
            "LUT as Logic",
        )
        == 0.03
    )
    assert (
        test.get_utilisation(
            "./examples/vhdl_fifo_memory/post_synth_util.xml", "DSP", "DSPs",
        )
        == 0.00
    )


def test_get_wns():
    assert (
        test.get_wns("./examples/vhdl_fifo_memory/post_synth_setup_timing.rpt")
        == -6.486
    )
    with pytest.raises(FileNotFoundError):
        test.get_wns("./wrong_file")
    with pytest.raises(Exception):
        test.get_wns("./examples/vhdl_fifo_memory/fifo.vhd")
