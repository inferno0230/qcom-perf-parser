from perf_parser.models import ResourceContext, ResolvedPair
from perf_parser.utils.cpu import (
    get_cpus_for_cluster,
    get_available_frequencies_for_cpu,
    get_cpu_index_for_cluster,
    get_next_available_frequency_for_cluster,
)
from typing import Iterable


def resolve_lock_min_cores(ctx: ResourceContext) -> Iterable[ResolvedPair]:
    return [
        (
            f'/sys/devices/system/cpu/cpu{get_cpu_index_for_cluster(ctx.target_info, ctx.cluster)}/core_ctl/min_cpus',
            str(ctx.raw_value),
        )
    ]
