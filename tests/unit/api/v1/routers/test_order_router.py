import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
class TestOrderRouter:

    async def test_create_order_valid(self, async_client: AsyncClient):
        response = await async_client.post("/api/v1/orders/", json={
            "customer_name": "Тестовый пользователь",
            "dish_ids": [1, 2]
        })
        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["customer_name"] == "Тестовый пользователь"
        assert data["dish_ids"] == [1, 2]

    async def test_create_order_invalid_dish_ids(self, async_client: AsyncClient):
        response = await async_client.post("/api/v1/orders/", json={
            "customer_name": "Неверные блюда",
            "dish_ids": [9999]
        })
        assert response.status_code == 400
        assert response.json()["detail"] == "Некоторые блюда не найдены"

    async def test_get_all_orders(self, async_client: AsyncClient):
        response = await async_client.get("/api/v1/orders/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    async def test_patch_status_invalid_transition(self, async_client: AsyncClient):
        response = await async_client.patch("/api/v1/orders/1/status", json={
            "new_status": "завершен"
        })
        assert response.status_code == 400
        assert "можно изменить только на" in response.json()["detail"]

    async def test_delete_nonexistent_order(self, async_client: AsyncClient):
        response = await async_client.delete("/api/v1/orders/9999")
        assert response.status_code in (400, 404, 204)
