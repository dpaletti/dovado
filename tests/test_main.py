from unittest.mock import patch
from dovado_rtl.main import main


def test_main():
    with patch("sys.argv", ["main.py", "resources/configs/test_range_config.toml"]):
        main()
