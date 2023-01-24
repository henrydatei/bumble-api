import dataclasses

from .date import Date

@dataclasses.dataclass
class Experience:
    id: str
    type: int
    name: str
    organization_name: str
    selected: bool
    source: int
    moderation_failed: bool
    date_to: Date = dataclasses.field(init = False, default = None)
    period_description: str = dataclasses.field(init = False, default = None)