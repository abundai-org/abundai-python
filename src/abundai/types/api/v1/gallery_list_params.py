# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GalleryListParams"]


class GalleryListParams(TypedDict, total=False):
    limit: str

    page: str

    sort: Literal["new", "hot", "top"]
