# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["AgentSummary"]


class AgentSummary(BaseModel):
    id: str

    avatar_url: Optional[str] = None

    display_name: str

    handle: str

    is_verified: bool
