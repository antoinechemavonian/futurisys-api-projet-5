import pandas as pd

from app import models
from app.features import FEATURES

_OUI = {"oui", "yes", "true", "1", "1.0"}


def _binaire(valeur):
    if isinstance(valeur, str):
        return 1 if valeur.strip().lower() in _OUI else 0
    return int(valeur)


def charger_csv(chemin, session, cible="a_quitte_l_entreprise"):
    """Insère le dataset dans la table employes.

    Le CSV peut utiliser les noms d'entraînement (avec accents) ou les noms de l'API.
    Les lignes avec une valeur manquante sont ignorées.
    Retourne (lignes insérées, lignes ignorées).
    """
    df = pd.read_csv(chemin)
    df = df.rename(columns={original: nom for nom, original, _ in FEATURES})
    noms = [nom for nom, _, _ in FEATURES]
    manquantes = [n for n in noms if n not in df.columns]
    if manquantes:
        raise ValueError(f"Colonnes manquantes dans le CSV : {manquantes}")

    total = len(df)
    df = df.dropna(subset=noms)
    employes = []
    for ligne in df.to_dict(orient="records"):
        valeurs = {}
        for nom, _, kind in FEATURES:
            valeurs[nom] = int(ligne[nom]) if kind == "binaire" else float(ligne[nom])
        brut = ligne.get(cible)
        valeurs["a_quitte"] = None if brut is None or pd.isna(brut) else _binaire(brut)
        employes.append(models.Employe(**valeurs))
    session.add_all(employes)
    session.commit()
    return len(employes), total - len(employes)
