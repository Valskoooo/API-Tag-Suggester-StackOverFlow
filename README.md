# API de Prédiction de Tags

Cette API, développée avec **FastAPI** et **Streamlit**, a pour but de prédire des tags à partir d'une phrase ou d'une question saisie par l'utilisateur. Elle utilise un modèle de machine learning basé sur une régression logistique et un embedding **Universal Sentence Encoder (USE)**.

## Caractéristiques

- **Entraînement** : Le modèle a été entraîné sur un corpus de 50 000 questions et réponses provenant de StackOverflow.
- **Prédiction** : L'API permet de prédire un nombre spécifié de tags à partir d'une entrée textuelle.

## Documentation de l'API

La documentation de l'API est accessible à l'adresse suivante : [http://localhost:8000/docs](http://localhost:8000/docs).

## Prédictions de Tags

Pour prédire des tags, utilisez la page suivante : `/tags`, avec les paramètres suivants :

- `s` : La phrase d'entrée (obligatoire).
- `n` : Le nombre de tags à retourner (obligatoire).

### Exemple de réponse

L'API retourne un JSON contenant :

```json
{
  "phrase": "Votre phrase ici",
  "nombre_de_tags": n,
  "tags_predits": ["tag1", "tag2", "tag3", ...]
}```