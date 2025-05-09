from fastapi import FastAPI
from app.routes import reviews

app = FastAPI(
    title="API de Análise de Sentimento",
    version="1.0.0",
    description="Classifica avaliações em positiva, negativa ou neutra.",
)
"""
FastAPI: Instância principal da aplicação responsável por servir os endpoints da API.
"""

# Registra as rotas da API relacionadas a avaliações de clientes.
app.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
