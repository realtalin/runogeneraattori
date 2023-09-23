import re
import nltk



def puhdista_teksti(teksti):
  """Puhdistaa tekstitiedoston jättäen sanat, välilyönnit ja lopetusmerkit."""
  teksti = re.sub(r'[^\w\s.!?]', '', teksti)
  return teksti

def tokenoi_teksti(teksti):
    """"Tokenoi tekstin. Palauttaa Listan listoja (lauseita), jotka koostuvat sanoista sekä pisteistä."""
    lauseet_sanoina = []
    for lause in nltk.sent_tokenize(teksti):
       lause_sanoina = nltk.word_tokenize(lause)
       lauseet_sanoina.append(lause_sanoina)
    return lauseet_sanoina


if __name__ == "__main__":
    sense = nltk.corpus.gutenberg.raw("austen-sense.txt")
    tokenoitu_teksti = tokenoi_teksti(puhdista_teksti(sense))
    print(tokenoitu_teksti)
