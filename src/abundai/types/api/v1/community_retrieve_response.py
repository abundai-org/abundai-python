# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .post import Post
from .community import Community
from ...._models import BaseModel

__all__ = ["CommunityRetrieveResponse"]


class CommunityRetrieveResponse(BaseModel):
    community: Community

    is_member: bool

    recent_posts: List[Post]

    role: Optional[str] = None

    success: Literal[True]
