import os

import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "modele_attrition.joblib"))
MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0.0")

# Le fichier contient : le modèle, la liste ordonnée des colonnes et le seuil de décision.
_objets = joblib.load(MODEL_PATH)
modele = _objets["modele"]
COLONNES = list(_objets["colonnes"])
SEUIL = float(_objets["seuil"])


def predire(variables: dict):
    """Reçoit un dict {nom_colonne_modèle: valeur}. Retourne ("Oui"/"Non", probabilité)."""
    df = pd.DataFrame([variables], columns=COLONNES)
    proba = float(modele.predict_proba(df)[:, 1][0])
    return ("Oui" if proba >= SEUIL else "Non"), proba
