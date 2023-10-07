import nltk
from runogeneroija import generoi_ketju, generoi_runo


def main():
    teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")

    try:
        riveja = int(input("Kuinka monta riviä pitkä runo? "))
        pituus = int(input("Runon rivien maksimipituus? "))
        taso = int(input("Monennen tason Markov-ketju? "))

    except ValueError:
        print("Annettu parametri oli väärän tyyppinen: Anna numero")

    else:
        ketju = generoi_ketju(teksti, taso)
        runo = generoi_runo(ketju, riveja, pituus)
        print(runo)


if __name__ == "__main__":
    main()
