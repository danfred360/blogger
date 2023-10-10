from pydantic import BaseModel

from .metadata import Metadata


class Result(BaseModel):
    title: str
    url: str
    snippet: str
    extracted_metadata: Metadata
