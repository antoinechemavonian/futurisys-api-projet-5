import os

# Doit être défini AVANT l'import de l'application.
os.environ.setdefault("DATABASE_URL", "sqlite:///./test_predictions.db")
os.environ.pop("API_KEY", None)

import pytest
from fastapi.testclient import TestClient

from app.database import Base, SessionLocal, engine
from app.main import app
from app.schemas import EXEMPLE_EMPLOYE


@pytest.fixture(autouse=True)
def base_propre():
    """Base vide avant chaque test : les résultats sont reproductibles."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def employe():
    return dict(EXEMPLE_EMPLOYE)


@pytest.fixture
def session():
    s = SessionLocal()
    yield s
    s.close()
