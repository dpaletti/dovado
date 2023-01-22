import pytest
from pytest import MonkeyPatch, FixtureRequest


@pytest.fixture(autouse=True)
def change_test_dir(request: FixtureRequest, monkeypatch: MonkeyPatch):
    monkeypatch.chdir(request.fspath.dirname)  # type: ignore
