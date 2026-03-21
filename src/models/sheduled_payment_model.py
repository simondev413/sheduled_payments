from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from src.models.enum.sheduled_payment_enum import PaymentStatusEnum, PaymentTypeEnum


class SheduledPaymentBase(BaseModel):
    user_id: str = Field(..., alias="userId")
    amount: float
    benificiary: str
    sheduled_date: datetime
    sheduled_type: PaymentTypeEnum = PaymentTypeEnum.ONE_TIME
    status: PaymentStatusEnum = PaymentStatusEnum.PENDING
    next_execution_date: datetime
    description: str

    model_config = ConfigDict(populate_by_name=True, use_enum_values=False)


class SheduledPaymentCreate(SheduledPaymentBase):
    pass


class SheduledPayment(SheduledPaymentBase):
    id: str = Field(default_factory=lambda: str(uuid4()))
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, use_enum_values=False)

