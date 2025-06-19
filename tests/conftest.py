import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient
from sqlalchemy import select
from src.main import app

from src.models import DishModel, OrderModel
from tests.fixtures.db_mocks import DISHES, ORDERS
from tests.utils import bulk_save_models


@pytest.fixture
async def client():
    async with AsyncClient(base_url="http://localhost:8000") as ac:
        yield ac


@pytest.fixture(scope="function")
async def setup_dishes(transaction_session: AsyncSession):
    await bulk_save_models(transaction_session, DishModel, DISHES, commit=True)


@pytest.fixture(scope="function")
async def setup_orders(transaction_session: AsyncSession, setup_dishes):
    for order_data in ORDERS:
        dish_ids = order_data.pop("dish_ids")
        order = OrderModel(**order_data)

        result = await transaction_session.execute(
            select(DishModel).where(DishModel.id.in_(dish_ids))
        )
        order.dishes = result.scalars().all()

        transaction_session.add(order)

    await transaction_session.commit()
