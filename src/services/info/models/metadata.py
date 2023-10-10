from typing import List, Optional

from pydantic import BaseModel, HttpUrl, validator


class Metadata(BaseModel):
    short_summary: str
    links_worth_examinging_further: Optional[List[HttpUrl]] = None
    site_favicon_image_url: Optional[HttpUrl] = None

    # @validator("*")
    # def check_fields(cls, value):
    #     # ... your validation logic here ...
    #     return value
