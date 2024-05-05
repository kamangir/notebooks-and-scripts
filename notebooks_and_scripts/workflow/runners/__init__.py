from enum import Enum, auto


class RunnerType(Enum):
    GENERIC = auto()
    LOCAL = auto()
    LOCALFLOW = auto()
    AWS_BATCH = auto()
