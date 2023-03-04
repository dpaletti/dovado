import os
from pathlib import Path
from dovado_rtl.parsers.scala.scala_parsed import ScalaParsed

from dovado_rtl.parsers.scala.scala_parser import ScalaParser


def test_rocket_top_parsing():
    path_prexif: str = "../" + os.curdir + "/resources"
    to_parse = Path(path_prexif + "/rocket-chip/src/main/scala/tile/RocketTile.scala")
    parser = ScalaParser()
    parsed: ScalaParsed = parser.parse(Path(to_parse))
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
        == Path(path_prexif + "/replaced_rocket_tile.scala").read_text()
    )
