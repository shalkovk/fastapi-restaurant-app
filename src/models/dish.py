from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Mapped, relationship

from src.models.base import BaseModel
from src.models.relationships import order_dish


if TYPE_CHECKING:
    from src.models.order import OrderModel


class DishModel(BaseModel):
    __tablename__ = "dish"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String(32), index=True, nullable=False)
    description: Mapped[str | None] = Column(String(128))
    price: Mapped[float] = Column(Float, nullable=False)
    category: Mapped[str] = Column(String(32), index=True)

    orders: Mapped[list["OrderModel"]] = relationship(
        "OrderModel",
        secondary=order_dish,
        back_populates="dishes",
        lazy="selectin"
    )
