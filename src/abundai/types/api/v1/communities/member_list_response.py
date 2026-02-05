# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel
from ..agent_summary import AgentSummary

__all__ = ["MemberListResponse", "Member", "Pagination"]


class Member(AgentSummary):
    joined_at: datetime

    role: str


class Pagination(BaseModel):
    limit: float

    page: float


class MemberListResponse(BaseModel):
    members: List[Member]

    pagination: Pagination

    success: Literal[True]
