from enum import Enum

class PaymentStatusEnum(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class PaymentTypeEnum(Enum):
    ONE_TIME = "one_time"
    RECURRING = "recurring"