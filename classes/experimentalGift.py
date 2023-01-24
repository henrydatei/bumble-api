import dataclasses

@dataclasses.dataclass
class ExperimentalGift:
    foo: str  = dataclasses.field(default = "bar", init = False)