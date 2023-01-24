import dataclasses

from .range import Range

@dataclasses.dataclass
class Country:
    id: int
    name: str
    phone_prefix: str
    iso_code: str
    flag_symbol: str
    phone_length: Range