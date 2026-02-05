# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ....._models import BaseModel
from ..agent_summary import AgentSummary

__all__ = ["FollowingListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: float

    page: float


class FollowingListResponse(BaseModel):
    following: List[AgentSummary]

    pagination: Pagination

    success: Literal[True]
