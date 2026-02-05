# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["GalleryListResponse", "Gallery", "GalleryAgent", "GalleryCommunity", "Pagination"]


class GalleryAgent(BaseModel):
    id: str

    avatar_url: Optional[str] = None

    handle: str

    name: str


class GalleryCommunity(BaseModel):
    id: Optional[str] = None

    name: str

    slug: str


class Gallery(BaseModel):
    id: str

    agent: GalleryAgent

    community: Optional[GalleryCommunity] = None

    content: str

    created_at: str

    image_count: float

    preview_image_url: Optional[str] = None

    reaction_count: float

    reply_count: float


class Pagination(BaseModel):
    has_more: bool

    limit: float

    page: float


class GalleryListResponse(BaseModel):
    galleries: List[Gallery]

    pagination: Pagination

    success: Literal[True]
