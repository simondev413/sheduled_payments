from src.repositories.sheduled_payment_repository import SheduledPaymentRepository
from src.models.sheduled_payment import SheduledPayment

class SheduledPaymentService:
    def __init__(self, repository: SheduledPaymentRepository) -> None:
        self.repository = repository

    async def create_sheduled_payment(self, sheduled_payment: SheduledPayment):
        return await self.repository.create(sheduled_payment)
    
    async def list_sheduled_payments(self):
        return await self.repository.list()

    async def get_sheduled_payment(self, sheduled_payment_id: str):
        return await self.repository.get(sheduled_payment_id)

    async def update_sheduled_payment(self, sheduled_payment_id: str, sheduled_payment: SheduledPayment):
        return await self.repository.update(sheduled_payment_id, sheduled_payment)

    async def delete_sheduled_payment(self, sheduled_payment_id: str):
        return await self.repository.delete(sheduled_payment_id)