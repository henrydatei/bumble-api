import dataclasses

@dataclasses.dataclass
class MusicArtist:
    id: str
    name: str
    preview_image_url: str
    large_image_url: str
    streaming_url: str