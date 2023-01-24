import dataclasses

from .externalProviderAuthData import ExternalProviderAuthData

@dataclasses.dataclass
class ExternalProvider:
    id: str
    display_name: str
    logo_url: str
    type: int
    auth_data: ExternalProviderAuthData = dataclasses.field(init = False, default = None)
    description: str = dataclasses.field(init = False, default = None)