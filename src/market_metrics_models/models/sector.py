from sqlalchemy.orm import Mapped, relationship
from market_metrics_models.models.base import Base, BaseModelMixin


class Sector(Base, BaseModelMixin):
    __tablename__ = 'sector'

    sector: Mapped[str]

    # One-to-many - This is: Parent table
    industries: Mapped[list["Industry"]] = relationship(back_populates="sector")
