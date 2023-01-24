import dataclasses

@dataclasses.dataclass
class ProfileSummary:
    primary_text: str = dataclasses.field(default = None, init = False)
    secondary_text: str = dataclasses.field(default = None, init = False)