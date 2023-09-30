import nltk
from tokenoija import tokenoi_teksti
from markov_ketju import MarkovKetju


def main():
    teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")
    tokenoitu_teksti = tokenoi_teksti(teksti)

    try:
        taso = int(input("Monennen tason Markov-ketju? "))
        pituus = int(input("Lauseiden maksimipituus? "))
        maara = int(input("Kuinka monta lausetta? "))

    except ValueError:
        print("Annettu parametri oli väärän tyyppinen: Anna numero")

    else:

        ketju = MarkovKetju(tokenoitu_teksti, taso)
        ketju.luo_sanajonot()
        ketju.generoi_trie()

        for _ in range(maara):
            print(ketju.generoi_lause(pituus))


if __name__ == "__main__":
    main()
