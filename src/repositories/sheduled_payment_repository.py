from src.models.sheduled_payment import SheduledPayment
from typing import Any,Dict,Optional

class SheduledPaymentRepository:
    def __init__(self, db:Dict[str, Any]) -> None:
        self.db = db

    async def create(self, sheduled_payment: SheduledPayment) -> SheduledPayment:
        self.db[sheduled_payment.id] = sheduled_payment
        return sheduled_payment

    async def list(self):
        return list(self.db.values())

    async def get(self, sheduled_payment_id: str) -> Optional[SheduledPayment]:
        return self.db.get(sheduled_payment_id)

    async def update(self, sheduled_payment_id: str, sheduled_payment: SheduledPayment) -> Optional[SheduledPayment]:
        if sheduled_payment_id in self.db:
            self.db[sheduled_payment_id] = sheduled_payment
            return sheduled_payment
        return None 
    
    async def delete(self, sheduled_payment_id: str) -> bool:
        if sheduled_payment_id in self.db:
            del self.db[sheduled_payment_id]
            return True
        return False
    
