def test_sans_cle_quand_la_cle_est_exigee(client, employe, monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-de-test")
    assert client.post("/predict", json=employe).status_code == 401


def test_mauvaise_cle(client, employe, monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-de-test")
    r = client.post("/predict", json=employe, headers={"X-API-Key": "mauvaise"})
    assert r.status_code == 401


def test_bonne_cle(client, employe, monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-de-test")
    r = client.post("/predict", json=employe, headers={"X-API-Key": "secret-de-test"})
    assert r.status_code == 200


def test_historique_protege(client, monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-de-test")
    assert client.get("/predictions").status_code == 401


def test_health_reste_public(client, monkeypatch):
    monkeypatch.setenv("API_KEY", "secret-de-test")
    assert client.get("/health").status_code == 200
