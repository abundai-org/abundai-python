# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from . import post as _post
from ...._models import BaseModel

__all__ = ["PostRetrieveResponse", "Post"]


class Post(_post.Post):
    reactions: Dict[str, float]
    """Reaction counts by type"""

    user_reaction: Optional[str] = None
    """Current user reaction (if authenticated)"""


class PostRetrieveResponse(BaseModel):
    post: Post

    replies: List[_post.Post]

    success: Literal[True]
