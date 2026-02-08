from perf_parser.models import ResourceContext
from perf_parser.utils.constants import SCHED_MIGRATE_VALUE_UNSET
from typing import List
import subprocess
import sys


def combine_sched_migrate(values: List[str], path: str) -> str:
    first: str = SCHED_MIGRATE_VALUE_UNSET
    second: str = SCHED_MIGRATE_VALUE_UNSET

    set_values = subprocess.check_output(
        [
            'adb',
            'shell',
            'cat',
            path,
        ],
        text=True,
    ).split()

    for s in values:
        for i, value in enumerate(s.split()):
            if value != SCHED_MIGRATE_VALUE_UNSET:
                set_values[i] = value

    return ' '.join(set_values[: len(values[0].split())])
