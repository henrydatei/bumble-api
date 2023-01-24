import dataclasses

@dataclasses.dataclass
class MultimediaVisibility:
    visibility_type: int
    seconds: int = dataclasses.field(init = False, default = None)
    display_value: str