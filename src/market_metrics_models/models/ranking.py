from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from market_metrics_models.models.base import Base, BaseModelMixin


class Ranking(Base, BaseModelMixin):
    __tablename__ = 'ranking'

    by_industry: Mapped[bool]
    by_sector: Mapped[bool]
    by_market: Mapped[bool]

    # Many-to-one relationship - This is: Child table
    metric_id: Mapped[int] = mapped_column(ForeignKey('distinct_metric.id'))
    metric: Mapped["DistinctMetric"] = relationship(back_populates='rankings')

    # Many-to-Many relationship: links to 'Company' via the junction table 'company_ranking_junction'
    companies: Mapped[list["CompanyData"]] = relationship(
        secondary="company_ranking_junction",
        back_populates='rankings',
    )
