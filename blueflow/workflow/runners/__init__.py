from typing import List
from enum import Enum, auto


class RunnerType(Enum):
    GENERIC = auto()
    LOCAL = auto()
    AWS_BATCH = auto()


def list_of_runners() -> List[str]:
    return sorted([runner_type.name.lower() for runner_type in RunnerType])
