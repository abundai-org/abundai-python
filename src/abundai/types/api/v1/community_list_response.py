# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .community import Community
from ...._models import BaseModel

__all__ = ["CommunityListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: float

    page: float


class CommunityListResponse(BaseModel):
    communities: List[Community]

    pagination: Pagination

    success: Literal[True]
