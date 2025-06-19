import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from enum import Enum


class OrderBase(BaseModel):
    customer_name: str = Field(max_length=32)
    dish_ids: List[int] = Field(..., description="Список ID блюд")


class OrderStatus(str, Enum):
    processing = "в обработке"
    cooking = "готовится"
    delivering = "доставляется"
    completed = "завершен"


class OrderCreate(OrderBase):
    model_config = ConfigDict(from_attributes=True)


class OrderOutput(BaseModel):
    id: int
    customer_name: str
    status: OrderStatus
    dish_ids: List[int]
    dish_names: List[str]
    order_time: datetime.datetime

    model_config = ConfigDict(from_attributes=True)


class OrderStatusPatch(BaseModel):
    new_status: OrderStatus
