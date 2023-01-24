import dataclasses

@dataclasses.dataclass
class ApplicationFeature:
    feature: int
    enabled: bool