from src.services.sheduled_payments_service import SheduledPaymentService
from src.models.sheduled_payment import SheduledPayment
from fastapi import Request,Response



class SheduledPaymentController:
    def __init__(self, service: SheduledPaymentService) -> None:
        self.service = service

    async def create_sheduled_payment(self, request: Request, response: Response):
        request_data = await request.json()
        sheduled_payment = SheduledPayment(**request_data)
        validated_data = SheduledPayment.model_validate(sheduled_payment)
        created_payment = await self.service.create_sheduled_payment(validated_data)
        response.status_code = 201
        return created_payment.model_dump()

    async def list_sheduled_payments(self):
        return await self.service.list_sheduled_payments()

    async def get_sheduled_payment(self, sheduled_payment_id: str):
        return await self.service.get_sheduled_payment(sheduled_payment_id)

    async def update_sheduled_payment(self, sheduled_payment_id: str, request: Request):
        sheduled_payment_data = await request.json()
        sheduled_payment = SheduledPayment.model_validate(**sheduled_payment_data)
        return await self.service.update_sheduled_payment(sheduled_payment_id, sheduled_payment)

    async def delete_sheduled_payment(self, sheduled_payment_id: str):
        return await self.service.delete_sheduled_payment(sheduled_payment_id)
    
   