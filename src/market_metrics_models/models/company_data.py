from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from market_metrics_models.models.base import Base, BaseModelMixin


class CompanyData(Base, BaseModelMixin):
    """Stock Market symbols dynamic data."""
    __tablename__ = 'company_data'

    symbol: Mapped[str]
    price: Mapped[float]
    market_cap: Mapped[float]
    volume: Mapped[int]
    average_volume: Mapped[float]
    beta: Mapped[float]
    ema_200_close: Mapped[float]
    lowest_52_weeks: Mapped[float]
    highest_52_weeks: Mapped[float]
    extraction_date: Mapped[date]

    # Many-to-One relationship - This is: Child table
    company_profile_id: Mapped[int] = mapped_column(ForeignKey('static_company_profile.id'))
    company_profile: Mapped["StaticCompanyProfile"] = relationship(back_populates='companies')

    # Many-to-Many relationships: links to 'FundamentalMetric' via the junction table 'company_metric_junction'
    fundamental_metrics: Mapped["list[FundamentalMetric]"] = relationship(
        secondary="company_metric_junction",
        back_populates='companies',
    )
    # links to 'Ranking' via the junction table 'company_ranking_junction'
    rankings: Mapped["list[Ranking]"] = relationship(
        secondary="company_ranking_junction",
        back_populates='companies',
    )
