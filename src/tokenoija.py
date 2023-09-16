import re
import nltk

sense = nltk.corpus.gutenberg.raw("austen-sense.txt")

def puhdista_teksti(teksti):
  teksti = re.sub(r'[^\w\s.]', '', teksti)
  return teksti

def tokenoi_teksti(teksti):
    lauseet_sanoina = []
    for lause in nltk.sent_tokenize(teksti):
       lause_sanoina = nltk.word_tokenize(lause)
       lauseet_sanoina.append(lause_sanoina)
    return lauseet_sanoina

tokenoitu_teksti = tokenoi_teksti(puhdista_teksti(sense))

print(tokenoitu_teksti)
