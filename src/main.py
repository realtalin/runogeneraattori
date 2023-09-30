import nltk
from src.tokenoija import puhdista_teksti, tokenoi_teksti
from src.markov_ketju import MarkovKetju

if __name__ == "__main__":
    teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")
    tokenoitu_teksti = tokenoi_teksti(puhdista_teksti(teksti))
    ketju = MarkovKetju(tokenoitu_teksti, 3)
    ketju.luo_sanajonot()
    ketju.generoi_trie()
    lause = ketju.generoi_lause(10)

    print(lause)