from perf_parser.models import ResourceContext, ResolvedPair
from perf_parser.utils.gpu import get_next_available_frequency
from typing import Iterable


def resolve_next_gpu_freq(ctx: ResourceContext) -> Iterable[ResolvedPair]:
    return [(ctx.node, str(get_next_available_frequency(1000000 * ctx.raw_value)))]
