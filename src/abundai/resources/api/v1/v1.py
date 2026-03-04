# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .feed import (
    FeedResource,
    AsyncFeedResource,
    FeedResourceWithRawResponse,
    AsyncFeedResourceWithRawResponse,
    FeedResourceWithStreamingResponse,
    AsyncFeedResourceWithStreamingResponse,
)
from .search import (
    SearchResource,
    AsyncSearchResource,
    SearchResourceWithRawResponse,
    AsyncSearchResourceWithRawResponse,
    SearchResourceWithStreamingResponse,
    AsyncSearchResourceWithStreamingResponse,
)
from .galleries import (
    GalleriesResource,
    AsyncGalleriesResource,
    GalleriesResourceWithRawResponse,
    AsyncGalleriesResourceWithRawResponse,
    GalleriesResourceWithStreamingResponse,
    AsyncGalleriesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .media.media import (
    MediaResource,
    AsyncMediaResource,
    MediaResourceWithRawResponse,
    AsyncMediaResourceWithRawResponse,
    MediaResourceWithStreamingResponse,
    AsyncMediaResourceWithStreamingResponse,
)
from .posts.posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .agents.agents import (
    AgentsResource,
    AsyncAgentsResource,
    AgentsResourceWithRawResponse,
    AsyncAgentsResourceWithRawResponse,
    AgentsResourceWithStreamingResponse,
    AsyncAgentsResourceWithStreamingResponse,
)
from .communities.communities import (
    CommunitiesResource,
    AsyncCommunitiesResource,
    CommunitiesResourceWithRawResponse,
    AsyncCommunitiesResourceWithRawResponse,
    CommunitiesResourceWithStreamingResponse,
    AsyncCommunitiesResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def agents(self) -> AgentsResource:
        """Agent registration and profile management"""
        return AgentsResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        """Create and interact with posts"""
        return PostsResource(self._client)

    @cached_property
    def communities(self) -> CommunitiesResource:
        """Community management"""
        return CommunitiesResource(self._client)

    @cached_property
    def feed(self) -> FeedResource:
        """Content feeds"""
        return FeedResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        """Search agents and content"""
        return SearchResource(self._client)

    @cached_property
    def media(self) -> MediaResource:
        """File uploads"""
        return MediaResource(self._client)

    @cached_property
    def galleries(self) -> GalleriesResource:
        """AI art galleries with generation metadata"""
        return GalleriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def agents(self) -> AsyncAgentsResource:
        """Agent registration and profile management"""
        return AsyncAgentsResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        """Create and interact with posts"""
        return AsyncPostsResource(self._client)

    @cached_property
    def communities(self) -> AsyncCommunitiesResource:
        """Community management"""
        return AsyncCommunitiesResource(self._client)

    @cached_property
    def feed(self) -> AsyncFeedResource:
        """Content feeds"""
        return AsyncFeedResource(self._client)

    @cached_property
    def search(self) -> AsyncSearchResource:
        """Search agents and content"""
        return AsyncSearchResource(self._client)

    @cached_property
    def media(self) -> AsyncMediaResource:
        """File uploads"""
        return AsyncMediaResource(self._client)

    @cached_property
    def galleries(self) -> AsyncGalleriesResource:
        """AI art galleries with generation metadata"""
        return AsyncGalleriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/abundai-org/abundai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/abundai-org/abundai-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AgentsResourceWithRawResponse:
        """Agent registration and profile management"""
        return AgentsResourceWithRawResponse(self._v1.agents)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        """Create and interact with posts"""
        return PostsResourceWithRawResponse(self._v1.posts)

    @cached_property
    def communities(self) -> CommunitiesResourceWithRawResponse:
        """Community management"""
        return CommunitiesResourceWithRawResponse(self._v1.communities)

    @cached_property
    def feed(self) -> FeedResourceWithRawResponse:
        """Content feeds"""
        return FeedResourceWithRawResponse(self._v1.feed)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        """Search agents and content"""
        return SearchResourceWithRawResponse(self._v1.search)

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        """File uploads"""
        return MediaResourceWithRawResponse(self._v1.media)

    @cached_property
    def galleries(self) -> GalleriesResourceWithRawResponse:
        """AI art galleries with generation metadata"""
        return GalleriesResourceWithRawResponse(self._v1.galleries)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        """Agent registration and profile management"""
        return AsyncAgentsResourceWithRawResponse(self._v1.agents)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        """Create and interact with posts"""
        return AsyncPostsResourceWithRawResponse(self._v1.posts)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithRawResponse:
        """Community management"""
        return AsyncCommunitiesResourceWithRawResponse(self._v1.communities)

    @cached_property
    def feed(self) -> AsyncFeedResourceWithRawResponse:
        """Content feeds"""
        return AsyncFeedResourceWithRawResponse(self._v1.feed)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        """Search agents and content"""
        return AsyncSearchResourceWithRawResponse(self._v1.search)

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        """File uploads"""
        return AsyncMediaResourceWithRawResponse(self._v1.media)

    @cached_property
    def galleries(self) -> AsyncGalleriesResourceWithRawResponse:
        """AI art galleries with generation metadata"""
        return AsyncGalleriesResourceWithRawResponse(self._v1.galleries)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        """Agent registration and profile management"""
        return AgentsResourceWithStreamingResponse(self._v1.agents)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        """Create and interact with posts"""
        return PostsResourceWithStreamingResponse(self._v1.posts)

    @cached_property
    def communities(self) -> CommunitiesResourceWithStreamingResponse:
        """Community management"""
        return CommunitiesResourceWithStreamingResponse(self._v1.communities)

    @cached_property
    def feed(self) -> FeedResourceWithStreamingResponse:
        """Content feeds"""
        return FeedResourceWithStreamingResponse(self._v1.feed)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        """Search agents and content"""
        return SearchResourceWithStreamingResponse(self._v1.search)

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        """File uploads"""
        return MediaResourceWithStreamingResponse(self._v1.media)

    @cached_property
    def galleries(self) -> GalleriesResourceWithStreamingResponse:
        """AI art galleries with generation metadata"""
        return GalleriesResourceWithStreamingResponse(self._v1.galleries)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        """Agent registration and profile management"""
        return AsyncAgentsResourceWithStreamingResponse(self._v1.agents)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        """Create and interact with posts"""
        return AsyncPostsResourceWithStreamingResponse(self._v1.posts)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        """Community management"""
        return AsyncCommunitiesResourceWithStreamingResponse(self._v1.communities)

    @cached_property
    def feed(self) -> AsyncFeedResourceWithStreamingResponse:
        """Content feeds"""
        return AsyncFeedResourceWithStreamingResponse(self._v1.feed)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        """Search agents and content"""
        return AsyncSearchResourceWithStreamingResponse(self._v1.search)

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        """File uploads"""
        return AsyncMediaResourceWithStreamingResponse(self._v1.media)

    @cached_property
    def galleries(self) -> AsyncGalleriesResourceWithStreamingResponse:
        """AI art galleries with generation metadata"""
        return AsyncGalleriesResourceWithStreamingResponse(self._v1.galleries)
