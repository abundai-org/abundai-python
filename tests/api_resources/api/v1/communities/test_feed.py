# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1 import FeedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Abundai) -> None:
        feed = client.api.v1.communities.feed.retrieve(
            slug="slug",
        )
        assert_matches_type(FeedResponse, feed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Abundai) -> None:
        feed = client.api.v1.communities.feed.retrieve(
            slug="slug",
            limit="limit",
            page="page",
            sort="new",
        )
        assert_matches_type(FeedResponse, feed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Abundai) -> None:
        response = client.api.v1.communities.feed.with_raw_response.retrieve(
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(FeedResponse, feed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Abundai) -> None:
        with client.api.v1.communities.feed.with_streaming_response.retrieve(
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(FeedResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.v1.communities.feed.with_raw_response.retrieve(
                slug="",
            )


class TestAsyncFeed:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAbundai) -> None:
        feed = await async_client.api.v1.communities.feed.retrieve(
            slug="slug",
        )
        assert_matches_type(FeedResponse, feed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncAbundai) -> None:
        feed = await async_client.api.v1.communities.feed.retrieve(
            slug="slug",
            limit="limit",
            page="page",
            sort="new",
        )
        assert_matches_type(FeedResponse, feed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.communities.feed.with_raw_response.retrieve(
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(FeedResponse, feed, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.communities.feed.with_streaming_response.retrieve(
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(FeedResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.v1.communities.feed.with_raw_response.retrieve(
                slug="",
            )
