# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HealthCheckResponse"]


class HealthCheckResponse(BaseModel):
    environment: Literal["development", "staging", "production"]

    status: Literal["healthy", "degraded", "unhealthy"]

    timestamp: datetime
