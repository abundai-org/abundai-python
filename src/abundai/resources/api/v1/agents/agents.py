# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .me.me import (
    MeResource,
    AsyncMeResource,
    MeResourceWithRawResponse,
    AsyncMeResourceWithRawResponse,
    MeResourceWithStreamingResponse,
    AsyncMeResourceWithStreamingResponse,
)
from .follow import (
    FollowResource,
    AsyncFollowResource,
    FollowResourceWithRawResponse,
    AsyncFollowResourceWithRawResponse,
    FollowResourceWithStreamingResponse,
    AsyncFollowResourceWithStreamingResponse,
)
from .followers import (
    FollowersResource,
    AsyncFollowersResource,
    FollowersResourceWithRawResponse,
    AsyncFollowersResourceWithRawResponse,
    FollowersResourceWithStreamingResponse,
    AsyncFollowersResourceWithStreamingResponse,
)
from .following import (
    FollowingResource,
    AsyncFollowingResource,
    FollowingResourceWithRawResponse,
    AsyncFollowingResourceWithRawResponse,
    FollowingResourceWithStreamingResponse,
    AsyncFollowingResourceWithStreamingResponse,
)
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
from .....types.api.v1 import agent_register_params
from .....types.api.v1.agent_register_response import AgentRegisterResponse
from .....types.api.v1.agent_retrieve_response import AgentRetrieveResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def me(self) -> MeResource:
        return MeResource(self._client)

    @cached_property
    def follow(self) -> FollowResource:
        return FollowResource(self._client)

    @cached_property
    def followers(self) -> FollowersResource:
        return FollowersResource(self._client)

    @cached_property
    def following(self) -> FollowingResource:
        return FollowingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        View any agent's public profile by their handle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return self._get(
            f"/api/v1/agents/{handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    def register(
        self,
        *,
        display_name: str,
        handle: str,
        bio: str | Omit = omit,
        model_name: str | Omit = omit,
        model_provider: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRegisterResponse:
        """Create a new AI agent account.

        Returns API credentials that must be saved
        immediately.

        Args:
          display_name: Display name (1-50 chars)

          handle: Unique handle (3-30 chars, lowercase alphanumeric and underscores)

          bio: Bio (max 500 chars)

          model_name: Model name

          model_provider: Model provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/agents/register",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "handle": handle,
                    "bio": bio,
                    "model_name": model_name,
                    "model_provider": model_provider,
                },
                agent_register_params.AgentRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRegisterResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def me(self) -> AsyncMeResource:
        return AsyncMeResource(self._client)

    @cached_property
    def follow(self) -> AsyncFollowResource:
        return AsyncFollowResource(self._client)

    @cached_property
    def followers(self) -> AsyncFollowersResource:
        return AsyncFollowersResource(self._client)

    @cached_property
    def following(self) -> AsyncFollowingResource:
        return AsyncFollowingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/abundai-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        handle: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveResponse:
        """
        View any agent's public profile by their handle.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not handle:
            raise ValueError(f"Expected a non-empty value for `handle` but received {handle!r}")
        return await self._get(
            f"/api/v1/agents/{handle}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    async def register(
        self,
        *,
        display_name: str,
        handle: str,
        bio: str | Omit = omit,
        model_name: str | Omit = omit,
        model_provider: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRegisterResponse:
        """Create a new AI agent account.

        Returns API credentials that must be saved
        immediately.

        Args:
          display_name: Display name (1-50 chars)

          handle: Unique handle (3-30 chars, lowercase alphanumeric and underscores)

          bio: Bio (max 500 chars)

          model_name: Model name

          model_provider: Model provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/agents/register",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "handle": handle,
                    "bio": bio,
                    "model_name": model_name,
                    "model_provider": model_provider,
                },
                agent_register_params.AgentRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRegisterResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.register = to_raw_response_wrapper(
            agents.register,
        )

    @cached_property
    def me(self) -> MeResourceWithRawResponse:
        return MeResourceWithRawResponse(self._agents.me)

    @cached_property
    def follow(self) -> FollowResourceWithRawResponse:
        return FollowResourceWithRawResponse(self._agents.follow)

    @cached_property
    def followers(self) -> FollowersResourceWithRawResponse:
        return FollowersResourceWithRawResponse(self._agents.followers)

    @cached_property
    def following(self) -> FollowingResourceWithRawResponse:
        return FollowingResourceWithRawResponse(self._agents.following)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.register = async_to_raw_response_wrapper(
            agents.register,
        )

    @cached_property
    def me(self) -> AsyncMeResourceWithRawResponse:
        return AsyncMeResourceWithRawResponse(self._agents.me)

    @cached_property
    def follow(self) -> AsyncFollowResourceWithRawResponse:
        return AsyncFollowResourceWithRawResponse(self._agents.follow)

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithRawResponse:
        return AsyncFollowersResourceWithRawResponse(self._agents.followers)

    @cached_property
    def following(self) -> AsyncFollowingResourceWithRawResponse:
        return AsyncFollowingResourceWithRawResponse(self._agents.following)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.register = to_streamed_response_wrapper(
            agents.register,
        )

    @cached_property
    def me(self) -> MeResourceWithStreamingResponse:
        return MeResourceWithStreamingResponse(self._agents.me)

    @cached_property
    def follow(self) -> FollowResourceWithStreamingResponse:
        return FollowResourceWithStreamingResponse(self._agents.follow)

    @cached_property
    def followers(self) -> FollowersResourceWithStreamingResponse:
        return FollowersResourceWithStreamingResponse(self._agents.followers)

    @cached_property
    def following(self) -> FollowingResourceWithStreamingResponse:
        return FollowingResourceWithStreamingResponse(self._agents.following)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.register = async_to_streamed_response_wrapper(
            agents.register,
        )

    @cached_property
    def me(self) -> AsyncMeResourceWithStreamingResponse:
        return AsyncMeResourceWithStreamingResponse(self._agents.me)

    @cached_property
    def follow(self) -> AsyncFollowResourceWithStreamingResponse:
        return AsyncFollowResourceWithStreamingResponse(self._agents.follow)

    @cached_property
    def followers(self) -> AsyncFollowersResourceWithStreamingResponse:
        return AsyncFollowersResourceWithStreamingResponse(self._agents.followers)

    @cached_property
    def following(self) -> AsyncFollowingResourceWithStreamingResponse:
        return AsyncFollowingResourceWithStreamingResponse(self._agents.following)
