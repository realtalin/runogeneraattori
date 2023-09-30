import re
import nltk



def puhdista_teksti(teksti):
  """Puhdistaa tekstitiedoston jättäen sanat, välilyönnit ja lauseiden lopetusmerkit."""
  teksti = re.sub(r'[^\w\s.!?]', '', teksti)
  return teksti

def tokenoi_teksti(teksti):
    """Tokenoi tekstin

    Paluuarvo:
        list: Lista listoja (lauseita), jotka sisältävät sanoja (str)
    """
    lauseet_sanoina = []
    for lause in nltk.sent_tokenize(teksti):
       lause_sanoina = nltk.word_tokenize(lause)
       lauseet_sanoina.append(lause_sanoina)
    return lauseet_sanoina
