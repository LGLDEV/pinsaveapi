from pydantic import BaseModel, Field
from typing import List

class Media(BaseModel):
    url: str = Field(alias="url")
    quality: str = Field(alias="quality")
    formatted_size: str = Field(alias="formattedSize")
    extension: str = Field(alias="extension")


class Pin(BaseModel):
    pin_url: str = Field(alias="url")
    thumbnail: str = Field(alias="thumbnail")
    medias: str = Field(alias="medias")
    source: str = Field(alias="source")