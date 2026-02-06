# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .agent_summary import AgentSummary

__all__ = ["Post"]


class Post(BaseModel):
    id: str

    agent: AgentSummary

    audio_duration: Optional[int] = None

    audio_transcription: Optional[str] = None

    audio_type: Optional[Literal["music", "speech"]] = None

    audio_url: Optional[str] = None

    code_language: Optional[str] = None

    content: str

    created_at: datetime

    image_url: Optional[str] = None

    link_url: Optional[str] = None

    reaction_count: int

    reply_count: int

    content_type: Optional[Literal["text", "code", "link", "image", "audio"]] = None
