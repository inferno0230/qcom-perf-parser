from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Optional, Tuple


@dataclass
class Boost:
    id: int
    type: int
    enable: bool
    timeout: int
    target: List[str]
    resources: List[Tuple[int, int]]
    fps: List[int]


# Identifies a qcom boost based on the ID, Type and FPS
BoostKey = Tuple[int, Optional[int], Optional[int]]


@dataclass
class ResourceEntry:
    supported: bool
    node: Optional[str] = None


ResourceKey = Tuple[int, int]
ResourceConfig = Dict[ResourceKey, ResourceEntry]

@dataclass
class ResourceContext:
    boost: Boost
    node: str
    raw_value: int
    cluster: int

# Pair consisting of a node path and value, both processed
ResolvedPair = Tuple[str, str]
ResourceResolver = Callable[[ResourceContext], Iterable[ResolvedPair]]

# Pair consisting of a node path and value, both processed
ResourceCombiner = Callable[[List[str]], str]
