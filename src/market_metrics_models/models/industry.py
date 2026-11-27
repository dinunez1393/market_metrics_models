from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from market_metrics_models.models.base import Base, BaseModelMixin


class Industry(Base, BaseModelMixin):
    __tablename__ = 'industry'

    industry: Mapped[str]

    # Many-to-one relationship - This is: Child table
    sector_id: Mapped[int] = mapped_column(ForeignKey('sector.id'))
    sector: Mapped["Sector"] = relationship(back_populates='industries')

    # One-to-many relationship - This is: Parent table
    company_profiles: Mapped[list["StaticCompanyProfile"]] = relationship(back_populates="industry")
