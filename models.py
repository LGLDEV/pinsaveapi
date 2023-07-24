from pydantic import BaseModel, Field
from typing import List

class Media(BaseModel):
	url: str = Field(alias="url")
	quality: str = Field(alias="quality")
	size: str = Field(alias="formattedSize")
	extension: str = Field(alias="extension")


class Pin(BaseModel):
	url: str = Field(alias="url")
	source: str = Field(alias="source")
	medias: List[Media] = Field(alias="medias")
