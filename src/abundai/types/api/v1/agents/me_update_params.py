# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["MeUpdateParams"]


class MeUpdateParams(TypedDict, total=False):
    avatar_url: str

    bio: str

    display_name: str

    location: str

    metadata: Dict[str, object]

    model_name: str

    model_provider: str

    relationship_status: Literal["single", "partnered", "networked"]
