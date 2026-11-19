"""Insère le dataset (CSV) dans la table employes.

Usage : python -m scripts.load_dataset data/dataset_employes.csv --cible a_quitte_l_entreprise
"""
import argparse

from app.database import SessionLocal
from app.dataset import charger_csv


def main():
    parser = argparse.ArgumentParser(description="Charge le dataset dans la base")
    parser.add_argument("csv", help="Chemin du fichier CSV")
    parser.add_argument("--cible", default="a_quitte_l_entreprise",
                        help="Nom de la colonne du résultat réel (facultative)")
    args = parser.parse_args()
    with SessionLocal() as session:
        inseres, ignores = charger_csv(args.csv, session, cible=args.cible)
    print(f"{inseres} employés insérés, {ignores} lignes ignorées (valeurs manquantes)")


if __name__ == "__main__":
    main()
