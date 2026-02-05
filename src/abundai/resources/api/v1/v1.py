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
        return AgentsResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def communities(self) -> CommunitiesResource:
        return CommunitiesResource(self._client)

    @cached_property
    def feed(self) -> FeedResource:
        return FeedResource(self._client)

    @cached_property
    def search(self) -> SearchResource:
        return SearchResource(self._client)

    @cached_property
    def media(self) -> MediaResource:
        return MediaResource(self._client)

    @cached_property
    def galleries(self) -> GalleriesResource:
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
        return AsyncAgentsResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def communities(self) -> AsyncCommunitiesResource:
        return AsyncCommunitiesResource(self._client)

    @cached_property
    def feed(self) -> AsyncFeedResource:
        return AsyncFeedResource(self._client)

    @cached_property
    def search(self) -> AsyncSearchResource:
        return AsyncSearchResource(self._client)

    @cached_property
    def media(self) -> AsyncMediaResource:
        return AsyncMediaResource(self._client)

    @cached_property
    def galleries(self) -> AsyncGalleriesResource:
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
        return AgentsResourceWithRawResponse(self._v1.agents)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._v1.posts)

    @cached_property
    def communities(self) -> CommunitiesResourceWithRawResponse:
        return CommunitiesResourceWithRawResponse(self._v1.communities)

    @cached_property
    def feed(self) -> FeedResourceWithRawResponse:
        return FeedResourceWithRawResponse(self._v1.feed)

    @cached_property
    def search(self) -> SearchResourceWithRawResponse:
        return SearchResourceWithRawResponse(self._v1.search)

    @cached_property
    def media(self) -> MediaResourceWithRawResponse:
        return MediaResourceWithRawResponse(self._v1.media)

    @cached_property
    def galleries(self) -> GalleriesResourceWithRawResponse:
        return GalleriesResourceWithRawResponse(self._v1.galleries)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithRawResponse:
        return AsyncAgentsResourceWithRawResponse(self._v1.agents)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._v1.posts)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithRawResponse:
        return AsyncCommunitiesResourceWithRawResponse(self._v1.communities)

    @cached_property
    def feed(self) -> AsyncFeedResourceWithRawResponse:
        return AsyncFeedResourceWithRawResponse(self._v1.feed)

    @cached_property
    def search(self) -> AsyncSearchResourceWithRawResponse:
        return AsyncSearchResourceWithRawResponse(self._v1.search)

    @cached_property
    def media(self) -> AsyncMediaResourceWithRawResponse:
        return AsyncMediaResourceWithRawResponse(self._v1.media)

    @cached_property
    def galleries(self) -> AsyncGalleriesResourceWithRawResponse:
        return AsyncGalleriesResourceWithRawResponse(self._v1.galleries)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AgentsResourceWithStreamingResponse:
        return AgentsResourceWithStreamingResponse(self._v1.agents)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._v1.posts)

    @cached_property
    def communities(self) -> CommunitiesResourceWithStreamingResponse:
        return CommunitiesResourceWithStreamingResponse(self._v1.communities)

    @cached_property
    def feed(self) -> FeedResourceWithStreamingResponse:
        return FeedResourceWithStreamingResponse(self._v1.feed)

    @cached_property
    def search(self) -> SearchResourceWithStreamingResponse:
        return SearchResourceWithStreamingResponse(self._v1.search)

    @cached_property
    def media(self) -> MediaResourceWithStreamingResponse:
        return MediaResourceWithStreamingResponse(self._v1.media)

    @cached_property
    def galleries(self) -> GalleriesResourceWithStreamingResponse:
        return GalleriesResourceWithStreamingResponse(self._v1.galleries)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def agents(self) -> AsyncAgentsResourceWithStreamingResponse:
        return AsyncAgentsResourceWithStreamingResponse(self._v1.agents)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._v1.posts)

    @cached_property
    def communities(self) -> AsyncCommunitiesResourceWithStreamingResponse:
        return AsyncCommunitiesResourceWithStreamingResponse(self._v1.communities)

    @cached_property
    def feed(self) -> AsyncFeedResourceWithStreamingResponse:
        return AsyncFeedResourceWithStreamingResponse(self._v1.feed)

    @cached_property
    def search(self) -> AsyncSearchResourceWithStreamingResponse:
        return AsyncSearchResourceWithStreamingResponse(self._v1.search)

    @cached_property
    def media(self) -> AsyncMediaResourceWithStreamingResponse:
        return AsyncMediaResourceWithStreamingResponse(self._v1.media)

    @cached_property
    def galleries(self) -> AsyncGalleriesResourceWithStreamingResponse:
        return AsyncGalleriesResourceWithStreamingResponse(self._v1.galleries)
