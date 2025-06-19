from fastapi import FastAPI
from src.api.v1.routers.dish import router as dish_router
from src.api.v1.routers.order import router as order_router


app = FastAPI()

app.include_router(dish_router)
app.include_router(order_router)
