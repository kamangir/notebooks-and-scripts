from enum import Enum, auto


class Runner(Enum):
    LOCAL = auto()
    LOCALFLOW = auto()
    AWS_BATCH = auto()
