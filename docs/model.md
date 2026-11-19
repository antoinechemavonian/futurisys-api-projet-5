# Documentation Technique du Modèle - TechNova

## 1. Objectif métier
Prédire la probabilité qu'un employé quitte l'entreprise (attrition) afin de permettre aux équipes RH de mettre en place des actions de rétention préventives.

## 2. Algorithme et Données
- Algorithme : Random Forest Classifier (optimisé via GridSearch/RandomizedSearch).
- Données d'entraînement : Dataset historique de 1470 employés (SIRH + Évaluations + Sondage).
- Classes : Déséquilibre géré (237 départs pour 1233 non-départs).

## 3. Performances
- Métriques clés : Privilégiant le Recall (pour ne rater aucun départ) et le F1-Score.
- Seuil de décision : Un seuil spécifique (`seuil_final`) a été optimisé lors du Projet 4 pour maximiser la détection des départs sans générer trop de faux positifs.
- Le modèle sauvegardé (`.joblib`) contient le modèle entraîné, la liste des colonnes attendues et le seuil de décision.

## 4. Maintenance et Mise à jour
- Fréquence de ré-entraînement : Recommandé tous les 6 mois pour éviter le "Data Drift" (changement de comportement des employés).
- Protocole : Réexécuter le notebook du Projet 4 avec les données mises à jour, puis remplacer le fichier `modele_attrition.joblib` sur le dépôt Git, puis incrémenter `MODEL_VERSION` et poser un tag Git.
- La version de scikit-learn de `requirements.txt` doit être celle utilisée pour l'entraînement.

## 5. Contrat d'entrée de l'API
- L'API attend les **47 variables** du modèle, toutes obligatoires (voir `app/schemas.py` et l'exemple dans Swagger).
- Les 21 variables binaires (statut marital, département, poste, domaine d'étude) valent 0 ou 1.
- Les variables calculées (`satisfaction_moyenne`, `evolution_evaluation`, `experience_avant_entreprise`, `promotion_sur_anciennete`, `revenu_par_annee_experience`) sont fournies par l'appelant, comme à l'entraînement.
- Une requête incomplète, avec un champ inconnu ou une valeur hors bornes reçoit une erreur 422. Aucune valeur n'est complétée automatiquement.
- Seuil de décision : 0.3331. La prédiction est « Oui » si la probabilité de départ atteint ce seuil.

## 6. Documentation de l'API
L'API FastAPI génère automatiquement une documentation interactive Swagger/OpenAPI. 
Une fois l'API lancée (`uvicorn app.main:app --reload`), elle est accessible sur : `http://localhost:8000/docs`
