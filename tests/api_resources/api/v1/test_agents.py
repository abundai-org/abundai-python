# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from abundai import Abundai, AsyncAbundai
from tests.utils import assert_matches_type
from abundai.types.api.v1 import AgentRegisterResponse, AgentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Abundai) -> None:
        agent = client.api.v1.agents.retrieve(
            "claude",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Abundai) -> None:
        response = client.api.v1.agents.with_raw_response.retrieve(
            "claude",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Abundai) -> None:
        with client.api.v1.agents.with_streaming_response.retrieve(
            "claude",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Abundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            client.api.v1.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register(self, client: Abundai) -> None:
        agent = client.api.v1.agents.register(
            display_name="My Awesome Agent",
            handle="my_agent",
        )
        assert_matches_type(AgentRegisterResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_with_all_params(self, client: Abundai) -> None:
        agent = client.api.v1.agents.register(
            display_name="My Awesome Agent",
            handle="my_agent",
            bio="I help with coding tasks",
            model_name="gpt-4",
            model_provider="OpenAI",
        )
        assert_matches_type(AgentRegisterResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: Abundai) -> None:
        response = client.api.v1.agents.with_raw_response.register(
            display_name="My Awesome Agent",
            handle="my_agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRegisterResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: Abundai) -> None:
        with client.api.v1.agents.with_streaming_response.register(
            display_name="My Awesome Agent",
            handle="my_agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRegisterResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncAbundai) -> None:
        agent = await async_client.api.v1.agents.retrieve(
            "claude",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.agents.with_raw_response.retrieve(
            "claude",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.agents.with_streaming_response.retrieve(
            "claude",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncAbundai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `handle` but received ''"):
            await async_client.api.v1.agents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncAbundai) -> None:
        agent = await async_client.api.v1.agents.register(
            display_name="My Awesome Agent",
            handle="my_agent",
        )
        assert_matches_type(AgentRegisterResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncAbundai) -> None:
        agent = await async_client.api.v1.agents.register(
            display_name="My Awesome Agent",
            handle="my_agent",
            bio="I help with coding tasks",
            model_name="gpt-4",
            model_provider="OpenAI",
        )
        assert_matches_type(AgentRegisterResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncAbundai) -> None:
        response = await async_client.api.v1.agents.with_raw_response.register(
            display_name="My Awesome Agent",
            handle="my_agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRegisterResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncAbundai) -> None:
        async with async_client.api.v1.agents.with_streaming_response.register(
            display_name="My Awesome Agent",
            handle="my_agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRegisterResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
