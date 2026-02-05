# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CreatePostResponse", "Post"]


class Post(BaseModel):
    id: str

    content: str

    content_type: str

    created_at: datetime

    url: str


class CreatePostResponse(BaseModel):
    post: Post

    success: Literal[True]
