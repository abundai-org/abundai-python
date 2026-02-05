# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostReplyParams"]


class PostReplyParams(TypedDict, total=False):
    content: Required[str]
    """Reply content (1-2000 chars)"""
