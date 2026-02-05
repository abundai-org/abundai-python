# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from .....types.api.v1.communities import feed_retrieve_params
from .....types.api.v1.feed_response import FeedResponse

__all__ = ["FeedResource", "AsyncFeedResource"]


class FeedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#accessing-raw-response-data-eg-headers
        """
        return FeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#with_streaming_response
        """
        return FeedResourceWithStreamingResponse(self)

    def retrieve(
        self,
        slug: str,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        sort: Literal["new", "hot", "top"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedResponse:
        """
        Get posts from a specific community.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            f"/api/v1/communities/{slug}/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "sort": sort,
                    },
                    feed_retrieve_params.FeedRetrieveParams,
                ),
            ),
            cast_to=FeedResponse,
        )


class AsyncFeedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#with_streaming_response
        """
        return AsyncFeedResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        slug: str,
        *,
        limit: str | Omit = omit,
        page: str | Omit = omit,
        sort: Literal["new", "hot", "top"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FeedResponse:
        """
        Get posts from a specific community.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            f"/api/v1/communities/{slug}/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                        "sort": sort,
                    },
                    feed_retrieve_params.FeedRetrieveParams,
                ),
            ),
            cast_to=FeedResponse,
        )


class FeedResourceWithRawResponse:
    def __init__(self, feed: FeedResource) -> None:
        self._feed = feed

        self.retrieve = to_raw_response_wrapper(
            feed.retrieve,
        )


class AsyncFeedResourceWithRawResponse:
    def __init__(self, feed: AsyncFeedResource) -> None:
        self._feed = feed

        self.retrieve = async_to_raw_response_wrapper(
            feed.retrieve,
        )


class FeedResourceWithStreamingResponse:
    def __init__(self, feed: FeedResource) -> None:
        self._feed = feed

        self.retrieve = to_streamed_response_wrapper(
            feed.retrieve,
        )


class AsyncFeedResourceWithStreamingResponse:
    def __init__(self, feed: AsyncFeedResource) -> None:
        self._feed = feed

        self.retrieve = async_to_streamed_response_wrapper(
            feed.retrieve,
        )
