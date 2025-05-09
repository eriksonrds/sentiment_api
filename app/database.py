import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Usa a variável de ambiente DATABASE_URL se existir, senão utiliza uma conexão local padrão.
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/sentiment_db"
)
"""
str: URL de conexão com o banco de dados PostgreSQL.
"""

# Cria o engine do SQLAlchemy responsável por gerenciar a comunicação com o banco.
engine = create_engine(DATABASE_URL)
"""
Engine: Objeto do SQLAlchemy que representa a interface com o banco de dados.
"""

# Cria a fábrica de sessões para executar transações no banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
sessionmaker: Função que retorna uma nova sessão de conexão com o banco de dados.
"""

# Base para os modelos ORM.
Base = declarative_base()
"""
DeclarativeMeta: Classe base utilizada para definir os modelos do SQLAlchemy.
"""
