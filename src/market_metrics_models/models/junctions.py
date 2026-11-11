# Intermediary tables for Many-to-Many relationships
from sqlalchemy import Column, ForeignKey, Table
from market_metrics_models.models.base import Base


# Plain intermediary table for Companies - Metrics Many-To-Many relationship
company_metric_junction = Table(
    "company_metric_junction",
    Base.metadata,
    Column('company_id', ForeignKey('company_data.id'), primary_key=True),
    Column('metric_id', ForeignKey('fundamental_metric.id'), primary_key=True),
)

# Plain intermediary table for Companies - Ranking Many-To-Many relationship
company_ranking_junction = Table(
    "company_ranking_junction",
    Base.metadata,
    Column('company_id', ForeignKey('company_data.id'), primary_key=True),
    Column('ranking_id', ForeignKey('ranking.id'), primary_key=True),
)
