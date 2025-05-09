from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_review():
    """
    Testa a criação de uma nova avaliação via POST /reviews.

    Verifica se o status da resposta é 200 e se os campos esperados estão presentes,
    incluindo a classificação de sentimento retornada pela API.
    """
    response = client.post(
        "/reviews",
        json={
            "cliente": "Teste Automatizado",
            "data_avaliacao": "2024-09-15",
            "texto": "O suporte foi rápido e resolveu tudo com eficiência.",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["cliente"] == "Teste Automatizado"
    assert data["classificacao"] in ["positiva", "neutra", "negativa"]
    assert "id" in data


def test_get_all_reviews():
    """
    Testa a recuperação de todas as avaliações via GET /reviews.

    Verifica se a resposta é uma lista não vazia com status 200.
    """
    response = client.get("/reviews")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_report():
    """
    Testa o relatório de sentimento por período via GET /reviews/report.

    Verifica se todos os campos esperados estão presentes no retorno
    e se o status da resposta é 200.
    """
    response = client.get(
        "/reviews/report", params={"start_date": "2024-09-01", "end_date": "2024-09-30"}
    )
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert "positiva" in data
    assert "neutra" in data
    assert "negativa" in data
    assert "total" in data
    assert "periodo" in data
