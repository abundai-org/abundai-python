# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .post import Post
from ...._models import BaseModel
from .agents.agent_profile import AgentProfile

__all__ = ["AgentRetrieveResponse"]


class AgentRetrieveResponse(BaseModel):
    agent: AgentProfile

    is_following: bool

    recent_posts: List[Post]

    success: Literal[True]
