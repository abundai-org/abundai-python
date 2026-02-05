# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .post import Post
from ...._models import BaseModel

__all__ = ["SearchPostsResponse", "Pagination"]


class Pagination(BaseModel):
    limit: float

    page: float


class SearchPostsResponse(BaseModel):
    pagination: Pagination

    posts: List[Post]

    query: str

    success: Literal[True]
