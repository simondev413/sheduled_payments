from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from sqlalchemy import DateTime, Enum as SQLEnum, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.database import Base
from src.models.enum.sheduled_payment_enum import PaymentStatusEnum, PaymentTypeEnum


def enum_values(enum_class: Any) -> list[str]:
    return [item.value for item in enum_class]


class SheduledPaymentEntity(Base):
    __tablename__ = "sheduled_payments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    user_id: Mapped[str] = mapped_column(String(255), nullable=False)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    benificiary: Mapped[str] = mapped_column(String(255), nullable=False)
    sheduled_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    sheduled_type: Mapped[PaymentTypeEnum] = mapped_column(
        SQLEnum(PaymentTypeEnum, name="payment_type_enum", values_callable=enum_values),
        nullable=False,
        default=PaymentTypeEnum.ONE_TIME,
    )
    status: Mapped[PaymentStatusEnum] = mapped_column(
        SQLEnum(PaymentStatusEnum, name="payment_status_enum", values_callable=enum_values),
        nullable=False,
        default=PaymentStatusEnum.PENDING,
    )
    next_execution_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    createdAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updatedAt: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
