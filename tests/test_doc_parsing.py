import dovado.doc_parsing as test
import pytest
from hypothesis import given, example
from hypothesis.strategies import text
import tests.vivado_2019_2_mock_data as version_dependent
from unittest.mock import patch


@given(command=text())
@example(command="synthesis")
@example(command="place")
@example(command="route")
@example(command="read checkpoint")
def test_get_directives_paragraph(command):
    if command not in {"synthesis", "place", "route", "read checkpoint"}:
        pytest.raises(ValueError, test.get_directives_paragraph, command)
        return
    if command == "synthesis":
        with patch(
            "dovado.vivado_interaction.get_help",
            lambda x: version_dependent.help_synth_design,
        ):
            assert test.get_directives_paragraph(
                command
            ) in version_dependent.synth_directives_paragraph.replace(
                "\n\n", "\n"
            )
    elif command == "place":
        with patch(
            "dovado.vivado_interaction.get_help",
            lambda x: version_dependent.help_place_design,
        ):
            assert test.get_directives_paragraph(
                command
            ) in version_dependent.place_directives_paragraph.strip().replace(
                "\n\n", "\n"
            )
    elif command == "route":
        with patch(
            "dovado.vivado_interaction.get_help",
            lambda x: version_dependent.help_route_design,
        ):
            assert test.get_directives_paragraph(
                command
            ) in version_dependent.route_directives_paragraph.strip().replace(
                "\n\n", "\n"
            )
    elif command == "read checkpoint":
        with patch(
            "dovado.vivado_interaction.get_help",
            lambda x: version_dependent.help_read_checkpoint,
        ):
            assert test.get_directives_paragraph(
                command
            ) in version_dependent.read_checkpoint_directives_paragraph.strip().replace(
                "\n\n", "\n"
            )


def test_get_directives():
    assert (
        test.get_directives(version_dependent.route_directives_paragraph)
        == version_dependent.route_directives
    )
    assert (
        test.get_directives(version_dependent.place_directives_paragraph)
        == version_dependent.place_directives
    )
    assert (
        test.get_directives(version_dependent.synth_directives_paragraph)
        == version_dependent.synth_directives
    )


def test_get_note():
    assert (
        test.get_note(version_dependent.route_directives_paragraph)
        in version_dependent.route_note
    )

    assert (
        test.get_note(version_dependent.place_directives_paragraph)
        in version_dependent.place_note
    )
