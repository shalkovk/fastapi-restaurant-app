"""Содержит вспомогательные классы и функции для тестов."""

from collections.abc import Callable, Iterable, Sequence
from contextlib import AbstractContextManager, nullcontext
from typing import Any, TypeVar

from pydantic import BaseModel
from httpx import Response
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from starlette.status import HTTP_200_OK

BASE_ENDPOINT_URL = "/api/v1"

Check = Callable[[dict[str, Any]], bool]
T = TypeVar("T")


class BaseConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class TestDescription(BaseConfig):
    description: str = ''


class TestExpectation(BaseConfig):
    expected_error: AbstractContextManager = nullcontext()
    expected_status: int = HTTP_200_OK
    expected_data: Any = None
    checks: Iterable[Check] | None = None


class BaseTestCase(TestDescription, TestExpectation):
    data: dict | None = None


class RequestTestCase(BaseTestCase):
    url: str = BASE_ENDPOINT_URL
    headers: dict | None = None


async def bulk_save_models(
    session: AsyncSession,
    model: type[DeclarativeBase],
    data: Iterable[dict[str, Any]],
    *,
    commit: bool = False,
) -> None:
    """
    Сохраняет сразу множество моделей в БД.
    """
    for values in data:
        await session.execute(insert(model).values(**values))

    if commit:
        await session.commit()
    else:
        await session.flush()


def compare_dicts_and_db_models(
    result: Sequence[DeclarativeBase] | None,
    expected_result: Sequence[dict] | None,
    schema: type[BaseModel],
) -> bool:
    """
    Сравнивает результат из БД с ожидаемыми данными.
    Все переводится в Pydantic-схемы.
    """
    if result is None or expected_result is None:
        return result == expected_result

    result_to_schema = [schema(**item.__dict__) for item in result]
    expected_result_to_schema = [schema(**item) for item in expected_result]

    equality_len = len(result_to_schema) == len(expected_result_to_schema)
    equality_obj = all(
        obj in expected_result_to_schema for obj in result_to_schema)

    return all((equality_len, equality_obj))


def prepare_payload(response: Response, exclude: Sequence[str] | None = None) -> dict:
    """
    Извлекает полезную нагрузку из ответа и исключает указанные поля.
    """
    try:
        payload = response.json()
    except Exception:
        return {}

    if exclude:
        for key in exclude:
            payload.pop(key, None)

    return payload
