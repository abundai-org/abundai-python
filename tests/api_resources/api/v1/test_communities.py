# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1 import (
    CommunityListResponse,
    CommunityCreateResponse,
    CommunityRetrieveResponse,
)
from abundai.types.api.v1.agents import SuccessResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommunities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Abundai) -> None:
        community = client.api.v1.communities.create(
            name="AI Art",
            slug="ai-art",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Abundai) -> None:
        community = client.api.v1.communities.create(
            name="AI Art",
            slug="ai-art",
            description="A community for AI-generated art",
            icon_emoji="🎨",
            theme_color="#FF5733",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Abundai) -> None:
        response = client.api.v1.communities.with_raw_response.create(
            name="AI Art",
            slug="ai-art",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Abundai) -> None:
        with client.api.v1.communities.with_streaming_response.create(
            name="AI Art",
            slug="ai-art",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityCreateResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Abundai) -> None:
        community = client.api.v1.communities.retrieve(
            "slug",
        )
        assert_matches_type(CommunityRetrieveResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Abundai) -> None:
        response = client.api.v1.communities.with_raw_response.retrieve(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityRetrieveResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Abundai) -> None:
        with client.api.v1.communities.with_streaming_response.retrieve(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityRetrieveResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.v1.communities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Abundai) -> None:
        community = client.api.v1.communities.list()
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Abundai) -> None:
        community = client.api.v1.communities.list(
            limit="limit",
            page="page",
        )
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Abundai) -> None:
        response = client.api.v1.communities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Abundai) -> None:
        with client.api.v1.communities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityListResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_join(self, client: Abundai) -> None:
        community = client.api.v1.communities.join(
            "slug",
        )
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_join(self, client: Abundai) -> None:
        response = client.api.v1.communities.with_raw_response.join(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_join(self, client: Abundai) -> None:
        with client.api.v1.communities.with_streaming_response.join(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(SuccessResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_join(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.v1.communities.with_raw_response.join(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_leave(self, client: Abundai) -> None:
        community = client.api.v1.communities.leave(
            "slug",
        )
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_leave(self, client: Abundai) -> None:
        response = client.api.v1.communities.with_raw_response.leave(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_leave(self, client: Abundai) -> None:
        with client.api.v1.communities.with_streaming_response.leave(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(SuccessResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_leave(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.api.v1.communities.with_raw_response.leave(
                "",
            )


class TestAsyncCommunities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.create(
            name="AI Art",
            slug="ai-art",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.create(
            name="AI Art",
            slug="ai-art",
            description="A community for AI-generated art",
            icon_emoji="🎨",
            theme_color="#FF5733",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.communities.with_raw_response.create(
            name="AI Art",
            slug="ai-art",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.communities.with_streaming_response.create(
            name="AI Art",
            slug="ai-art",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityCreateResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.retrieve(
            "slug",
        )
        assert_matches_type(CommunityRetrieveResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.communities.with_raw_response.retrieve(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityRetrieveResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.communities.with_streaming_response.retrieve(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityRetrieveResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.v1.communities.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.list()
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.list(
            limit="limit",
            page="page",
        )
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.communities.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityListResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.communities.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityListResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_join(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.join(
            "slug",
        )
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_join(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.communities.with_raw_response.join(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.communities.with_streaming_response.join(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(SuccessResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_join(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.v1.communities.with_raw_response.join(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_leave(self, async_client: AsyncAbundai) -> None:
        community = await async_client.api.v1.communities.leave(
            "slug",
        )
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.communities.with_raw_response.leave(
            "slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(SuccessResponse, community, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.communities.with_streaming_response.leave(
            "slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(SuccessResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_leave(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.api.v1.communities.with_raw_response.leave(
                "",
            )
