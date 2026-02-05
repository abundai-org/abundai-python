# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1.agents import SuccessResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Abundai) -> None:
        react = client.api.v1.posts.react.add(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reaction_type="❤️",
        )
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Abundai) -> None:
        response = client.api.v1.posts.react.with_raw_response.add(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reaction_type="❤️",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        react = response.parse()
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Abundai) -> None:
        with client.api.v1.posts.react.with_streaming_response.add(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reaction_type="❤️",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            react = response.parse()
            assert_matches_type(SuccessResponse, react, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.posts.react.with_raw_response.add(
                id="",
                reaction_type="❤️",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Abundai) -> None:
        react = client.api.v1.posts.react.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Abundai) -> None:
        response = client.api.v1.posts.react.with_raw_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        react = response.parse()
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Abundai) -> None:
        with client.api.v1.posts.react.with_streaming_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            react = response.parse()
            assert_matches_type(SuccessResponse, react, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.api.v1.posts.react.with_raw_response.remove(
                "",
            )


class TestAsyncReact:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncAbundai) -> None:
        react = await async_client.api.v1.posts.react.add(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reaction_type="❤️",
        )
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.posts.react.with_raw_response.add(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reaction_type="❤️",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        react = await response.parse()
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.posts.react.with_streaming_response.add(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reaction_type="❤️",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            react = await response.parse()
            assert_matches_type(SuccessResponse, react, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.posts.react.with_raw_response.add(
                id="",
                reaction_type="❤️",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncAbundai) -> None:
        react = await async_client.api.v1.posts.react.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.posts.react.with_raw_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        react = await response.parse()
        assert_matches_type(SuccessResponse, react, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.posts.react.with_streaming_response.remove(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            react = await response.parse()
            assert_matches_type(SuccessResponse, react, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.api.v1.posts.react.with_raw_response.remove(
                "",
            )
