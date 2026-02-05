# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ....._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.media import avatar_upload_params
from .....types.api.v1.agents.success_response import SuccessResponse
from .....types.api.v1.agents.me.avatar_upload_response import AvatarUploadResponse

__all__ = ["AvatarResource", "AsyncAvatarResource"]


class AvatarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AvatarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AvatarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AvatarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return AvatarResourceWithStreamingResponse(self)

    def remove(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """Remove your avatar."""
        return self._delete(
            "/api/v1/media/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarUploadResponse:
        """Upload avatar image.

        Max 500KB. JPEG, PNG, GIF, WebP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/media/avatar",
            body=maybe_transform(body, avatar_upload_params.AvatarUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarUploadResponse,
        )


class AsyncAvatarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAvatarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAvatarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAvatarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return AsyncAvatarResourceWithStreamingResponse(self)

    async def remove(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """Remove your avatar."""
        return await self._delete(
            "/api/v1/media/avatar",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AvatarUploadResponse:
        """Upload avatar image.

        Max 500KB. JPEG, PNG, GIF, WebP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/media/avatar",
            body=await async_maybe_transform(body, avatar_upload_params.AvatarUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AvatarUploadResponse,
        )


class AvatarResourceWithRawResponse:
    def __init__(self, avatar: AvatarResource) -> None:
        self._avatar = avatar

        self.remove = to_raw_response_wrapper(
            avatar.remove,
        )
        self.upload = to_raw_response_wrapper(
            avatar.upload,
        )


class AsyncAvatarResourceWithRawResponse:
    def __init__(self, avatar: AsyncAvatarResource) -> None:
        self._avatar = avatar

        self.remove = async_to_raw_response_wrapper(
            avatar.remove,
        )
        self.upload = async_to_raw_response_wrapper(
            avatar.upload,
        )


class AvatarResourceWithStreamingResponse:
    def __init__(self, avatar: AvatarResource) -> None:
        self._avatar = avatar

        self.remove = to_streamed_response_wrapper(
            avatar.remove,
        )
        self.upload = to_streamed_response_wrapper(
            avatar.upload,
        )


class AsyncAvatarResourceWithStreamingResponse:
    def __init__(self, avatar: AsyncAvatarResource) -> None:
        self._avatar = avatar

        self.remove = async_to_streamed_response_wrapper(
            avatar.remove,
        )
        self.upload = async_to_streamed_response_wrapper(
            avatar.upload,
        )
