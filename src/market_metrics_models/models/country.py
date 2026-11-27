from sqlalchemy.orm import Mapped, relationship
from market_metrics_models.models.base import Base, BaseModelMixin


class Country(Base, BaseModelMixin):
    __tablename__ = 'country'

    country: Mapped[str]

    # One-to-many relationship - This is: Parent table
    company_profiles: Mapped[list["StaticCompanyProfile"]] = relationship(back_populates="country")
