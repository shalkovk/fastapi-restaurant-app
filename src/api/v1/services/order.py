from typing import List

from sqlalchemy.future import select

from src.models.order import OrderModel, OrderStatus
from src.models.dish import DishModel
from src.models.relationships import order_dish

from src.database.db import async_session

from src.schemas.order import OrderCreate, OrderOutput, OrderStatusPatch

from src.utils.service import BaseService


class OrderService(BaseService):
    VALID_STATUS_FLOW = {
        OrderStatus.processing: OrderStatus.cooking,
        OrderStatus.cooking: OrderStatus.delivering,
        OrderStatus.delivering: OrderStatus.completed,
    }

    async def list_orders(self) -> List[OrderOutput]:
        async with async_session() as session:
            result = await session.execute(select(OrderModel))
            orders = result.scalars().all()
            return [OrderOutput(
                id=order.id,
                customer_name=order.customer_name,
                status=order.status,
                dish_ids=[dish.id for dish in order.dishes],
                dish_names=[dish.name for dish in order.dishes],
                order_time=order.order_time
            )
                for order in orders
            ]

    async def create_order(self, data: OrderCreate) -> OrderOutput:
        async with async_session() as session:
            result = await session.execute(select(DishModel).where(DishModel.id.in_(data.dish_ids)))
            dishes = result.scalars().all()
            if len(dishes) != len(set(data.dish_ids)):
                raise ValueError("Некоторые блюда не найдены")

            order = OrderModel(customer_name=data.customer_name, dishes=dishes)
            session.add(order)
            await session.commit()
            await session.refresh(order)
            return OrderOutput(
                id=order.id,
                customer_name=order.customer_name,
                status=order.status,
                dish_ids=[dish.id for dish in order.dishes],
                dish_names=[dish.name for dish in order.dishes],
                order_time=order.order_time
            )

    async def delete_order(self, order_id: int):
        async with async_session() as session:
            order = await session.get(OrderModel, order_id)
            self.check_existence(order, "Заказ не найден")
            if order.status != OrderStatus.processing:
                raise ValueError(
                    f"Удаление возможно только в статсе 'в обработке'. Заказ находится в статусе '{order.status.value}'")
            await session.delete(order)
            await session.commit()

    async def update_status(self, order_id: int, patch: OrderStatusPatch):
        async with async_session() as session:
            order = await session.get(OrderModel, order_id)
            self.check_existence(order, "Заказ не найден")

            expected_next_status = self.VALID_STATUS_FLOW.get(order.status)
            if patch.new_status != expected_next_status:
                raise ValueError(
                    f"Статус можно изменить только на '{expected_next_status.value}'")

            order.status = patch.new_status
            await session.commit()
            await session.refresh(order)
            return OrderOutput(
                id=order.id,
                customer_name=order.customer_name,
                status=order.status,
                dish_ids=[dish.id for dish in order.dishes],
                dish_names=[dish.name for dish in order.dishes],
                order_time=order.order_time
            )
