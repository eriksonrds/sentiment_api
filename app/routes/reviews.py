from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, date
from collections import Counter

from app import models, schemas, database, sentiment

router = APIRouter()


def get_db():
    """
    Cria uma sessão com o banco de dados e garante seu fechamento após o uso.

    Yields:
        Session: Sessão ativa do banco de dados.
    """
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ReviewResponse)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova avaliação, classifica o sentimento automaticamente e armazena no banco.

    Args:
        review (schemas.ReviewCreate): Dados da avaliação recebidos na requisição.
        db (Session): Sessão ativa do banco de dados.

    Returns:
        schemas.ReviewResponse: Avaliação criada com classificação de sentimento.
    """
    classification = sentiment.analyze_sentiment(review.texto)

    db_review = models.Review(
        cliente=review.cliente,
        data_avaliacao=review.data_avaliacao,
        texto=review.texto,
        classificacao=classification,
        created_at=datetime.utcnow(),
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review


@router.get("/", response_model=list[schemas.ReviewResponse])
def get_all_reviews(db: Session = Depends(get_db)):
    """
    Retorna todas as avaliações registradas no banco.

    Args:
        db (Session): Sessão ativa do banco de dados.

    Returns:
        list[schemas.ReviewResponse]: Lista de todas as avaliações.
    """
    return db.query(models.Review).all()


@router.get("/report")
def get_report(
    start_date: date = Query(..., description="Data inicial no formato YYYY-MM-DD"),
    end_date: date = Query(..., description="Data final no formato YYYY-MM-DD"),
    db: Session = Depends(get_db),
):
    """
    Gera um relatório com contagem de avaliações por sentimento dentro de um período.

    Args:
        start_date (date): Data inicial do filtro.
        end_date (date): Data final do filtro.
        db (Session): Sessão ativa do banco de dados.

    Returns:
        dict: Contagem de avaliações por tipo de sentimento e intervalo do período.
    """
    resultados = (
        db.query(models.Review)
        .filter(models.Review.data_avaliacao.between(start_date, end_date))
        .all()
    )

    contagem = Counter([r.classificacao for r in resultados])

    return {
        "positiva": contagem.get("positiva", 0),
        "neutra": contagem.get("neutra", 0),
        "negativa": contagem.get("negativa", 0),
        "total": sum(contagem.values()),
        "periodo": {"de": str(start_date), "ate": str(end_date)},
    }


@router.get("/{review_id}", response_model=schemas.ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    """
    Recupera uma avaliação específica pelo ID informado.

    Args:
        review_id (int): ID da avaliação buscada.
        db (Session): Sessão ativa do banco de dados.

    Returns:
        schemas.ReviewResponse: Avaliação encontrada ou erro 404 se inexistente.
    """
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review não encontrada")
    return review
