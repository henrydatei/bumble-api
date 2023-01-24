import dataclasses

@dataclasses.dataclass
class City:
    id: int
    name: str
    context_info: str