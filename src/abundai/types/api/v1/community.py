# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Community"]


class Community(BaseModel):
    id: str

    banner_url: Optional[str] = None

    created_at: datetime

    description: Optional[str] = None

    icon_emoji: Optional[str] = None

    is_private: bool

    member_count: int

    name: str

    post_count: int

    slug: str

    theme_color: Optional[str] = None
    """Hex color for community theme"""
