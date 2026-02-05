# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1.agents import SuccessResponse
from abundai.types.api.v1.agents.me import AvatarUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvatar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: Abundai) -> None:
        avatar = client.api.v1.media.avatar.remove()
        assert_matches_type(SuccessResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Abundai) -> None:
        response = client.api.v1.media.avatar.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(SuccessResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Abundai) -> None:
        with client.api.v1.media.avatar.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(SuccessResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: Abundai) -> None:
        avatar = client.api.v1.media.avatar.upload()
        assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Abundai) -> None:
        avatar = client.api.v1.media.avatar.upload(
            file=b"raw file contents",
        )
        assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Abundai) -> None:
        response = client.api.v1.media.avatar.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = response.parse()
        assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Abundai) -> None:
        with client.api.v1.media.avatar.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = response.parse()
            assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAvatar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncAbundai) -> None:
        avatar = await async_client.api.v1.media.avatar.remove()
        assert_matches_type(SuccessResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.media.avatar.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(SuccessResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.media.avatar.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(SuccessResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncAbundai) -> None:
        avatar = await async_client.api.v1.media.avatar.upload()
        assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncAbundai) -> None:
        avatar = await async_client.api.v1.media.avatar.upload(
            file=b"raw file contents",
        )
        assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.media.avatar.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        avatar = await response.parse()
        assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.media.avatar.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            avatar = await response.parse()
            assert_matches_type(AvatarUploadResponse, avatar, path=["response"])

        assert cast(Any, response.is_closed) is True
