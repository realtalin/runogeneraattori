import nltk
from runogeneroija import generoi_ketju, generoi_runo


def pyyda_numero(pyynto: str, minimi, maksimi, nolla_lopettaa=False):
    """Pyytää ja validoi käyttäjältä numeron

    Args:
        pyynto (str): Pyyntoteksti
        minimi (int): Minimiarvo
        maksimi (int): Maksimiarvo
        nolla_lopettaa (bool, optional): Kutsuuko annettu 0 pääfunktiota uudelleen. Oletusarvoisesti False.

    Returns:
        arvo: Käyttäjän antama validoitu numero
    """
    while True:
        try:
            arvo = int(input(pyynto))
        except ValueError:
            print("Annettu arvo oli väärän tyyppinen: Anna numero")
            continue

        if nolla_lopettaa:
            if arvo == 0:
                main()

        if arvo < minimi or arvo > maksimi:
            print(f"Anna numero väliltä {minimi}-{maksimi}")
            continue
        break

    return arvo


def main():
    teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")
    taso = pyyda_numero("Monennen tason Markov-ketju? (1-6) ", 1, 6)
    ketju = generoi_ketju(teksti, taso)

    while True:
        riveja = pyyda_numero(
            "Monen rivin runo? (1-100, 0 valitaksesi uusi Markov-ketjun taso) ",
            1,
            100,
            True,
        )

        rivin_pituus = pyyda_numero(
            "Rivien pituus? (1-20) ",
            1,
            20,
        )

        runo = generoi_runo(ketju, riveja, rivin_pituus)
        print(runo)


if __name__ == "__main__":
    main()
