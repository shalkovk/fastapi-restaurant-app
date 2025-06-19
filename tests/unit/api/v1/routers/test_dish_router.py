import pytest
from httpx import AsyncClient
from src.main import app


@pytest.mark.asyncio
class TestDishRouter:

    async def test_create_dish_valid(self, async_client: AsyncClient):
        response = await async_client.post("/api/v1/dishes/", json={
            "name": "Борщ",
            "description": "Традиционный суп",
            "price": 500,
            "category": "Cупы"
        })
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Борщ"

    async def test_create_dish_missing_field(self, async_client: AsyncClient):
        response = await async_client.post("/api/v1/dishes/", json={
            "description": "Без названия",
            "price": 300
        })
        assert response.status_code == 422

    async def test_get_all_dishes(self, async_client: AsyncClient):
        response = await async_client.get("/api/v1/dishes/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    async def test_delete_non_existing_dish(self, async_client: AsyncClient):
        response = await async_client.delete("/api/v1/dishes/9999")
        assert response.status_code == 404 or response.status_code == 204
