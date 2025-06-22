# app/core/config.py
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # API
    PROJECT_NAME: str = "PulseStream"
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:password@localhost:5432/market_data"
    
    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC_PRICE_EVENTS: str = "price-events"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    
    # Market Data Provider
    MARKET_DATA_PROVIDER: str = "finnhub"  # Options: yfinance, alpha_vantage, finnhub
    ALPHA_VANTAGE_API_KEY: Optional[str] = None
    FINNHUB_API_KEY: Optional[str] = "d1c717pr01qre5ak3npgd1c717pr01qre5ak3nq0"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()