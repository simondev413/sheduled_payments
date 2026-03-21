from enum import Enum


class PaymentStatusEnum(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class PaymentTypeEnum(str, Enum):
    ONE_TIME = "one_time"
    RECURRING = "recurring"
