from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Index
from sqlalchemy.sql import func
from app.core.database import Base


class RawMarketData(Base):
    __tablename__ = "raw_market_data"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    raw_response = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        Index('idx_raw_market_symbol_created', 'symbol', 'created_at'),
    )


class ProcessedPrice(Base):
    __tablename__ = "processed_prices"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    provider = Column(String, nullable=False)
    raw_response_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        Index('idx_processed_symbol_timestamp', 'symbol', 'timestamp'),
    )


class MovingAverage(Base):
    __tablename__ = "moving_averages"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, nullable=False)
    ma_value = Column(Float, nullable=False)
    period = Column(Integer, default=5)
    timestamp = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        Index('idx_ma_symbol_timestamp', 'symbol', 'timestamp'),
    )


class PollingJobConfig(Base):
    __tablename__ = "polling_job_configs"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, unique=True, nullable=False)
    symbols = Column(JSON, nullable=False)  # List of symbols
    interval = Column(Integer, nullable=False)  # Seconds
    provider = Column(String, nullable=False)
    status = Column(String, default="active")  # active, paused, stopped
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())