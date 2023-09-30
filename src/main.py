import nltk
from tokenoija import tokenoi_teksti
from markov_ketju import MarkovKetju

if __name__ == "__main__":
    teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")
    tokenoitu_teksti = tokenoi_teksti(teksti)
    ketju = MarkovKetju(tokenoitu_teksti, 3)
    ketju.luo_sanajonot()
    ketju.generoi_trie()
    lause = ketju.generoi_lause(10)

    print(lause)
