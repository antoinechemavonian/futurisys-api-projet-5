"""Liste des 47 variables attendues par le modèle.

Chaque ligne : (nom dans l'API et la base, nom exact utilisé à l'entraînement, type).
Les noms de l'API sont en ASCII (sans accents ni espaces) pour rester simples à utiliser.
"""

FEATURES = [
    ("age", "age", "nombre"),
    ("revenu_mensuel", "revenu_mensuel", "nombre"),
    ("nombre_experiences_precedentes", "nombre_experiences_precedentes", "nombre"),
    ("annee_experience_totale", "annee_experience_totale", "nombre"),
    ("annees_dans_l_entreprise", "annees_dans_l_entreprise", "nombre"),
    ("annees_dans_le_poste_actuel", "annees_dans_le_poste_actuel", "nombre"),
    ("satisfaction_employee_environnement", "satisfaction_employee_environnement", "nombre"),
    ("note_evaluation_precedente", "note_evaluation_precedente", "nombre"),
    ("satisfaction_employee_nature_travail", "satisfaction_employee_nature_travail", "nombre"),
    ("satisfaction_employee_equipe", "satisfaction_employee_equipe", "nombre"),
    ("satisfaction_employee_equilibre_pro_perso", "satisfaction_employee_equilibre_pro_perso", "nombre"),
    ("note_evaluation_actuelle", "note_evaluation_actuelle", "nombre"),
    ("heures_supplementaires", "heures_supplementaires", "nombre"),
    ("augmentation_salaire_precedente", "augmentation_salaire_precedente", "nombre"),
    ("nombre_participation_pee", "nombre_participation_pee", "nombre"),
    ("nb_formations_suivies", "nb_formations_suivies", "nombre"),
    ("distance_domicile_travail", "distance_domicile_travail", "nombre"),
    ("niveau_education", "niveau_education", "nombre"),
    ("frequence_deplacement", "frequence_deplacement", "nombre"),
    ("annees_depuis_la_derniere_promotion", "annees_depuis_la_derniere_promotion", "nombre"),
    ("annees_sous_responsable_actuel", "annees_sous_responsable_actuel", "nombre"),
    ("statut_marital_celibataire", "statut_marital_Célibataire", "binaire"),
    ("statut_marital_divorce_e", "statut_marital_Divorcé(e)", "binaire"),
    ("statut_marital_marie_e", "statut_marital_Marié(e)", "binaire"),
    ("departement_commercial", "departement_Commercial", "binaire"),
    ("departement_consulting", "departement_Consulting", "binaire"),
    ("departement_ressources_humaines", "departement_Ressources Humaines", "binaire"),
    ("poste_assistant_de_direction", "poste_Assistant de Direction", "binaire"),
    ("poste_cadre_commercial", "poste_Cadre Commercial", "binaire"),
    ("poste_consultant", "poste_Consultant", "binaire"),
    ("poste_directeur_technique", "poste_Directeur Technique", "binaire"),
    ("poste_manager", "poste_Manager", "binaire"),
    ("poste_representant_commercial", "poste_Représentant Commercial", "binaire"),
    ("poste_ressources_humaines", "poste_Ressources Humaines", "binaire"),
    ("poste_senior_manager", "poste_Senior Manager", "binaire"),
    ("poste_tech_lead", "poste_Tech Lead", "binaire"),
    ("domaine_etude_autre", "domaine_etude_Autre", "binaire"),
    ("domaine_etude_entrepreunariat", "domaine_etude_Entrepreunariat", "binaire"),
    ("domaine_etude_infra_cloud", "domaine_etude_Infra & Cloud", "binaire"),
    ("domaine_etude_marketing", "domaine_etude_Marketing", "binaire"),
    ("domaine_etude_ressources_humaines", "domaine_etude_Ressources Humaines", "binaire"),
    ("domaine_etude_transformation_digitale", "domaine_etude_Transformation Digitale", "binaire"),
    ("satisfaction_moyenne", "satisfaction_moyenne", "nombre"),
    ("evolution_evaluation", "evolution_evaluation", "nombre"),
    ("experience_avant_entreprise", "experience_avant_entreprise", "nombre"),
    ("promotion_sur_anciennete", "promotion_sur_anciennete", "nombre"),
    ("revenu_par_annee_experience", "revenu_par_annee_experience", "nombre"),
]

NOMS_API = [f[0] for f in FEATURES]
NOMS_MODELE = [f[1] for f in FEATURES]
