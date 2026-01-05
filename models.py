from sqlalchemy import Column, Integer, String, Float, Enum
from database import Base
import enum


class RedemptionStatus(enum.Enum):
    UNUSED = "unused"
    REDEEMED = "redeemed"


class DataCard(Base):
    __tablename__ = "data_cards"

    id = Column(Integer, primary_key=True, index=True)
    pin = Column(String(32), unique=True, nullable=False, index=True)
    network = Column(String(20), nullable=False)
    data_gb = Column(Float, nullable=False)
    status = Column(Enum(RedemptionStatus), default=RedemptionStatus.UNUSED)
