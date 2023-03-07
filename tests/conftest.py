import pytest
from pathlib import Path


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(Path(request.config.rootdir, "tests"))
