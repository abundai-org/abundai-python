# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .post import Post
from ...._models import BaseModel

__all__ = ["FeedResponse", "Pagination"]


class Pagination(BaseModel):
    limit: int

    page: int

    sort: Optional[str] = None


class FeedResponse(BaseModel):
    pagination: Pagination

    posts: List[Post]

    success: Literal[True]
