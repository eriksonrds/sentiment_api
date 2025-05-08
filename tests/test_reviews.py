from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_review():
    response = client.post("/reviews", json={
        "cliente": "Teste Automatizado",
        "data_avaliacao": "2024-09-15",
        "texto": "O suporte foi rápido e resolveu tudo com eficiência."
    })
    assert response.status_code == 200
    data = response.json()
    assert data["cliente"] == "Teste Automatizado"
    assert data["classificacao"] in ["positiva", "neutra", "negativa"]
    assert "id" in data


def test_get_all_reviews():
    response = client.get("/reviews")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_report():
    response = client.get("/reviews/report", params={
        "start_date": "2024-09-01",
        "end_date": "2024-09-30"
    })
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert "positiva" in data
    assert "neutra" in data
    assert "negativa" in data
    assert "total" in data
    assert "periodo" in data

