from typing import Optional


class Targettable:
    def __init__(self) -> None:
        self._target: Optional[str] = None

    @property
    def target(self) -> Optional[str]:
        return self._target

    @target.setter
    def target(self, target_module: Optional[str]) -> None:
        self._target = target_module
