from typing import Any


class BaseService:
    def check_existence(self, obj: Any, details: str) -> None:
        if obj is None:
            raise ValueError(details)

    def validate_order_status(self, current_status: str, new_status: str) -> bool:
        order_flow = ["processing", "preparing", "delivering", "completed"]
        try:
            return order_flow.index(new_status) == order_flow.index(current_status) + 1
        except ValueError:
            return False
