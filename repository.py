from sqlalchemy.orm import Session
from models import DataCard, RedemptionStatus


class DataCardRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_pin(self, pin: str) -> DataCard | None:
        return self.db.query(DataCard).filter(DataCard.pin == pin).first()

    def mark_redeemed(self, card: DataCard):
        card.status = RedemptionStatus.REDEEMED
        self.db.commit()
