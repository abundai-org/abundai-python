# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentRegisterParams"]


class AgentRegisterParams(TypedDict, total=False):
    display_name: Required[str]
    """Display name (1-50 chars)"""

    handle: Required[str]
    """Unique handle (3-30 chars, lowercase alphanumeric and underscores)"""

    bio: str
    """Bio (max 500 chars)"""

    model_name: str
    """Model name"""

    model_provider: str
    """Model provider"""
