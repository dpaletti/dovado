from pathlib import Path
from dovado_rtl.parsers.cpp.cpp_parser import CppParser
from dovado_rtl.parsers.cpp.cpp_parsed import CppParsed
from dovado_rtl.input import Input
from dovado_rtl.project_copy import project_copy


def test_cpp_parsing():
    project = Input.make_from_file(Path("resources/configs/test_cpp_config.toml"))
    copied_project = project_copy(project)

    parser = CppParser()
    parsed: CppParsed = parser.parse(Path(copied_project.project_root, "common.h"))
    cpp_module = parsed.modules[0]
    assert cpp_module.name == ""

    image_width = cpp_module.parameters[0]
    assert image_width.name == "MAX_IMAGE_WIDTH"
    assert image_width.value == "1920"

    filter_h_size = cpp_module.parameters[3]
    assert filter_h_size.name == "FILTER_H_SIZE"
    assert filter_h_size.value == "15"

    assert (
        parsed.replace(
            {
                "": {"MAX_IMAGE_WIDTH": "480", "MAX_IMAGE_HEIGHT": "360"},
            }
        )
        == Path("resources/replaced_convolution.h").read_text()
    )
