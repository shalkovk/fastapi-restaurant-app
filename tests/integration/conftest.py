import pytest
from httpx import AsyncClient
from src.main import app


@pytest.fixture
async def client():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        yield ac
