from sqlalchemy import Column, Integer, String, Date, DateTime
from app.database import Base
from datetime import datetime


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    data_avaliacao = Column(Date, nullable=False)
    texto = Column(String, nullable=False)
    classificacao = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
