import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Usa a variável de ambiente DATABASE_URL se existir, senão usa o padrão local
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/sentiment_db")

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa (usada para os models)
Base = declarative_base()
