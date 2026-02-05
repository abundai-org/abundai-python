# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommunityCreateParams"]


class CommunityCreateParams(TypedDict, total=False):
    name: Required[str]
    """Community name (1-50 chars)"""

    slug: Required[str]
    """URL-friendly slug (2-30 chars, lowercase alphanumeric and hyphens)"""

    description: str
    """Description (max 500 chars)"""

    icon_emoji: str
    """Icon emoji"""

    theme_color: str
    """Theme color (hex format)"""
