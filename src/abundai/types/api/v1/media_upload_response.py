# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["MediaUploadResponse"]


class MediaUploadResponse(BaseModel):
    image_id: str

    image_url: str

    message: str

    success: Literal[True]
