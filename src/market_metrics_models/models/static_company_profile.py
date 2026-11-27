from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from market_metrics_models.models.base import Base, BaseModelMixin


class StaticCompanyProfile(Base, BaseModelMixin):
    __tablename__ = 'static_company_profile'

    company_name: Mapped[str]
    isin: Mapped[str]
    ipo_date: Mapped[date]

    # Many-to-One relationships - This is: Child table
    currency_id: Mapped[int] = mapped_column(ForeignKey('currency.id'))
    currency: Mapped["Currency"] = relationship(back_populates='company_profiles')

    country_id: Mapped[int] = mapped_column(ForeignKey('country.id'))
    country: Mapped["Country"] = relationship(back_populates='company_profiles')

    industry_id: Mapped[int] = mapped_column(ForeignKey('industry.id'))
    industry: Mapped["Industry"] = relationship(back_populates='company_profiles')

    market_id: Mapped[int] = mapped_column(ForeignKey('market.id'))
    market: Mapped["Market"] = relationship(back_populates='company_profiles')

    # One-to-Many relationship - This is: Parent table
    companies: Mapped[list["CompanyData"]] = relationship(back_populates='company_profile')
