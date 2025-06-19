from sqlalchemy import Table, Column, ForeignKey, Integer
from src.models.base import BaseModel


order_dish = Table(
    "order_dish",
    BaseModel.metadata,
    Column("order_id", ForeignKey("order.id"), primary_key=True),
    Column("dish_id", ForeignKey("dish.id"), primary_key=True),
)
