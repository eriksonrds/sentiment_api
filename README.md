# API de Análise de Sentimento

Este projeto é uma API REST desenvolvida com **FastAPI** que classifica avaliações de clientes como **positiva**, **negativa** ou **neutra** utilizando análise de sentimento.

---

## Tecnologias Utilizadas

* Python 3.10+
* FastAPI
* SQLAlchemy
* PostgreSQL
* VADER Sentiment Analyzer
* Docker + Docker Compose
* Pydantic
* Pytest
* Uvicorn

---

## Como rodar localmente

### 1. Clone o projeto

```bash
git clone https://github.com/seuusuario/sentiment_api.git
cd sentiment_api
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## Rodando o banco PostgreSQL com Docker

Certifique-se de ter o Docker instalado. Depois, execute:

```bash
docker-compose up -d
```

Isso criará um container com:

* **Banco**: sentiment\_db
* **Usuário**: postgres
* **Senha**: postgres
* Porta local: `5432`

---

## Criando as tabelas no banco

```bash
python run_db_setup.py
```

---

##  Executando a API

```bash
uvicorn app.main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Endpoints disponíveis

* `POST /reviews`: envia uma nova avaliação
* `GET /reviews`: lista todas as avaliações
* `GET /reviews/{id}`: consulta uma avaliação específica
* `GET /reviews/report?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD`: retorna relatório de sentimentos no período

---

## Rodando os testes

```bash
pytest
```

---

## Estrutura de Pastas

```
sentiment_api/
├── app/
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   │   └── reviews.py
│   ├── schemas.py
│   └── sentiment.py
├── tests/
│   └── test_reviews.py
├── run_db_setup.py
├── requirements.txt
├── docker-compose.yml
└── README.md
```
