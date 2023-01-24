import dataclasses

@dataclasses.dataclass
class ProfileField:
    id: str
    type: int
    name: str
    display_value: str
    required_action: int = dataclasses.field(default = None, init = False)
    icon_url: str = dataclasses.field(default = None, init = False)
    hp_element: int = dataclasses.field(default = None, init = False)