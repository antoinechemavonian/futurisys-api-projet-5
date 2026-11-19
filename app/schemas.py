from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.features import FEATURES

# Exemple affiché dans Swagger (valeurs indicatives).
EXEMPLE_EMPLOYE = {
    "age": 35,
    "revenu_mensuel": 5000.0,
    "nombre_experiences_precedentes": 2,
    "annee_experience_totale": 10,
    "annees_dans_l_entreprise": 5,
    "annees_dans_le_poste_actuel": 2,
    "satisfaction_employee_environnement": 3,
    "note_evaluation_precedente": 3,
    "satisfaction_employee_nature_travail": 3,
    "satisfaction_employee_equipe": 3,
    "satisfaction_employee_equilibre_pro_perso": 3,
    "note_evaluation_actuelle": 3,
    "heures_supplementaires": 0,
    "augmentation_salaire_precedente": 15.0,
    "nombre_participation_pee": 1,
    "nb_formations_suivies": 2,
    "distance_domicile_travail": 10,
    "niveau_education": 3,
    "frequence_deplacement": 1,
    "annees_depuis_la_derniere_promotion": 1,
    "annees_sous_responsable_actuel": 3,
    "statut_marital_celibataire": 0,
    "statut_marital_divorce_e": 0,
    "statut_marital_marie_e": 1,
    "departement_commercial": 0,
    "departement_consulting": 1,
    "departement_ressources_humaines": 0,
    "poste_assistant_de_direction": 0,
    "poste_cadre_commercial": 0,
    "poste_consultant": 1,
    "poste_directeur_technique": 0,
    "poste_manager": 0,
    "poste_representant_commercial": 0,
    "poste_ressources_humaines": 0,
    "poste_senior_manager": 0,
    "poste_tech_lead": 0,
    "domaine_etude_autre": 0,
    "domaine_etude_entrepreunariat": 0,
    "domaine_etude_infra_cloud": 1,
    "domaine_etude_marketing": 0,
    "domaine_etude_ressources_humaines": 0,
    "domaine_etude_transformation_digitale": 0,
    "satisfaction_moyenne": 3.0,
    "evolution_evaluation": 0.0,
    "experience_avant_entreprise": 5.0,
    "promotion_sur_anciennete": 0.2,
    "revenu_par_annee_experience": 500.0,
}


class EmployeInput(BaseModel):
    """Les 47 variables attendues par le modèle. Aucune n'est facultative."""

    model_config = ConfigDict(extra="forbid", json_schema_extra={"example": EXEMPLE_EMPLOYE})

    age: float = Field(ge=16, le=100, allow_inf_nan=False, description="Âge de l'employé")
    revenu_mensuel: float = Field(gt=0, allow_inf_nan=False, description="Revenu mensuel")
    nombre_experiences_precedentes: float = Field(ge=0, allow_inf_nan=False, description="Variable : nombre_experiences_precedentes")
    annee_experience_totale: float = Field(ge=0, allow_inf_nan=False, description="Variable : annee_experience_totale")
    annees_dans_l_entreprise: float = Field(ge=0, allow_inf_nan=False, description="Variable : annees_dans_l_entreprise")
    annees_dans_le_poste_actuel: float = Field(ge=0, allow_inf_nan=False, description="Variable : annees_dans_le_poste_actuel")
    satisfaction_employee_environnement: float = Field(ge=0, allow_inf_nan=False, description="Variable : satisfaction_employee_environnement")
    note_evaluation_precedente: float = Field(ge=0, allow_inf_nan=False, description="Variable : note_evaluation_precedente")
    satisfaction_employee_nature_travail: float = Field(ge=0, allow_inf_nan=False, description="Variable : satisfaction_employee_nature_travail")
    satisfaction_employee_equipe: float = Field(ge=0, allow_inf_nan=False, description="Variable : satisfaction_employee_equipe")
    satisfaction_employee_equilibre_pro_perso: float = Field(ge=0, allow_inf_nan=False, description="Variable : satisfaction_employee_equilibre_pro_perso")
    note_evaluation_actuelle: float = Field(ge=0, allow_inf_nan=False, description="Variable : note_evaluation_actuelle")
    heures_supplementaires: float = Field(ge=0, allow_inf_nan=False, description="Variable : heures_supplementaires")
    augmentation_salaire_precedente: float = Field(ge=0, allow_inf_nan=False, description="Variable : augmentation_salaire_precedente")
    nombre_participation_pee: float = Field(ge=0, allow_inf_nan=False, description="Variable : nombre_participation_pee")
    nb_formations_suivies: float = Field(ge=0, allow_inf_nan=False, description="Variable : nb_formations_suivies")
    distance_domicile_travail: float = Field(ge=0, allow_inf_nan=False, description="Variable : distance_domicile_travail")
    niveau_education: float = Field(ge=0, allow_inf_nan=False, description="Variable : niveau_education")
    frequence_deplacement: float = Field(ge=0, allow_inf_nan=False, description="Variable : frequence_deplacement")
    annees_depuis_la_derniere_promotion: float = Field(ge=0, allow_inf_nan=False, description="Variable : annees_depuis_la_derniere_promotion")
    annees_sous_responsable_actuel: float = Field(ge=0, allow_inf_nan=False, description="Variable : annees_sous_responsable_actuel")
    statut_marital_celibataire: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : statut_marital_Célibataire")
    statut_marital_divorce_e: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : statut_marital_Divorcé(e)")
    statut_marital_marie_e: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : statut_marital_Marié(e)")
    departement_commercial: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : departement_Commercial")
    departement_consulting: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : departement_Consulting")
    departement_ressources_humaines: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : departement_Ressources Humaines")
    poste_assistant_de_direction: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Assistant de Direction")
    poste_cadre_commercial: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Cadre Commercial")
    poste_consultant: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Consultant")
    poste_directeur_technique: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Directeur Technique")
    poste_manager: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Manager")
    poste_representant_commercial: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Représentant Commercial")
    poste_ressources_humaines: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Ressources Humaines")
    poste_senior_manager: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Senior Manager")
    poste_tech_lead: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : poste_Tech Lead")
    domaine_etude_autre: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : domaine_etude_Autre")
    domaine_etude_entrepreunariat: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : domaine_etude_Entrepreunariat")
    domaine_etude_infra_cloud: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : domaine_etude_Infra & Cloud")
    domaine_etude_marketing: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : domaine_etude_Marketing")
    domaine_etude_ressources_humaines: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : domaine_etude_Ressources Humaines")
    domaine_etude_transformation_digitale: int = Field(ge=0, le=1, description="Indicateur 0 ou 1 : domaine_etude_Transformation Digitale")
    satisfaction_moyenne: float = Field(ge=0, allow_inf_nan=False, description="Variable : satisfaction_moyenne")
    evolution_evaluation: float = Field(allow_inf_nan=False, description="Variable calculée : evolution_evaluation")
    experience_avant_entreprise: float = Field(allow_inf_nan=False, description="Variable calculée : experience_avant_entreprise")
    promotion_sur_anciennete: float = Field(allow_inf_nan=False, description="Variable calculée : promotion_sur_anciennete")
    revenu_par_annee_experience: float = Field(allow_inf_nan=False, description="Variable calculée : revenu_par_annee_experience")

    def vers_modele(self) -> dict:
        """Renvoie les valeurs avec les noms exacts utilisés à l'entraînement."""
        valeurs = self.model_dump()
        return {original: valeurs[nom] for nom, original, _ in FEATURES}


class PredictionResponse(BaseModel):
    id: int
    prediction: str = Field(description='"Oui" si le départ est prévu, sinon "Non"')
    probabilite: float = Field(description="Probabilité de départ (0 à 1)")
    seuil: float = Field(description="Seuil de décision du modèle")
    version_modele: str


class HistoriqueItem(BaseModel):
    id: int
    date: datetime
    prediction: str
    probabilite: float
