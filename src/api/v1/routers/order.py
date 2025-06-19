from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from src.api.v1.services.order import OrderService
from src.schemas.order import OrderOutput, OrderStatusPatch, OrderCreate


router = APIRouter(
    prefix="/api/v1/orders",
    tags=["Orders 🧾"]
)


@router.get("/", response_model=List[OrderOutput])
async def get_all_orders(service: OrderService = Depends()):
    return await service.list_orders()


@router.post("/", response_model=OrderOutput, status_code=status.HTTP_201_CREATED)
async def create_orders(order: OrderCreate, service: OrderService = Depends()):
    try:
        return await service.create_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_orders(id: int, service: OrderService = Depends()):
    try:
        await service.delete_order(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/{id}/status", response_model=OrderOutput)
async def patch_status_orders(id: int, status_patch: OrderStatusPatch, service: OrderService = Depends()):
    try:
        return await service.update_status(id, status_patch)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
