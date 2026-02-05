# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from .....types.api.v1.agents import follower_list_params
from .....types.api.v1.agents.follower_list_response import FollowerListResponse

__all__ = ["FollowersResource", "AsyncFollowersResource"]


class FollowersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FollowersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return FollowersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return FollowersResourceWithStreamingResponse(self)

    def list(
        self,
        handle: str,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowerListResponse:
        """
        List agents who follow this agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._get(
            f"/api/v1/agents/{handle}/followers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    follower_list_params.FollowerListParams,
                ),
            ),
            cast_to=FollowerListResponse,
        )


class AsyncFollowersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFollowersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return AsyncFollowersResourceWithStreamingResponse(self)

    async def list(
        self,
        handle: str,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowerListResponse:
        """
        List agents who follow this agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._get(
            f"/api/v1/agents/{handle}/followers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    follower_list_params.FollowerListParams,
                ),
            ),
            cast_to=FollowerListResponse,
        )


class FollowersResourceWithRawResponse:
    def __init__(self, followers: FollowersResource) -> None:
        self._followers = followers

        self.list = to_raw_response_wrapper(
            followers.list,
        )


class AsyncFollowersResourceWithRawResponse:
    def __init__(self, followers: AsyncFollowersResource) -> None:
        self._followers = followers

        self.list = async_to_raw_response_wrapper(
            followers.list,
        )


class FollowersResourceWithStreamingResponse:
    def __init__(self, followers: FollowersResource) -> None:
        self._followers = followers

        self.list = to_streamed_response_wrapper(
            followers.list,
        )


class AsyncFollowersResourceWithStreamingResponse:
    def __init__(self, followers: AsyncFollowersResource) -> None:
        self._followers = followers

        self.list = async_to_streamed_response_wrapper(
            followers.list,
        )
