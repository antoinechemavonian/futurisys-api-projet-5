import pandas as pd
import pytest
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError

from app import models
from app.dataset import charger_csv
from app.features import FEATURES
from app.schemas import EXEMPLE_EMPLOYE


def test_predict_enregistre_entree_et_sortie_liees(client, employe, session):
    r = client.post("/predict", json=employe)
    assert r.status_code == 200
    entree = session.get(models.PredictionInput, r.json()["id"])
    assert entree is not None
    assert entree.features["age"] == employe["age"]
    assert entree.output.prediction == r.json()["prediction"]
    assert entree.output.input_id == entree.id


def test_prediction_invalide_refusee_par_la_base(session):
    entree = models.PredictionInput(features={})
    session.add(entree)
    session.flush()
    session.add(models.PredictionOutput(
        input_id=entree.id, prediction="Peu", probabilite=0.5, seuil=0.33, version_modele="1.0.0"))
    with pytest.raises(IntegrityError):
        session.flush()
    session.rollback()


def test_probabilite_hors_bornes_refusee_par_la_base(session):
    entree = models.PredictionInput(features={})
    session.add(entree)
    session.flush()
    session.add(models.PredictionOutput(
        input_id=entree.id, prediction="Oui", probabilite=1.5, seuil=0.33, version_modele="1.0.0"))
    with pytest.raises(IntegrityError):
        session.flush()
    session.rollback()


def test_une_seule_sortie_par_entree(session):
    entree = models.PredictionInput(features={})
    session.add(entree)
    session.flush()
    for _ in range(2):
        session.add(models.PredictionOutput(
            input_id=entree.id, prediction="Non", probabilite=0.1, seuil=0.33, version_modele="1.0.0"))
    with pytest.raises(IntegrityError):
        session.flush()
    session.rollback()


def _csv_dataset(chemin, lignes):
    originaux = {nom: original for nom, original, _ in FEATURES}
    donnees = []
    for ligne in lignes:
        d = {originaux[nom]: valeur for nom, valeur in ligne.items() if nom in originaux}
        d["a_quitte_l_entreprise"] = "Oui"
        donnees.append(d)
    pd.DataFrame(donnees).to_csv(chemin, index=False)


def test_chargement_du_dataset(session, tmp_path):
    chemin = tmp_path / "dataset.csv"
    _csv_dataset(chemin, [dict(EXEMPLE_EMPLOYE), dict(EXEMPLE_EMPLOYE, age=41)])
    inseres, ignores = charger_csv(chemin, session)
    assert (inseres, ignores) == (2, 0)
    assert session.scalar(select(func.count(models.Employe.id))) == 2
    assert session.scalar(select(func.count(models.Employe.id)).where(models.Employe.a_quitte == 1)) == 2


def test_chargement_ignore_les_lignes_incompletes(session, tmp_path):
    chemin = tmp_path / "dataset.csv"
    _csv_dataset(chemin, [dict(EXEMPLE_EMPLOYE), dict(EXEMPLE_EMPLOYE, age=None)])
    inseres, ignores = charger_csv(chemin, session)
    assert (inseres, ignores) == (1, 1)


def test_chargement_refuse_un_csv_incomplet(session, tmp_path):
    chemin = tmp_path / "dataset.csv"
    pd.DataFrame([{"age": 30}]).to_csv(chemin, index=False)
    with pytest.raises(ValueError):
        charger_csv(chemin, session)
