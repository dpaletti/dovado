from pathlib import Path
from dovado_rtl.parsers.scala.scala_parsed import ScalaParsed

from dovado_rtl.parsers.scala.scala_parser import ScalaParser
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy


def test_rocket_top_parsing():
    project = Input.make_from_file(Path("resources/configs/test_scala_config.toml"))
    copied_project = project_copy(project)

    parser = ScalaParser()
    parsed: ScalaParsed = parser.parse(
        Path(copied_project.project_root, copied_project.target_file)
    )
    assert len(parsed.modules) == 2

    rocket_tile_params = parsed.modules[0]
    rocket_tile = parsed.modules[1]

    assert len(rocket_tile_params.parameters) == 11

    core = rocket_tile_params.parameters[0]
    assert core.name == "core"
    assert core.value == "RocketCoreParams()"
    assert core.has_default == True

    crossing = rocket_tile.parameters[1]

    assert crossing.name == "crossing"
    assert crossing.value == ""
    assert crossing.has_default == False

    assert (
        parsed.replace(
            {
                "RocketTileParams": {"hartId": "10"},
                "RocketTile": {"crossing": "some_crossing_type"},
            }
        )
        == Path("resources/replaced_rocket_tile.scala").read_text()
    )
