import joblib
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import tensorflow_hub as hub
import tensorflow as tf
import os

os.environ['CUDA_VISIBLE_DEVICES'] = ''    

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
model, X_test_use, y_pred_use, y_mlb, y_train = joblib.load('model/model_use_relog-v5.joblib')
mlb = MultiLabelBinarizer()
y_mlb = mlb.fit_transform(y_train)

def predict_tags(sentence, n_tags_to_display=5):
    """
    Prédit les tags pour une phrase donnée en utilisant les probabilités des tags.

    Args:
        sentence (str): La phrase d'entrée pour laquelle prédire les tags.
        n_tags_to_display (int): Le nombre de tags à afficher. Par défaut, 5.

    Returns:
        list: Une liste des tags prédits pour la phrase d'entrée.
    """
    # Convertir la phrase d'entrée en embedding
    sentence_embedding = embed([sentence])  # Assurez-vous que la phrase est dans une liste

    # Obtenir les probabilités de prédiction
    y_pred_proba = model.predict_proba(sentence_embedding)

    # Créer un dictionnaire des probabilités associées aux tags
    tag_probabilities = {tag: prob for tag, prob in zip(mlb.classes_, y_pred_proba[0])}

    # Trier les tags par probabilité décroissante
    sorted_tags = sorted(tag_probabilities.items(), key=lambda x: x[1], reverse=True)

    # Extraire les n_tags_to_display les plus probables
    top_tags = [tag for tag, prob in sorted_tags[:n_tags_to_display]]

    return top_tags