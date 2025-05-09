from pydantic import BaseModel, ConfigDict
from datetime import date, datetime


class ReviewCreate(BaseModel):
    """
    Schema para entrada de dados de uma nova avaliação via API.

    Attributes:
        cliente (str): Nome do cliente.
        data_avaliacao (date): Data da avaliação.
        texto (str): Texto da avaliação fornecida.
    """

    cliente: str
    data_avaliacao: date
    texto: str


class ReviewResponse(BaseModel):
    """
    Schema de resposta da API representando uma avaliação completa.

    Attributes:
        id (int): Identificador único da avaliação.
        cliente (str): Nome do cliente.
        data_avaliacao (date): Data da avaliação.
        texto (str): Texto da avaliação.
        classificacao (str): Classificação de sentimento ('positiva', 'negativa' ou 'neutra').
        created_at (datetime): Data/hora de criação do registro.
    """

    id: int
    cliente: str
    data_avaliacao: date
    texto: str
    classificacao: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
