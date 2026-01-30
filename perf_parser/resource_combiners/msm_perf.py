from perf_parser.models import ResourceContext
from typing import Iterable


def combine_msm_perf(values: Iterable[str], path: str) -> str:
    return ' '.join(v for v in values)
