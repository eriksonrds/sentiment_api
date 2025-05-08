from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, date
from collections import Counter

from app import models, schemas, database, sentiment

router = APIRouter()


# Dependency do banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ReviewResponse)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    """
    Recebe uma avaliação de cliente e classifica o sentimento automaticamente.
    """
    classification = sentiment.analyze_sentiment(review.texto)

    db_review = models.Review(
        cliente=review.cliente,
        data_avaliacao=review.data_avaliacao,
        texto=review.texto,
        classificacao=classification,
        created_at=datetime.utcnow()
    )

    db.add(db_review)
    db.commit()
    db.refresh(db_review)

    return db_review


@router.get("/", response_model=list[schemas.ReviewResponse])
def get_all_reviews(db: Session = Depends(get_db)):
    """
    Retorna todas as avaliações analisadas.
    """
    return db.query(models.Review).all()


@router.get("/report")
def get_report(
    start_date: date = Query(..., description="Data inicial no formato YYYY-MM-DD"),
    end_date: date = Query(..., description="Data final no formato YYYY-MM-DD"),
    db: Session = Depends(get_db)
):
    """
    Retorna um relatório de contagem de avaliações por sentimento dentro do período.
    """
    resultados = db.query(models.Review).filter(
        models.Review.data_avaliacao.between(start_date, end_date)
    ).all()

    contagem = Counter([r.classificacao for r in resultados])

    return {
        "positiva": contagem.get("positiva", 0),
        "neutra": contagem.get("neutra", 0),
        "negativa": contagem.get("negativa", 0),
        "total": sum(contagem.values()),
        "periodo": {
            "de": str(start_date),
            "ate": str(end_date)
        }
    }


@router.get("/{review_id}", response_model=schemas.ReviewResponse)
def get_review(review_id: int, db: Session = Depends(get_db)):
    """
    Busca uma avaliação específica pelo ID.
    """
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review não encontrada")
    return review
