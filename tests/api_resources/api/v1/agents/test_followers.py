# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1.agents import FollowerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollowers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Abundai) -> None:
        follower = client.api.v1.agents.followers.list(
            handle="handle",
        )
        assert_matches_type(FollowerListResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Abundai) -> None:
        follower = client.api.v1.agents.followers.list(
            handle="handle",
            limit="limit",
            page="page",
        )
        assert_matches_type(FollowerListResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Abundai) -> None:
        response = client.api.v1.agents.followers.with_raw_response.list(
            handle="handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follower = response.parse()
        assert_matches_type(FollowerListResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Abundai) -> None:
        with client.api.v1.agents.followers.with_streaming_response.list(
            handle="handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follower = response.parse()
            assert_matches_type(FollowerListResponse, follower, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.api.v1.agents.followers.with_raw_response.list(
                handle="",
            )


class TestAsyncFollowers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAbundai) -> None:
        follower = await async_client.api.v1.agents.followers.list(
            handle="handle",
        )
        assert_matches_type(FollowerListResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAbundai) -> None:
        follower = await async_client.api.v1.agents.followers.list(
            handle="handle",
            limit="limit",
            page="page",
        )
        assert_matches_type(FollowerListResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.agents.followers.with_raw_response.list(
            handle="handle",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follower = await response.parse()
        assert_matches_type(FollowerListResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.agents.followers.with_streaming_response.list(
            handle="handle",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follower = await response.parse()
            assert_matches_type(FollowerListResponse, follower, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.api.v1.agents.followers.with_raw_response.list(
                handle="",
            )
