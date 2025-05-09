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
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── sentiment.py
│   └── routes/
│       └── reviews.py
├── tests/
│   ├── test_reviews.py
│   └── test_examples_dataset.py
├── docker-compose.yml
├── load_examples.py
├── README.md
├── requirements.txt
├── run_db_setup.py
└── setup.cfg
```

---

## Observações sobre a Análise de Sentimento

A análise de sentimento foi implementada inicialmente com o algoritmo VADER, por sua leveza e simplicidade. No entanto, mesmo com ajustes de thresholds, o VADER apresenta limitações consideráveis para textos em português — especialmente em avaliações mais complexas ou ambíguas.

### Otimização com Tradução Automática

Embora o desafio não exigisse alta acurácia, foi adotada uma estratégia adicional para melhorar a qualidade das classificações: os textos em português são traduzidos automaticamente para inglês antes da aplicação do VADER. Essa abordagem simples e leve elevou a acurácia de 30% para até 70% no conjunto de testes fornecido, sem necessidade de modelos pesados ou fine-tuning.

A variação na acurácia depende diretamente do threshold escolhido para o `compound score` do VADER:

* Com configuração **mais permissiva** (threshold ±0.1), foi possível atingir **até 70% de acerto**.
* Com configuração **mais conservadora** (threshold ±0.4), a acurácia ficou em torno de **60%**, com menor risco de falsos positivos (ex: classificar algo neutro como positivo).

Essa escolha representa um equilíbrio entre sensibilidade e precisão, e demonstra atenção prática à calibragem do classificador de acordo com o comportamento dos dados.

### Flexibilidade para evolução

A arquitetura da API está preparada para suportar facilmente a substituição do classificador por uma abordagem mais robusta baseada em modelos da Hugging Face com fine-tuning e embeddings.

O arquivo `test_examples_dataset.py` foi criado para validar automaticamente os exemplos fornecidos no anexo do teste técnico. Ele permite comparar a saída do classificador com os rótulos esperados e testar melhorias iterativas.

---

> 📅 Desafio: "Teste Prático Desenvolvedor Back-End Python" — WeOn
