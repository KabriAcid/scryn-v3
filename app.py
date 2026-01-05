from dataclasses import dataclass
from enum import Enum
from typing import Dict


class RedemptionStatus(Enum):
    UNUSED = "unused"
    REDEEMED = "redeemed"


@dataclass
class DataCard:
    pin: str
    network: str
    data_gb: float
    status: RedemptionStatus = RedemptionStatus.UNUSED


class DataCardRepository:
    """
    Simulates persistent storage.
    In production, replace with DB (PostgreSQL, Redis, etc.)
    """
    def __init__(self):
        self._cards: Dict[str, DataCard] = {}

    def add_card(self, card: DataCard) -> None:
        self._cards[card.pin] = card

    def get_card(self, pin: str) -> DataCard | None:
        return self._cards.get(pin)

    def mark_as_redeemed(self, pin: str) -> None:
        self._cards[pin].status = RedemptionStatus.REDEEMED


class RedemptionService:
    def __init__(self, repository: DataCardRepository):
        self.repository = repository

    def redeem(self, pin: str) -> str:
        card = self.repository.get_card(pin)

        if not card:
            return "Invalid PIN. Please check and try again."

        if card.status == RedemptionStatus.REDEEMED:
            return "This PIN has already been redeemed."

        # Business logic hook:
        # Here you would call the telco API to credit data

        self.repository.mark_as_redeemed(pin)

        return (
            f"Your purchase of {card.data_gb}GB on {card.network} "
            f"is successful. Thank you for using our service."
        )


class USSDHandler:
    """
    Handles USSD requests.
    """
    def __init__(self, redemption_service: RedemptionService):
        self.redemption_service = redemption_service

    def handle_request(self, user_input: str) -> str:
        """
        Expected format:
        *123*PIN#
        """
        try:
            pin = self._extract_pin(user_input)
        except ValueError:
            return "Invalid USSD format. Please try again."

        return self.redemption_service.redeem(pin)

    @staticmethod
    def _extract_pin(ussd_string: str) -> str:
        if not ussd_string.startswith("*") or not ussd_string.endswith("#"):
            raise ValueError("Invalid USSD format")

        parts = ussd_string.strip("#").split("*")
        if len(parts) < 2:
            raise ValueError("PIN missing")

        return parts[-1]
