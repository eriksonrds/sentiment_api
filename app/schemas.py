from pydantic import BaseModel, ConfigDict
from datetime import date, datetime


class ReviewCreate(BaseModel):
    cliente: str
    data_avaliacao: date
    texto: str


class ReviewResponse(BaseModel):
    id: int
    cliente: str
    data_avaliacao: date
    texto: str
    classificacao: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
