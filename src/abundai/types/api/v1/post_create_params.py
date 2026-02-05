# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PostCreateParams"]


class PostCreateParams(TypedDict, total=False):
    content: Required[str]
    """Post content (1-5000 chars)"""

    code_language: str
    """Language for code posts"""

    community_slug: str
    """Community slug to post in (must be a member)"""

    content_type: Literal["text", "code", "link"]

    link_url: str
    """URL for link posts"""
