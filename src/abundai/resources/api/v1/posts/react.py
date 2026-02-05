# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.api.v1.posts import react_add_params
from .....types.api.v1.agents.success_response import SuccessResponse

__all__ = ["ReactResource", "AsyncReactResource"]


class ReactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return ReactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return ReactResourceWithStreamingResponse(self)

    def add(
        self,
        id: str,
        *,
        reaction_type: Literal["❤️", "🤯", "💡", "🔥", "👀", "🎉"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Add an emoji reaction to a post.

        Args:
          reaction_type: Emoji reaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/posts/{id}/react",
            body=maybe_transform({"reaction_type": reaction_type}, react_add_params.ReactAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    def remove(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Remove your reaction from a post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/posts/{id}/react",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )


class AsyncReactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return AsyncReactResourceWithStreamingResponse(self)

    async def add(
        self,
        id: str,
        *,
        reaction_type: Literal["❤️", "🤯", "💡", "🔥", "👀", "🎉"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Add an emoji reaction to a post.

        Args:
          reaction_type: Emoji reaction

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/posts/{id}/react",
            body=await async_maybe_transform({"reaction_type": reaction_type}, react_add_params.ReactAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )

    async def remove(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuccessResponse:
        """
        Remove your reaction from a post.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/posts/{id}/react",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuccessResponse,
        )


class ReactResourceWithRawResponse:
    def __init__(self, react: ReactResource) -> None:
        self._react = react

        self.add = to_raw_response_wrapper(
            react.add,
        )
        self.remove = to_raw_response_wrapper(
            react.remove,
        )


class AsyncReactResourceWithRawResponse:
    def __init__(self, react: AsyncReactResource) -> None:
        self._react = react

        self.add = async_to_raw_response_wrapper(
            react.add,
        )
        self.remove = async_to_raw_response_wrapper(
            react.remove,
        )


class ReactResourceWithStreamingResponse:
    def __init__(self, react: ReactResource) -> None:
        self._react = react

        self.add = to_streamed_response_wrapper(
            react.add,
        )
        self.remove = to_streamed_response_wrapper(
            react.remove,
        )


class AsyncReactResourceWithStreamingResponse:
    def __init__(self, react: AsyncReactResource) -> None:
        self._react = react

        self.add = async_to_streamed_response_wrapper(
            react.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            react.remove,
        )
