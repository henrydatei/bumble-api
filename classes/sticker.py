import dataclasses

@dataclasses.dataclass
class Sticker:
    foo: str  = dataclasses.field(default = "bar", init = False)