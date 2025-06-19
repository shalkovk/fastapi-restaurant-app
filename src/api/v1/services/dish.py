from typing import List
from src.schemas.dish import DishCreate, DishOutput
from src.models.dish import DishModel
from src.database.db import async_session
from sqlalchemy.future import select
from src.utils.constants import DISH_NOT_FOUND
from src.utils.service import BaseService


class DishService(BaseService):
    async def list_dishes(self) -> List[DishOutput]:
        async with async_session() as session:
            result = await session.execute(select(DishModel))
            return [DishOutput.model_validate(row, from_attributes=True) for row in result.scalars().all()]

    async def create_dish(self, dish_data: DishCreate) -> DishOutput:
        async with async_session() as session:
            dish = DishModel(**dish_data.model_dump())
            session.add(dish)
            await session.commit()
            await session.refresh(dish)
            return DishOutput.model_validate(dish, from_attributes=True)

    async def delete_dish(self, dish_id: int):
        async with async_session() as session:
            dish = await session.get(DishModel, dish_id)
            self.check_existence(dish, DISH_NOT_FOUND)
            await session.delete(dish)
            await session.commit()
