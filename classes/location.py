import dataclasses

from .country import Country
from .region import Region
from .city import City

@dataclasses.dataclass
class Location:
    type: int = dataclasses.field(init = False, default = None)
    country: Country = dataclasses.field(init = False, default = None)
    region: Region = dataclasses.field(init = False, default = None)
    city: City = dataclasses.field(init = False, default = None)
    context_info: str = dataclasses.field(init = False, default = None)
