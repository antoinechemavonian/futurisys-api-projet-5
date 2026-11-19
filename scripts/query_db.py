"""Interroge la base : statistiques du dataset et dernières prédictions.

Usage : python -m scripts.query_db
"""
from sqlalchemy import func, select

from app import models
from app.database import SessionLocal


def main():
    with SessionLocal() as s:
        nb_employes = s.scalar(select(func.count(models.Employe.id)))
        nb_partis = s.scalar(select(func.count(models.Employe.id)).where(models.Employe.a_quitte == 1))
        nb_pred = s.scalar(select(func.count(models.PredictionOutput.id)))
        nb_oui = s.scalar(
            select(func.count(models.PredictionOutput.id)).where(models.PredictionOutput.prediction == "Oui")
        )
        print(f"Employés dans le dataset : {nb_employes} (dont {nb_partis} partis)")
        print(f"Prédictions enregistrées : {nb_pred} (dont {nb_oui} « Oui »)")
        print("Dernières prédictions :")
        requete = (
            select(models.PredictionInput.id, models.PredictionInput.created_at,
                   models.PredictionOutput.prediction, models.PredictionOutput.probabilite)
            .join(models.PredictionOutput, models.PredictionOutput.input_id == models.PredictionInput.id)
            .order_by(models.PredictionInput.id.desc())
            .limit(5)
        )
        for ligne in s.execute(requete):
            print(f"  #{ligne.id}  {ligne.created_at:%Y-%m-%d %H:%M}  {ligne.prediction}  {ligne.probabilite:.3f}")


if __name__ == "__main__":
    main()
