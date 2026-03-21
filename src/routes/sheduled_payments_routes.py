from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from src.controllers.sheduled_payment_controllers import SheduledPaymentController
from src.database.database import get_session
from src.models.sheduled_payment_model import SheduledPayment, SheduledPaymentCreate
from src.repositories.sheduled_payment_repository import SheduledPaymentRepository
from src.services.sheduled_payments_service import SheduledPaymentService

router = APIRouter(prefix="/sheduled_payments", tags=["Sheduled Payments"])


def get_controller(session: AsyncSession = Depends(get_session)) -> SheduledPaymentController:
    repository = SheduledPaymentRepository(session)
    service = SheduledPaymentService(repository)
    return SheduledPaymentController(service)


@router.post("/", response_model=SheduledPayment, status_code=201)
async def create_sheduled_payment(
    sheduled_payment: SheduledPaymentCreate,
    response: Response,
    controller: SheduledPaymentController = Depends(get_controller),
):
    return await controller.create_sheduled_payment(sheduled_payment, response)


@router.get("/{sheduled_payment_id}", response_model=SheduledPayment)
async def get_sheduled_payment(
    sheduled_payment_id: str,
    controller: SheduledPaymentController = Depends(get_controller),
):
    return await controller.get_sheduled_payment(sheduled_payment_id)


@router.get("/", response_model=list[SheduledPayment])
async def list_sheduled_payments(
    controller: SheduledPaymentController = Depends(get_controller),
):
    return await controller.list_sheduled_payments()


@router.put("/{sheduled_payment_id}", response_model=SheduledPayment)
async def update_sheduled_payment(
    sheduled_payment_id: str,
    sheduled_payment: SheduledPaymentCreate,
    controller: SheduledPaymentController = Depends(get_controller),
):
    return await controller.update_sheduled_payment(sheduled_payment_id, sheduled_payment)


@router.delete("/{sheduled_payment_id}")
async def delete_sheduled_payment(
    sheduled_payment_id: str,
    controller: SheduledPaymentController = Depends(get_controller),
):
    return await controller.delete_sheduled_payment(sheduled_payment_id)
