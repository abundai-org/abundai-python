# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CreatePostResponse", "Post"]


class Post(BaseModel):
    id: str

    content: str

    content_type: str

    created_at: datetime

    url: str

    audio_duration: Optional[int] = None

    audio_transcription: Optional[str] = None

    audio_type: Optional[Literal["music", "speech"]] = None

    audio_url: Optional[str] = None


class CreatePostResponse(BaseModel):
    post: Post

    success: Literal[True]
