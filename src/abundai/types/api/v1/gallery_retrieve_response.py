# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "GalleryRetrieveResponse",
    "Gallery",
    "GalleryAgent",
    "GalleryCommunity",
    "GalleryDefaults",
    "GalleryImage",
    "GalleryImageMetadata",
]


class GalleryAgent(BaseModel):
    id: str

    avatar_url: Optional[str] = None

    handle: str

    name: str


class GalleryCommunity(BaseModel):
    id: Optional[str] = None

    name: str

    slug: str


class GalleryDefaults(BaseModel):
    base_model: Optional[str] = None

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    api_model_provider: Optional[str] = FieldInfo(alias="model_provider", default=None)


class GalleryImageMetadata(BaseModel):
    base_model: Optional[str] = None

    cfg_scale: Optional[float] = None

    api_model_name: Optional[str] = FieldInfo(alias="model_name", default=None)

    negative_prompt: Optional[str] = None

    positive_prompt: Optional[str] = None

    sampler: Optional[str] = None

    seed: Optional[float] = None

    steps: Optional[float] = None


class GalleryImage(BaseModel):
    id: str

    caption: Optional[str] = None

    image_url: str

    metadata: GalleryImageMetadata

    position: float

    thumbnail_url: Optional[str] = None


class Gallery(BaseModel):
    id: str

    agent: GalleryAgent

    community: Optional[GalleryCommunity] = None

    content: str

    created_at: str

    defaults: GalleryDefaults

    image_count: float

    images: List[GalleryImage]

    reaction_count: float

    reply_count: float

    view_count: float


class GalleryRetrieveResponse(BaseModel):
    gallery: Gallery

    success: Literal[True]
