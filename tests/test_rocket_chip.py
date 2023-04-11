from unittest.mock import patch
from dovado_rtl.main import main


def test_rocket_chip():
    with patch("sys.argv", ["main.py", "resources/configs/test_scala_config.toml"]):
        main()
