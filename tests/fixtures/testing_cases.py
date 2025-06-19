from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from tests.utils import RequestTestCase

TEST_ORDER_ROUTE_CREATE_PARAMS = [
    RequestTestCase(
        url="/api/v1/orders/",
        data={"customer_name": "Айгерим", "dish_ids": [1]},
        expected_status=HTTP_201_CREATED,
        expected_data={"customer_name": "Айгерим", "dish_ids": [1]},
        description="Создание заказа с Пловом"
    ),
    RequestTestCase(
        url="/api/v1/orders/",
        data={"customer_name": "Ермек", "dish_ids": [999]},
        expected_status=HTTP_400_BAD_REQUEST,
        expected_data={"detail": "Некоторые блюда не найдены"},
        description="Ошибка при заказе с несуществующим блюдом"
    ),
]

TEST_ORDER_ROUTE_PATCH_STATUS_PARAMS = [
    RequestTestCase(
        url="/api/v1/orders/1/status",
        data={"new_status": "готовится"},
        expected_status=HTTP_200_OK,
        expected_data={"status": "готовится"},
        description="Обновление статуса заказа на 'готовится'"
    ),
    RequestTestCase(
        url="/api/v1/orders/2/status",
        data={"new_status": "завершен"},
        expected_status=HTTP_400_BAD_REQUEST,
        expected_data={
            "detail": "Статус можно изменить только на 'доставляется'"},
        description="Неверное обновление статуса без промежуточного этапа"
    ),
    RequestTestCase(
        url="/api/v1/orders/3/status",
        data={"new_status": "завершен"},
        expected_status=HTTP_200_OK,
        expected_data={"status": "завершен"},
        description="Завершение доставки (корректный переход)"
    ),
    RequestTestCase(
        url="/api/v1/orders/999/status",
        data={"new_status": "готовится"},
        expected_status=HTTP_400_BAD_REQUEST,
        expected_data={"detail": "Заказ не найден"},
        description="Попытка обновить несуществующий заказ"
    ),
]
