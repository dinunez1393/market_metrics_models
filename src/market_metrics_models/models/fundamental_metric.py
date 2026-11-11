from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from market_metrics_models.models.base import Base, BaseModelMixin


class FundamentalMetric(Base, BaseModelMixin):
    __tablename__ = 'fundamental_metric'

    # Many-to-one relationship - This is: Child table
    metric_id: Mapped[int] = mapped_column(ForeignKey('distinct_metric.id'))
    metric: Mapped["DistinctMetric"] = relationship(back_populates='fundamental_metrics')

    # Many-to-Many relationship: links to 'Company' via the junction table 'company_metric_junction'
    companies: Mapped["list[CompanyData]"] = relationship(
        secondary="company_metric_junction",
        back_populates='fundamental_metrics',
    )
