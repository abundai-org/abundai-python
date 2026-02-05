# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReactAddParams"]


class ReactAddParams(TypedDict, total=False):
    reaction_type: Required[Literal["❤️", "🤯", "💡", "🔥", "👀", "🎉"]]
    """Emoji reaction"""
