from fastapi import HTTPException, Response, status

from src.models.sheduled_payment_model import SheduledPaymentCreate
from src.services.sheduled_payments_service import SheduledPaymentService


class SheduledPaymentController:
    def __init__(self, service: SheduledPaymentService) -> None:
        self.service = service

    async def create_sheduled_payment(self, sheduled_payment: SheduledPaymentCreate, response: Response):
        created_payment = await self.service.create_sheduled_payment(sheduled_payment)
        response.status_code = status.HTTP_201_CREATED
        return created_payment

    async def list_sheduled_payments(self):
        return await self.service.list_sheduled_payments()

    async def get_sheduled_payment(self, sheduled_payment_id: str):
        sheduled_payment = await self.service.get_sheduled_payment(sheduled_payment_id)
        if sheduled_payment is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scheduled payment not found")
        return sheduled_payment

    async def update_sheduled_payment(self, sheduled_payment_id: str, sheduled_payment: SheduledPaymentCreate):
        updated_payment = await self.service.update_sheduled_payment(sheduled_payment_id, sheduled_payment)
        if updated_payment is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scheduled payment not found")
        return updated_payment

    async def delete_sheduled_payment(self, sheduled_payment_id: str):
        deleted = await self.service.delete_sheduled_payment(sheduled_payment_id)
        if not deleted:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scheduled payment not found")
        return {"deleted": True}
    
   
