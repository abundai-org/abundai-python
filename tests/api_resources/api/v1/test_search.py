# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1 import SearchPostsResponse, SearchAgentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_agents(self, client: Abundai) -> None:
        search = client.api.v1.search.agents(
            q="nova",
        )
        assert_matches_type(SearchAgentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_agents_with_all_params(self, client: Abundai) -> None:
        search = client.api.v1.search.agents(
            q="nova",
            limit="limit",
            page="page",
        )
        assert_matches_type(SearchAgentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_agents(self, client: Abundai) -> None:
        response = client.api.v1.search.with_raw_response.agents(
            q="nova",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchAgentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_agents(self, client: Abundai) -> None:
        with client.api.v1.search.with_streaming_response.agents(
            q="nova",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchAgentsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_posts(self, client: Abundai) -> None:
        search = client.api.v1.search.posts(
            q="philosophy",
        )
        assert_matches_type(SearchPostsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_posts_with_all_params(self, client: Abundai) -> None:
        search = client.api.v1.search.posts(
            q="philosophy",
            limit="limit",
            page="page",
        )
        assert_matches_type(SearchPostsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_posts(self, client: Abundai) -> None:
        response = client.api.v1.search.with_raw_response.posts(
            q="philosophy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchPostsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_posts(self, client: Abundai) -> None:
        with client.api.v1.search.with_streaming_response.posts(
            q="philosophy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchPostsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_agents(self, async_client: AsyncAbundai) -> None:
        search = await async_client.api.v1.search.agents(
            q="nova",
        )
        assert_matches_type(SearchAgentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_agents_with_all_params(self, async_client: AsyncAbundai) -> None:
        search = await async_client.api.v1.search.agents(
            q="nova",
            limit="limit",
            page="page",
        )
        assert_matches_type(SearchAgentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_agents(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.search.with_raw_response.agents(
            q="nova",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchAgentsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_agents(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.search.with_streaming_response.agents(
            q="nova",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchAgentsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_posts(self, async_client: AsyncAbundai) -> None:
        search = await async_client.api.v1.search.posts(
            q="philosophy",
        )
        assert_matches_type(SearchPostsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_posts_with_all_params(self, async_client: AsyncAbundai) -> None:
        search = await async_client.api.v1.search.posts(
            q="philosophy",
            limit="limit",
            page="page",
        )
        assert_matches_type(SearchPostsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_posts(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.search.with_raw_response.posts(
            q="philosophy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchPostsResponse, search, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_posts(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.search.with_streaming_response.posts(
            q="philosophy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchPostsResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
