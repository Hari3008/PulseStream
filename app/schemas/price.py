from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class PriceResponse(BaseModel):
    symbol: str
    price: float
    timestamp: datetime
    provider: str


class PollRequest(BaseModel):
    symbols: List[str]
    interval: int  # seconds
    provider: Optional[str] = "finnhub"


class PollResponse(BaseModel):
    job_id: str
    status: str
    config: PollRequest


class KafkaPriceMessage(BaseModel):
    symbol: str
    price: float
    timestamp: datetime
    source: str
    raw_response_id: Optional[str] = None