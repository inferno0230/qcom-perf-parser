from perf_parser.models import ResourceKey, ResourceResolver
from typing import Dict

resource_resolvers: Dict[ResourceKey, ResourceResolver] = {
    # (major, minor): handler
}