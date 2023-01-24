import dataclasses

@dataclasses.dataclass
class VerificationAccessObject:
    foo: str  = dataclasses.field(default = "bar", init = False)