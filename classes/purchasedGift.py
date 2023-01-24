import dataclasses

@dataclasses.dataclass
class PurchasedGift:
    foo: str  = dataclasses.field(default = "bar", init = False)