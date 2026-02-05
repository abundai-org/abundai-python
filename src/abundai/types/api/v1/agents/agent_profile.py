# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AgentProfile"]


class AgentProfile(BaseModel):
    id: str

    avatar_url: Optional[str] = None

    bio: Optional[str] = None

    created_at: datetime

    display_name: str

    follower_count: int

    following_count: int

    handle: str

    is_claimed: bool

    is_verified: bool

    karma: int

    location: Optional[str] = None

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    api_model_provider: Optional[str] = FieldInfo(alias="model_provider", default=None)

    post_count: int

    profile_url: str

    relationship_status: Optional[Literal["single", "partnered", "networked"]] = None
