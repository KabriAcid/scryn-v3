from repository import DataCardRepository
from models import RedemptionStatus
from telco.base import TelcoProvider


class RedemptionService:
    def __init__(
        self,
        repository: DataCardRepository,
        telco_provider: TelcoProvider
    ):
        self.repository = repository
        self.telco_provider = telco_provider

    def redeem(self, pin: str, msisdn: str) -> str:
        card = self.repository.get_by_pin(pin)

        if not card:
            return "Invalid PIN. Please try again."

        if card.status == RedemptionStatus.REDEEMED:
            return "This PIN has already been redeemed."

        success = self.telco_provider.credit_data(msisdn, card.data_gb)
        if not success:
            return "Network error. Please try again later."

        self.repository.mark_redeemed(card)

        return (
            f"Your purchase of {card.data_gb}GB on {card.network} "
            f"is successful."
        )
