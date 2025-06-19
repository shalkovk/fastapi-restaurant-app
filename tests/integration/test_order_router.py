import pytest
from httpx import AsyncClient
from tests.fixtures.testing_cases import (
    TEST_ORDER_ROUTE_CREATE_PARAMS,
    TEST_ORDER_ROUTE_PATCH_STATUS_PARAMS,
)


class TestOrderRouter:

    @pytest.mark.parametrize("case", TEST_ORDER_ROUTE_CREATE_PARAMS)
    async def test_create_order(self, client: AsyncClient, case):
        response = await client.post(case.url, json=case.data)
        assert response.status_code == case.expected_status

        if case.expected_status == 201:
            for key in case.expected_data:
                assert response.json()[key] == case.expected_data[key]
        else:
            assert response.json() == case.expected_data

    @pytest.mark.parametrize("case", TEST_ORDER_ROUTE_PATCH_STATUS_PARAMS)
    async def test_patch_order_status(self, client: AsyncClient, case):
        response = await client.patch(case.url, json=case.data)
        assert response.status_code == case.expected_status

        if case.expected_status == 200:
            for key in case.expected_data:
                assert response.json()[key] == case.expected_data[key]
        else:
            assert response.json() == case.expected_data
