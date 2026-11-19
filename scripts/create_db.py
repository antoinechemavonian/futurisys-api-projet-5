"""Crée les tables de la base (PostgreSQL si DATABASE_URL est définie, sinon SQLite).

Usage : python -m scripts.create_db
"""
from sqlalchemy import inspect

from app import models  # noqa: F401  (enregistre les tables)
from app.database import DATABASE_URL, Base, engine


def main():
    Base.metadata.create_all(engine)
    tables = inspect(engine).get_table_names()
    print(f"Base : {engine.url.render_as_string(hide_password=True)}")
    print("Tables créées :", ", ".join(sorted(tables)))


if __name__ == "__main__":
    main()
