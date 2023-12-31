import string
from os import path
import nltk


nltk_dir = path.join(path.dirname(path.abspath(__file__)), "..", "nltk_data")
nltk.data.path.append(nltk_dir)


def tokenoi_teksti(teksti: str):
    """Tokenoi tekstin

    Parametrit:
        teksti: Opetusdata merkkijonona, esim. kirja.

    Paluuarvo:
        list: Lista listoja (lauseita), jotka sisältävät sanoja (str)
    """
    lauseet = []
    for lause in nltk.sent_tokenize(teksti):
        lause_sanoina = nltk.word_tokenize(lause)
        lauseet.append(lause_sanoina)

    puhdistetut_lauseet = []
    for lause in lauseet:
        puhdas_lause = [
            sana.strip(string.punctuation)
            for sana in lause
            if len(sana.strip(string.punctuation)) > 0
        ]
        puhdistetut_lauseet.append(puhdas_lause)

    return puhdistetut_lauseet
