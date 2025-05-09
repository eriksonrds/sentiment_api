from sqlalchemy import Column, Integer, String, Date, DateTime
from app.database import Base
from datetime import datetime


class Review(Base):
    """
    Modelo ORM para representar uma avaliação de cliente no banco de dados.

    Attributes:
        id (int): Identificador único da avaliação.
        cliente (str): Nome do cliente que realizou a avaliação.
        data_avaliacao (date): Data em que a avaliação foi feita.
        texto (str): Texto da avaliação fornecida pelo cliente.
        classificacao (str): Resultado da análise de sentimento ('positiva', 'negativa' ou 'neutra').
        created_at (datetime): Data e hora de criação do registro no banco (definido automaticamente).
    """

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, nullable=False)
    data_avaliacao = Column(Date, nullable=False)
    texto = Column(String, nullable=False)
    classificacao = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
