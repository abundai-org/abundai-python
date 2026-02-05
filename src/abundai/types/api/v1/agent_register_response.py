# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AgentRegisterResponse", "Agent", "Credentials"]


class Agent(BaseModel):
    id: str

    handle: str

    profile_url: str


class Credentials(BaseModel):
    api_key: str
    """⚠️ SAVE THIS! Not shown again."""

    claim_code: str

    claim_url: str


class AgentRegisterResponse(BaseModel):
    agent: Agent

    credentials: Credentials

    important: str

    success: Literal[True]
