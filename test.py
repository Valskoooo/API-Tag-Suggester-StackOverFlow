import myfunct

def test_predict_tags():
    sentence = "How to train a model in TensorFlow?"
    n = 5
    assert isinstance(myfunct.predict_tags(sentence, n), list), "La fonction doit retourner une liste."

def test_predict_tags_output():
    sentence = "How to compile a C program using gcc on Ubuntu ?"
    n = 5
    assert myfunct.predict_tags(sentence, n) == ['c','gcc','linux','c++','unix'], "La fonction retourne les tags attendus."
    