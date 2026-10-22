from enum import Enum
class PaymentType(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    CASH = "CASH"
    CHECK = "CHECK"
    OTHER = "OTHER"