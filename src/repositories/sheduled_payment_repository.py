from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.sheduled_payment_model import SheduledPayment, SheduledPaymentCreate
from src.entities.sheduled_payment_entity import SheduledPaymentEntity


class SheduledPaymentRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, sheduled_payment: SheduledPaymentCreate) -> SheduledPayment:
        entity = SheduledPaymentEntity(**sheduled_payment.model_dump())
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return SheduledPayment.model_validate(entity)

    async def list(self) -> list[SheduledPayment]:
        result = await self.session.execute(select(SheduledPaymentEntity))
        entities = result.scalars().all()
        return [SheduledPayment.model_validate(entity) for entity in entities]

    async def get(self, sheduled_payment_id: str) -> Optional[SheduledPayment]:
        entity = await self.session.get(SheduledPaymentEntity, sheduled_payment_id)
        if entity is None:
            return None
        return SheduledPayment.model_validate(entity)

    async def update(
        self,
        sheduled_payment_id: str,
        sheduled_payment: SheduledPaymentCreate,
    ) -> Optional[SheduledPayment]:
        entity = await self.session.get(SheduledPaymentEntity, sheduled_payment_id)
        if entity is None:
            return None

        for field, value in sheduled_payment.model_dump().items():
            setattr(entity, field, value)

        await self.session.commit()
        await self.session.refresh(entity)
        return SheduledPayment.model_validate(entity)

    async def delete(self, sheduled_payment_id: str) -> bool:
        entity = await self.session.get(SheduledPaymentEntity, sheduled_payment_id)
        if entity is None:
            return False

        await self.session.delete(entity)
        await self.session.commit()
        return True
    
