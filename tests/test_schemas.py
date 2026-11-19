import pytest
from pydantic import ValidationError

from app.features import NOMS_MODELE
from app.schemas import EXEMPLE_EMPLOYE, EmployeInput


def test_exemple_valide():
    assert EmployeInput(**EXEMPLE_EMPLOYE).age == 35


def test_champ_manquant_refuse(employe):
    del employe["age"]
    with pytest.raises(ValidationError):
        EmployeInput(**employe)


def test_champ_inconnu_refuse(employe):
    employe["salaire_secret"] = 1
    with pytest.raises(ValidationError):
        EmployeInput(**employe)


@pytest.mark.parametrize("champ, valeur", [
    ("age", -5), ("age", 150), ("revenu_mensuel", 0), ("revenu_mensuel", -100),
    ("annees_dans_l_entreprise", -1), ("poste_consultant", 2), ("age", "abc"),
    ("age", float("nan")),
])
def test_valeurs_invalides_refusees(employe, champ, valeur):
    employe[champ] = valeur
    with pytest.raises(ValidationError):
        EmployeInput(**employe)


def test_vers_modele_respecte_les_noms_et_l_ordre():
    valeurs = EmployeInput(**EXEMPLE_EMPLOYE).vers_modele()
    assert list(valeurs.keys()) == NOMS_MODELE
    assert len(valeurs) == 47
