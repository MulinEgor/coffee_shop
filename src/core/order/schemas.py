from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from src.core.order.models import ObtainingMethod, Status
from src.core.position.schemas import PositionGetSchema


class OrderPositionCreateSchema(BaseModel):
    """
    Pydantic схема для создания позиции в заказе.
    """

    position_id: int
    quantity: int = Field(ge=1, description="Количество позиций")
    weight: int = Field(ge=1, description="Вес позиции")


class OrderPositionGetSchema(OrderPositionCreateSchema):
    """
    Pydantic схема для получения позиции в заказе.
    """

    position: Optional[PositionGetSchema] = None


class OrderCreateSchema(BaseModel):
    """
    Pydantic схема для создания заказа.
    """

    user_id: int
    order_positions: list[OrderPositionCreateSchema]
    obtaining_method: ObtainingMethod


class OrderUpdateSchema(BaseModel):
    """
    Pydantic схема для обновления заказа. Все поля необязательные.
    """

    user_id: Optional[int] = None
    order_positions: Optional[list[OrderPositionCreateSchema]] = None
    obtaining_method: Optional[ObtainingMethod] = None
    date: Optional[datetime] = None
    status: Optional[Status] = None


class OrderGetSchema(OrderCreateSchema):
    """
    Pydantic схема для получения заказа.
    """

    id: int
    date: datetime
    status: Status
    total_price: int | None
    order_positions: list[OrderPositionGetSchema]
