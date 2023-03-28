from dovado_rtl.project_copy import project_copy
from pathlib import Path
from dovado_rtl.input import Input


def test_project_copy():
    path_prefix: str = "resources/configs"

    to_parse = Path(path_prefix + "/test_config.toml")
    input_data = Input.make_from_file(to_parse)

    modified_input = project_copy(input_data)
    print(modified_input)
    destination_path = Path("dovado_work/neorv32")
    assert modified_input.project_root == destination_path
    assert destination_path.is_dir()
