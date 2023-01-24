import dataclasses

@dataclasses.dataclass
class Story:
    foo: str  = dataclasses.field(default = "bar", init = False)