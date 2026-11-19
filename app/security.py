import os
import secrets

from fastapi import Header, HTTPException


def verifier_cle_api(x_api_key: str | None = Header(default=None)):
    """Protège les routes par une clé transmise dans l'en-tête X-API-Key.

    La clé attendue vient de la variable d'environnement API_KEY (jamais écrite dans le code).
    Si API_KEY n'est pas définie (développement local), l'accès reste libre.
    """
    cle_attendue = os.getenv("API_KEY")
    if not cle_attendue:
        return
    if x_api_key is None or not secrets.compare_digest(
        x_api_key.encode("utf-8"), cle_attendue.encode("utf-8")
    ):
        raise HTTPException(status_code=401, detail="Clé d'API manquante ou invalide")
