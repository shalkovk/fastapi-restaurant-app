from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import Mapped, relationship
import enum
from datetime import datetime

from src.models.base import BaseModel
from src.models.relationships import order_dish

if TYPE_CHECKING:
    from src.models.dish import DishModel


class OrderStatus(str, enum.Enum):
    processing = "в обработке"
    cooking = "готовится"
    delivering = "доставляется"
    completed = "завершен"


class OrderModel(BaseModel):
    __tablename__ = "order"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    customer_name: Mapped[str] = Column(String(32), nullable=False)
    order_time: Mapped[str] = Column(
        DateTime(timezone=True), default=lambda: datetime.utcnow())
    status: Mapped[OrderStatus] = Column(
        Enum(OrderStatus), default=OrderStatus.processing)

    dishes: Mapped[list["DishModel"]] = relationship(
        "DishModel",
        secondary=order_dish,
        back_populates="orders",
        lazy="selectin"
    )
