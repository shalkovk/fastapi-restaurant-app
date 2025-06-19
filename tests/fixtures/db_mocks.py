from datetime import datetime

DISHES = [
    {"id": 1, "name": "Плов", "price": 1200.0,
        "description": "Узбекский плов", "category": "Основное"},
    {"id": 2, "name": "Манты", "price": 1500.0,
        "description": "Казахские манты", "category": "Основное"},
    {"id": 3, "name": "Лагман", "price": 1100.0,
        "description": "Среднеазиатская лапша", "category": "Основное"},
    {"id": 4, "name": "Шашлык", "price": 1800.0,
        "description": "Мясо на углях", "category": "Гриль"},
    {"id": 5, "name": "Салат Цезарь", "price": 1000.0,
        "description": "Классический салат", "category": "Салаты"},
    {"id": 6, "name": "Бешбармак", "price": 1700.0,
        "description": "Традиционное блюдо", "category": "Основное"},
    {"id": 7, "name": "Компот", "price": 500.0,
        "description": "Домашний напиток", "category": "Напитки"},
    {"id": 8, "name": "Суп из лосося", "price": 2500.0,
        "description": "Рыбный суп", "category": "Супы"},
]

ORDERS = [
    {
        "id": 1,
        "customer_name": "Олег",
        "status": "в обработке",
        "dish_ids": [1],
        "order_time": datetime.utcnow(),
    },
    {
        "id": 2,
        "customer_name": "Иван",
        "status": "готовится",
        "dish_ids": [1, 2],
        "order_time": datetime.utcnow(),
    },
    {
        "id": 3,
        "customer_name": "Евгений",
        "status": "доставляется",
        "dish_ids": [3, 4],
        "order_time": datetime.utcnow(),
    },
    {
        "id": 4,
        "customer_name": "Артур",
        "status": "завершен",
        "dish_ids": [5],
        "order_time": datetime.utcnow(),
    },
    {
        "id": 5,
        "customer_name": "Смол",
        "status": "готовится",
        "dish_ids": [6, 7],
        "order_time": datetime.utcnow(),
    },
    {
        "id": 6,
        "customer_name": "Дмитрий",
        "status": "в обработке",
        "dish_ids": [8],
        "order_time": datetime.utcnow(),
    },
]
