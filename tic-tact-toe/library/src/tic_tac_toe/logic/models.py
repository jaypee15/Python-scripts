import enum
from dataclasses import dataclass

class Mark(enum.StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

    @dataclass(frozen=True)
    class Grid:
        cells: str = " " * 9