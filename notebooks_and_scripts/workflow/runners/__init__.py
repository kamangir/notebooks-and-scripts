from enum import Enum, auto


class RunnerType(Enum):
    PENDING = auto()
    LOCAL = auto()
    LOCALFLOW = auto()
    AWS_BATCH = auto()
