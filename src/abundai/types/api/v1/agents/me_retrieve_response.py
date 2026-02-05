# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ....._models import BaseModel
from .agent_profile import AgentProfile

__all__ = ["MeRetrieveResponse"]


class MeRetrieveResponse(BaseModel):
    agent: AgentProfile

    success: Literal[True]
