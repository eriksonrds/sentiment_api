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
git clone https://github.com/eriksonrds/sentiment_api.git
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

## Executando a API

```bash
uvicorn app.main:app --reload
```

A documentação interativa da API estará disponível em:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

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
│   ├── test_reviews.py
│   └── test_examples_dataset.py
├── run_db_setup.py
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Observações sobre a Análise de Sentimento

A análise de sentimento foi implementada inicialmente com o algoritmo VADER, por sua leveza e simplicidade. No entanto, mesmo com ajustes de thresholds, o VADER apresenta limitações consideráveis para textos em português — especialmente em avaliações mais complexas ou ambíguas.

### ✨ Otimização com Tradução Automática

Embora o desafio não exigisse alta acurácia, foi adotada uma estratégia adicional para melhorar a qualidade das classificações: os textos em português são traduzidos automaticamente para inglês antes da aplicação do VADER. Essa abordagem simples e leve elevou a acurácia de 30% para 70% no conjunto de testes fornecido, sem necessidade de modelos pesados ou fine-tuning.

Essa escolha foi feita com o objetivo de melhorar o desempenho da classificação sem comprometer a leveza e a simplicidade da aplicação, mantendo a compatibilidade com o escopo do desafio proposto.

### Flexibilidade para evolução

A arquitetura da API está preparada para suportar facilmente a substituição do classificador por uma abordagem mais robusta baseada em modelos da Hugging Face com fine-tuning e embeddings.

O arquivo `test_examples_dataset.py` foi criado para validar automaticamente os exemplos fornecidos no anexo do teste técnico. Ele permite comparar a saída do classificador com os rótulos esperados e testar melhorias iterativas.

---