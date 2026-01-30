from perf_parser.models import ResourceContext, ResolvedPair
from perf_parser.utils.constants import SCHED_MIGRATE_VALUE_UNSET
from typing import Iterable, Tuple

def _decode_raw_value(value: int) -> Tuple[int, int]:
    return ((value >> 16) & 0xFFFF, value & 0xFFFF)

def resolve_sched_group_migrate(ctx: ResourceContext) -> Iterable[ResolvedPair]:
    up, down = _decode_raw_value(ctx.raw_value)
    return [
        (ctx.node.replace("%s", "sched_group_upmigrate"), str(up)),
        (ctx.node.replace("%s", "sched_group_downmigrate"), str(down)),
    ]


def _migrate_value_string(first: bool, value: int) -> str:
    return f"{value} {SCHED_MIGRATE_VALUE_UNSET}" if first else f"{SCHED_MIGRATE_VALUE_UNSET} {value}"

def resolve_sched_migrate(ctx: ResourceContext) -> Iterable[ResolvedPair]:
    up, down = _decode_raw_value(ctx.raw_value)
    first = ctx.cluster <= 1
    return [
        (ctx.node.replace("%s", "sched_upmigrate"), _migrate_value_string(first, up)),
        (ctx.node .replace("%s", "sched_downmigrate"), _migrate_value_string(first, up)),
    ]
