# 🍽 FastAPI Restaurant App

Приложение для управления блюдами и заказами в ресторане. Поддерживает создание, получение, удаление блюд и заказов, а также обновление статуса заказов.

---

## 🚀 Быстрый старт

##### 1. 👨‍💻 Клонировать проект

```bash
git clone https://github.com/shalkovk/fastapi-restaurant-app.git
```

---

##### 2. 📁 Перейти в директорию с docker файлами

```bash
cd fastapi-restaurant-app/deploy
```

---

##### 3. ⚙️ Переменные окружения

В корневой директории создать файл `.env` и вставить переменные окружения:

```cmd
POSTGRES_DB=restaurant_app
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres-restaurant-db
POSTGRES_PORT=5432
```

---

##### 4. 🐳 Запуск через Docker Compose

Развернуть приложение в контейнерах docker. Убедитесь, что находитесь в директории `fastapi-restaurant-app/deploy`. В терминале выполните IDE:

```cmd
docker-compose up --build -d
```

---

##### 5. 🛠 Alembic — миграции

После установки docker образа и контейнеров, в терминале необходимо выполнить команды по очереди:

- `docker exec -it fastapi-restaurant-app bash`
- `alembic init alembic`
- `alembic revision --autogenerate -m 'init migrations'`
- `alembic upgrade head`

---

##### 6. 🌐 Открыть приложение

В адресной строке браузера обратиться по url:
`http://127.0.0.1:8000/docs`

---

### 📚 Endpoints API

#### 🍲 Блюда

- GET `/api/v1/dishes/` — получить список всех блюд

- POST `/api/v1/dishes/` — добавить блюдо

- DELETE `/api/v1/dishes/{id}` — удалить блюдо

#### 🧾 Заказы

- GET `/api/v1/orders/` — получить список всех заказов

- POST `/api/v1/orders/` — создать заказ

- PATCH `/api/v1/orders/{id}/status` — обновить статус заказа

- DELETE `/api/v1/orders/{id}` — удалить заказ

---

### 📁 Структура приложения

Ниже представлена структура приложения

```

├───alembic
│   └───versions
├───deploy
│   ├───docker-compose.yml
│   └───Dockerfile
├───src
│   ├───api
│   │   └───v1
│   │       ├───routers
│   │       │   ├───dish.py
│   │       │   └───order.py
│   │       └───services
│   │           ├───dish.py
│   │           └───order.py
│   ├───database
│   │   └───db.py
│   ├───models
│   │   ├───dish.py
│   │   ├───order.py
│   │   ├───base.py
│   │   └───relationships.py
│   ├───schemas
│   │   ├───dish.py
│   │   └───order.py
│   └───utils
│       ├───constants.py
│       └───service.py
│
└───tests
    ├───fixtures
    │   ├───db_mocks.py
    │   └───testing_cases.py
    ├───integration
    │   ├───conftest.py
    │   ├───test_dish_router.py
    │   └───test_order_router.py
    ├───unit
    │   ├───api
    │   │   └───v1
    │   │       └───routers
    │   │           └───test_dish_router.py
    │   └───test_order_router.py
    └───utils
        └───test_service.py

```

---

## 🧪 Тестирование

#### Локальный запуск

Для запуска тестов в терминале выполнить:

- Выполнить переход в модуль с тестами `cd tests`
- Выполнить команду `pytest`, предварительно установив библиотеку `pytest`. Для установки библиотеки — выполнить `pip install pytest`.
