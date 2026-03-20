from fastapi import APIRouter
from src.controllers.sheduled_payment_controllers import SheduledPaymentController
from src.services.sheduled_payments_service import SheduledPaymentService
from src.repositories.sheduled_payment_repository import SheduledPaymentRepository
from src.models.sheduled_payment import SheduledPayment
from fastapi import Request, Response

router = APIRouter(prefix="/sheduled_payments", tags=["Sheduled Payments"])

repository = SheduledPaymentRepository(db={})
service = SheduledPaymentService(repository)
controller = SheduledPaymentController(service)


@router.post("/")
async def create_sheduled_payment(request: Request, response: Response):
    controller = SheduledPaymentController(service)
    return await controller.create_sheduled_payment(request, response)

@router.get("/{sheduled_payment_id}",response_model=SheduledPayment)
async def get_sheduled_payment(sheduled_payment_id: str):
    controller = SheduledPaymentController(service)
    return await controller.get_sheduled_payment(sheduled_payment_id)

@router.get("/")
async def list_sheduled_payments():
    controller = SheduledPaymentController(service)
    return await controller.list_sheduled_payments()

@router.put("/{sheduled_payment_id}")
async def update_sheduled_payment(sheduled_payment_id: str, request: Request):
    controller = SheduledPaymentController(service)
    return await controller.update_sheduled_payment(sheduled_payment_id, request)   

@router.delete("/{sheduled_payment_id}")
async def delete_sheduled_payment(sheduled_payment_id: str):
    controller = SheduledPaymentController(service)
    return await controller.delete_sheduled_payment(sheduled_payment_id)
