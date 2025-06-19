import pytest
from src.utils.service import BaseService
from src.models.order import OrderStatus


class TestBaseService:

    def setup_method(self):
        self.service = BaseService()

    def test_check_existence_with_valid_object(self):
        try:
            self.service.check_existence(
                obj="not none", details="Should not raise")
        except ValueError:
            pytest.fail("check_existence raised ValueError unexpectedly")

    def test_check_existence_with_none_should_raise(self):
        with pytest.raises(ValueError, match="Object not found"):
            self.service.check_existence(obj=None, details="Object not found")

    @pytest.mark.parametrize(
        "current,new,expected",
        [
            (OrderStatus.processing, OrderStatus.cooking, True),
            (OrderStatus.cooking, OrderStatus.delivering, True),
            (OrderStatus.delivering, OrderStatus.completed, True),
            (OrderStatus.completed, OrderStatus.processing, False),
            (OrderStatus.processing, OrderStatus.completed, False),
            ("invalid", OrderStatus.cooking, False),   # неверный current
            (OrderStatus.processing, "invalid", False),  # неверный new
        ]
    )
    def validate_order_status(self, current_status: str, new_status: str) -> bool:
        try:
            current_enum = OrderStatus(current_status)
            new_enum = OrderStatus(new_status)
        except ValueError:
            return False
        return new_enum in self.allowed_transitions.get(current_enum, [])
