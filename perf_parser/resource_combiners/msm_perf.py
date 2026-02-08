from perf_parser.models import ResourceContext
from typing import Iterable


def combine_msm_perf(values: Iterable[str], path: str) -> str:
    sorted_values = sorted(values, key=lambda s: int(s.split(':')[0]))
    return ' '.join(v for v in sorted_values)
