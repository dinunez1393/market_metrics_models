from sqlalchemy.orm import Mapped, relationship
from market_metrics_models.models.base import Base, BaseModelMixin


class Currency(Base, BaseModelMixin):
    __tablename__ = 'currency'

    currency: Mapped[str]

    # One-to-Many - This is: Parent table
    company_profiles: Mapped["list[StaticCompanyProfile]"] = relationship(back_populates="currency")
