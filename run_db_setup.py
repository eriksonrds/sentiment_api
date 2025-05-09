"""
Cria as tabelas no banco de dados PostgreSQL com base nos modelos definidos no projeto.

Este script deve ser executado uma única vez após a configuração do banco
para garantir que a estrutura inicial da base de dados esteja pronta para uso.
"""

from app.database import Base, engine
from app import models

print("🔧 Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
