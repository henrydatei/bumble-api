import dataclasses

@dataclasses.dataclass
class ExternalProviderAuthData:
    type: int
    oauth_url: str