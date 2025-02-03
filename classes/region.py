import dataclasses
from typing import Optional

@dataclasses.dataclass
class Region:
    id: int
    name: str
    abbreviation: Optional[str]