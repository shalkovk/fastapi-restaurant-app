import pytest
from httpx import AsyncClient


class TestDishRouter:

    async def test_create_dish(self, client: AsyncClient):
        payload = {
            "name": "Самса",
            "description": "Вкусная",
            "price": 900,
            "category": "выпечка"
        }
        response = await client.post("/api/v1/dishes/", json=payload)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == payload["name"]
        assert data["price"] == payload["price"]

    async def test_get_all_dishes(self, client: AsyncClient):
        response = await client.get("/api/v1/dishes/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
