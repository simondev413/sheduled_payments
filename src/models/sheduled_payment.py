from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4
from src.models.enum.sheduled_payment_enum import PaymentStatusEnum,PaymentTypeEnum


class SheduledPayment(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    user_id: str =  Field(..., alias="userId")
    amount: float
    benificiary: str
    sheduled_date: datetime
    sheduled_type: PaymentTypeEnum = PaymentTypeEnum.ONE_TIME
    status:PaymentStatusEnum = PaymentStatusEnum.PENDING
    next_execution_date: datetime
    description: str
    createdAt: datetime = Field(default_factory=datetime.today)
    updatedAt: datetime = Field(default_factory=datetime.today)

