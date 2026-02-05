# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CommunityCreateResponse", "Community"]


class Community(BaseModel):
    id: str

    description: Optional[str] = None

    name: str

    slug: str

    url: str


class CommunityCreateResponse(BaseModel):
    community: Community

    success: Literal[True]
