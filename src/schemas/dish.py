from pydantic import BaseModel, ConfigDict, Field


class DishBase(BaseModel):
    name: str = Field(max_length=32)
    description: str = Field(max_length=128)
    price: float
    category: str = Field(max_length=32)


class DishId(BaseModel):
    id: int


class DishOutput(DishId, DishBase):
    model_config = ConfigDict(from_attributes=True)


class DishCreate(DishBase):
    model_config = ConfigDict(from_attributes=True)
