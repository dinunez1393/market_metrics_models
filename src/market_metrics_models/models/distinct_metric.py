from sqlalchemy.orm import Mapped, relationship
from market_metrics_models.models.base import Base, BaseModelMixin


class DistinctMetric(Base, BaseModelMixin):
    """Table for distinct fundamental metrics."""
    __tablename__ = 'distinct_metric'

    name: Mapped[str]

    # One-to-many relationships - This is: Parent table
    fundamental_metrics: Mapped["list[FundamentalMetric]"] = relationship(back_populates="metric")
    rankings: Mapped["list[Ranking]"] = relationship(back_populates="metric")
