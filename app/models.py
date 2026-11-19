from datetime import datetime, timezone

from sqlalchemy import (CheckConstraint, DateTime, Float, ForeignKey, JSON,
                        SmallInteger, String)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


def maintenant():
    return datetime.now(timezone.utc)


class Employe(Base):
    """Dataset : une ligne par employé (variables du modèle + résultat réel connu)."""

    __tablename__ = "employes"
    __table_args__ = (
        CheckConstraint("age >= 16 AND age <= 100", name="ck_employes_age"),
        CheckConstraint("statut_marital_celibataire IN (0, 1)", name="ck_employes_statut_marital_celibataire"),
        CheckConstraint("statut_marital_divorce_e IN (0, 1)", name="ck_employes_statut_marital_divorce_e"),
        CheckConstraint("statut_marital_marie_e IN (0, 1)", name="ck_employes_statut_marital_marie_e"),
        CheckConstraint("departement_commercial IN (0, 1)", name="ck_employes_departement_commercial"),
        CheckConstraint("departement_consulting IN (0, 1)", name="ck_employes_departement_consulting"),
        CheckConstraint("departement_ressources_humaines IN (0, 1)", name="ck_employes_departement_ressources_humaines"),
        CheckConstraint("poste_assistant_de_direction IN (0, 1)", name="ck_employes_poste_assistant_de_direction"),
        CheckConstraint("poste_cadre_commercial IN (0, 1)", name="ck_employes_poste_cadre_commercial"),
        CheckConstraint("poste_consultant IN (0, 1)", name="ck_employes_poste_consultant"),
        CheckConstraint("poste_directeur_technique IN (0, 1)", name="ck_employes_poste_directeur_technique"),
        CheckConstraint("poste_manager IN (0, 1)", name="ck_employes_poste_manager"),
        CheckConstraint("poste_representant_commercial IN (0, 1)", name="ck_employes_poste_representant_commercial"),
        CheckConstraint("poste_ressources_humaines IN (0, 1)", name="ck_employes_poste_ressources_humaines"),
        CheckConstraint("poste_senior_manager IN (0, 1)", name="ck_employes_poste_senior_manager"),
        CheckConstraint("poste_tech_lead IN (0, 1)", name="ck_employes_poste_tech_lead"),
        CheckConstraint("domaine_etude_autre IN (0, 1)", name="ck_employes_domaine_etude_autre"),
        CheckConstraint("domaine_etude_entrepreunariat IN (0, 1)", name="ck_employes_domaine_etude_entrepreunariat"),
        CheckConstraint("domaine_etude_infra_cloud IN (0, 1)", name="ck_employes_domaine_etude_infra_cloud"),
        CheckConstraint("domaine_etude_marketing IN (0, 1)", name="ck_employes_domaine_etude_marketing"),
        CheckConstraint("domaine_etude_ressources_humaines IN (0, 1)", name="ck_employes_domaine_etude_ressources_humaines"),
        CheckConstraint("domaine_etude_transformation_digitale IN (0, 1)", name="ck_employes_domaine_etude_transformation_digitale"),
        CheckConstraint("a_quitte IN (0, 1)", name="ck_employes_a_quitte"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    age: Mapped[float] = mapped_column(Float, nullable=False)
    revenu_mensuel: Mapped[float] = mapped_column(Float, nullable=False)
    nombre_experiences_precedentes: Mapped[float] = mapped_column(Float, nullable=False)
    annee_experience_totale: Mapped[float] = mapped_column(Float, nullable=False)
    annees_dans_l_entreprise: Mapped[float] = mapped_column(Float, nullable=False)
    annees_dans_le_poste_actuel: Mapped[float] = mapped_column(Float, nullable=False)
    satisfaction_employee_environnement: Mapped[float] = mapped_column(Float, nullable=False)
    note_evaluation_precedente: Mapped[float] = mapped_column(Float, nullable=False)
    satisfaction_employee_nature_travail: Mapped[float] = mapped_column(Float, nullable=False)
    satisfaction_employee_equipe: Mapped[float] = mapped_column(Float, nullable=False)
    satisfaction_employee_equilibre_pro_perso: Mapped[float] = mapped_column(Float, nullable=False)
    note_evaluation_actuelle: Mapped[float] = mapped_column(Float, nullable=False)
    heures_supplementaires: Mapped[float] = mapped_column(Float, nullable=False)
    augmentation_salaire_precedente: Mapped[float] = mapped_column(Float, nullable=False)
    nombre_participation_pee: Mapped[float] = mapped_column(Float, nullable=False)
    nb_formations_suivies: Mapped[float] = mapped_column(Float, nullable=False)
    distance_domicile_travail: Mapped[float] = mapped_column(Float, nullable=False)
    niveau_education: Mapped[float] = mapped_column(Float, nullable=False)
    frequence_deplacement: Mapped[float] = mapped_column(Float, nullable=False)
    annees_depuis_la_derniere_promotion: Mapped[float] = mapped_column(Float, nullable=False)
    annees_sous_responsable_actuel: Mapped[float] = mapped_column(Float, nullable=False)
    statut_marital_celibataire: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    statut_marital_divorce_e: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    statut_marital_marie_e: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    departement_commercial: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    departement_consulting: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    departement_ressources_humaines: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_assistant_de_direction: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_cadre_commercial: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_consultant: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_directeur_technique: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_manager: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_representant_commercial: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_ressources_humaines: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_senior_manager: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    poste_tech_lead: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    domaine_etude_autre: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    domaine_etude_entrepreunariat: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    domaine_etude_infra_cloud: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    domaine_etude_marketing: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    domaine_etude_ressources_humaines: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    domaine_etude_transformation_digitale: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    satisfaction_moyenne: Mapped[float] = mapped_column(Float, nullable=False)
    evolution_evaluation: Mapped[float] = mapped_column(Float, nullable=False)
    experience_avant_entreprise: Mapped[float] = mapped_column(Float, nullable=False)
    promotion_sur_anciennete: Mapped[float] = mapped_column(Float, nullable=False)
    revenu_par_annee_experience: Mapped[float] = mapped_column(Float, nullable=False)
    a_quitte: Mapped[int | None] = mapped_column(SmallInteger, nullable=True)


class PredictionInput(Base):
    """Chaque requête reçue par l'API (entrées du modèle)."""

    __tablename__ = "prediction_inputs"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=maintenant, nullable=False
    )
    features: Mapped[dict] = mapped_column(JSON, nullable=False)
    employe_id: Mapped[int | None] = mapped_column(
        ForeignKey("employes.id", ondelete="SET NULL"), nullable=True
    )
    output: Mapped["PredictionOutput"] = relationship(
        back_populates="input", uselist=False, cascade="all, delete-orphan"
    )


class PredictionOutput(Base):
    """Chaque prédiction produite (sorties du modèle), liée à son entrée."""

    __tablename__ = "prediction_outputs"
    __table_args__ = (
        CheckConstraint("prediction IN ('Oui', 'Non')", name="ck_prediction_valeur"),
        CheckConstraint("probabilite >= 0 AND probabilite <= 1", name="ck_probabilite_bornes"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    input_id: Mapped[int] = mapped_column(
        ForeignKey("prediction_inputs.id", ondelete="CASCADE"), unique=True, nullable=False
    )
    prediction: Mapped[str] = mapped_column(String(3), nullable=False)
    probabilite: Mapped[float] = mapped_column(Float, nullable=False)
    seuil: Mapped[float] = mapped_column(Float, nullable=False)
    version_modele: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=maintenant, nullable=False
    )
    input: Mapped["PredictionInput"] = relationship(back_populates="output")
