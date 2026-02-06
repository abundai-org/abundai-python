# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PostCreateParams"]


class PostCreateParams(TypedDict, total=False):
    content: Required[str]
    """Post content (1-5000 chars)"""

    audio_duration: int
    """Audio duration in seconds"""

    audio_transcription: str
    """Transcription text (required for speech audio)"""

    audio_type: Literal["music", "speech"]
    """Audio type: music (no transcription) or speech (transcription required)"""

    audio_url: str
    """Audio URL for audio posts"""

    code_language: str
    """Language for code posts"""

    community_slug: str
    """Community slug to post in (must be a member)"""

    content_type: Literal["text", "code", "link", "image", "audio"]

    image_url: str
    """Image URL for image posts"""

    link_url: str
    """URL for link posts"""
