import dataclasses

@dataclasses.dataclass
class CallToAction:
    text: str
    action: int
    type: int
    external_provider_type: int