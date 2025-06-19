from fastapi import APIRouter, Depends, HTTPException, status
from src.api.v1.services.dish import DishService
from src.schemas.dish import DishOutput, DishCreate


router = APIRouter(
    prefix="/api/v1/dishes",
    tags=["Dishes 🍲"]
)


@router.get("/")
async def get_all_dishes(service: DishService = Depends()):
    return await service.list_dishes()


@router.post("/", response_model=DishOutput, status_code=status.HTTP_201_CREATED)
async def create_dishes(dish: DishCreate, service: DishService = Depends()):
    return await service.create_dish(dish)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dishes(id: int, service: DishService = Depends()):
    try:
        await service.delete_dish(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
