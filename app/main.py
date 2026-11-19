from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models
from app.database import Base, engine, get_session
from app.ml import MODEL_VERSION, SEUIL, predire
from app.schemas import EmployeInput, HistoriqueItem, PredictionResponse
from app.security import verifier_cle_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield


app = FastAPI(
    title="API Attrition TechNova",
    description=(
        "Prédit si un employé risque de quitter l'entreprise. "
        "Chaque requête et chaque prédiction sont enregistrées en base. "
        "Authentification : en-tête `X-API-Key` (si la variable API_KEY est définie)."
    ),
    version=MODEL_VERSION,
    lifespan=lifespan,
)


@app.get("/health", tags=["Supervision"], summary="Vérifier que l'API est prête")
def health():
    return {"status": "ok", "modele_charge": True, "version": MODEL_VERSION}


@app.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Prédiction"],
    summary="Obtenir une prédiction d'attrition",
    dependencies=[Depends(verifier_cle_api)],
    responses={401: {"description": "Clé d'API manquante ou invalide"},
               422: {"description": "Données invalides"},
               500: {"description": "Erreur interne du modèle"}},
)
def predict(employe: EmployeInput, session: Session = Depends(get_session)):
    entree = models.PredictionInput(features=employe.model_dump())
    session.add(entree)
    session.flush()
    try:
        prediction, proba = predire(employe.vers_modele())
    except Exception:
        session.rollback()
        raise HTTPException(status_code=500, detail="Erreur lors de la prédiction")
    session.add(models.PredictionOutput(
        input_id=entree.id, prediction=prediction, probabilite=proba,
        seuil=SEUIL, version_modele=MODEL_VERSION,
    ))
    session.commit()
    return PredictionResponse(
        id=entree.id, prediction=prediction, probabilite=proba,
        seuil=SEUIL, version_modele=MODEL_VERSION,
    )


@app.get(
    "/predictions",
    response_model=list[HistoriqueItem],
    tags=["Historique"],
    summary="Dernières prédictions enregistrées",
    dependencies=[Depends(verifier_cle_api)],
)
def historique(limite: int = Query(20, ge=1, le=100), session: Session = Depends(get_session)):
    requete = (
        select(models.PredictionInput, models.PredictionOutput)
        .join(models.PredictionOutput, models.PredictionOutput.input_id == models.PredictionInput.id)
        .order_by(models.PredictionInput.id.desc())
        .limit(limite)
    )
    return [
        HistoriqueItem(id=e.id, date=e.created_at, prediction=s.prediction, probabilite=s.probabilite)
        for e, s in session.execute(requete).all()
    ]
