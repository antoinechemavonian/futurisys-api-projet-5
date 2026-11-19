from sqlalchemy import func, select

from app import models


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["modele_charge"] is True


def test_predict_valide(client, employe):
    r = client.post("/predict", json=employe)
    assert r.status_code == 200
    corps = r.json()
    assert corps["prediction"] in ("Oui", "Non")
    assert 0 <= corps["probabilite"] <= 1
    assert corps["version_modele"]


def test_predict_est_deterministe(client, employe):
    a = client.post("/predict", json=employe).json()
    b = client.post("/predict", json=employe).json()
    assert a["probabilite"] == b["probabilite"]


def test_predict_corps_vide(client):
    assert client.post("/predict", json={}).status_code == 422


def test_predict_champ_manquant(client, employe):
    del employe["revenu_mensuel"]
    r = client.post("/predict", json=employe)
    assert r.status_code == 422


def test_predict_valeur_invalide(client, employe):
    employe["age"] = -10
    assert client.post("/predict", json=employe).status_code == 422


def test_predict_type_invalide(client, employe):
    employe["age"] = "trente"
    assert client.post("/predict", json=employe).status_code == 422


def test_erreur_modele_donne_500_et_rien_en_base(client, employe, session, monkeypatch):
    def en_panne(_):
        raise RuntimeError("panne simulée")

    monkeypatch.setattr("app.main.predire", en_panne)
    r = client.post("/predict", json=employe)
    assert r.status_code == 500
    assert session.scalar(select(func.count(models.PredictionInput.id))) == 0
    assert session.scalar(select(func.count(models.PredictionOutput.id))) == 0


def test_historique(client, employe):
    client.post("/predict", json=employe)
    client.post("/predict", json=employe)
    r = client.get("/predictions?limite=1")
    assert r.status_code == 200
    assert len(r.json()) == 1


def test_historique_limite_invalide(client):
    assert client.get("/predictions?limite=0").status_code == 422


def test_documentation_swagger(client):
    assert client.get("/docs").status_code == 200
    chemins = client.get("/openapi.json").json()["paths"]
    assert "/predict" in chemins and "/health" in chemins
