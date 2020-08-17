import dovado.report_parsing as test
import tests.vivado_2019_2_mock_data as version_dependent
import pytest


def test_get_utilisation():
    assert (
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "./examples/vhdl_fifo_memory/post_synth_util.xml",
            "Util%",
            "LUT as Logic",
        )
        == 0.03
    )
    assert (
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "./examples/vhdl_fifo_memory/post_synth_util.xml",
            "Util%",
            "DSPs",
        )
        == 0.00
    )
    with pytest.raises(ValueError):
        test.get_utilisation(
            ["wrong_metrics"],
            ["wrong titles", "wronger"],
            "ignored",
            "ignored",
            "ignored",
        )

    with pytest.raises(FileNotFoundError):
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "./non_existent_file",
            "Ignored",
            "Ignored",
        )

    with pytest.raises(Exception):
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "",
            "Ignored",
            "Ignored",
        )
    with pytest.raises(Exception):
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "",
            "Wrong Column",
            "DSPs",
        )
    with pytest.raises(Exception):
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "./examples/vhdl_fifo_memory/post_synth_util.xml",
            "Wrong Column",
            "DSPs",
        )
    with pytest.raises(Exception):
        test.get_utilisation(
            version_dependent.available_utilization_metrics,
            version_dependent.utilization_titles,
            "./examples/vhdl_fifo_memory/post_synth_util.xml",
            "Util%",
            "Wrong Row",
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
