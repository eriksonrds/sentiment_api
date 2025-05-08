from app.database import Base, engine
from app import models

print("🔧 Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso!")
