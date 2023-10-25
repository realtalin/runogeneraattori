from os import path
import nltk
from simple_term_menu import TerminalMenu
from runogeneroija import (
    generoi_ketju,
    generoi_runo_pituudella,
    generoi_runo_runomitalla,
)


def lataa_nltk_data():
    """Lataa NLTK-datan kun ohjelma ajetaan ensimmäisen kerran"""
    nltk_dir = path.join(path.dirname(path.abspath(__file__)), "..", "nltk_data")
    nltk.data.path.append(nltk_dir)

    if not path.isdir(nltk_dir):
        nltk.download("punkt", download_dir=nltk_dir)
        nltk.download("gutenberg", download_dir=nltk_dir)


def pyyda_numero(pyynto: str, minimi, maksimi):
    """Pyytää ja validoi käyttäjältä numeron

    Args:
        pyynto (str): Pyyntoteksti
        minimi (int): Minimiarvo
        maksimi (int): Maksimiarvo

    Returns:
        arvo: Käyttäjän antama validoitu numero
    """
    while True:
        try:
            arvo = int(input(pyynto))
        except ValueError:
            print("Annettu arvo oli väärän tyyppinen: Anna numero")
            continue

        if arvo < minimi or arvo > maksimi:
            print(f"Anna numero väliltä {minimi}-{maksimi}")
            continue
        break

    return arvo


def main():
    asetukset = [
        "Lopeta",
        "Generoi runo",
        "Teksti: ",
        "Markovin ketjun taso: ",
        "Runomitta: ",
    ]

    tekstit = [
        "Emma, Jane Austen",
        "Moby-Dick, Herman Melville",
        "Hamlet, William Shakespeare",
    ]

    runomitat = [
        "Vapaa",
        "Haiku",
        "Tanka",
    ]

    paavalikko = TerminalMenu(asetukset)

    while True:
        paavalikko_valinta = paavalikko.show()

        if paavalikko_valinta == 0:
            break

        if paavalikko_valinta == 1:
            try:
                if runomitta is None:
                    print(generoi_runo_pituudella(ketju, riveja, rivin_pituus))

                else:
                    print(generoi_runo_runomitalla(ketju, runomitta))

            except UnboundLocalError:
                print(
                    "Valitse ensin teksti, ketjun taso, runomitta, ja mahdollisesti runon pituus sekä rivien pituus"
                )

        if paavalikko_valinta == 2:
            tekstivalikko = TerminalMenu(tekstit)
            tekstivalikko_valinta = tekstivalikko.show()

            if tekstivalikko_valinta == 0:
                teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")

            if tekstivalikko_valinta == 1:
                teksti = nltk.corpus.gutenberg.raw("melville-moby_dick.txt")

            if tekstivalikko_valinta == 2:
                teksti = nltk.corpus.gutenberg.raw("shakespeare-hamlet.txt")

            asetukset[2] = f"Teksti: {tekstit[tekstivalikko_valinta]}"
            asetukset[3] = "Markovin ketjun taso: "
            taso = None
            ketju = None
            paavalikko = TerminalMenu(asetukset)

        if paavalikko_valinta == 3:
            taso = pyyda_numero("Markovin ketjun taso (1-6): ", 1, 6)
            asetukset[3] = f"Markovin ketjun taso: {taso}"
            try:
                ketju = generoi_ketju(teksti, taso)
            except UnboundLocalError:
                print("Valitse ensin teksti")
                asetukset[3] = "Markovin ketjun taso: "

            paavalikko = TerminalMenu(asetukset)

        if paavalikko_valinta == 4:
            runomittavalikko = TerminalMenu(runomitat)
            runomittavalikko_valinta = runomittavalikko.show()

            if runomittavalikko_valinta == 0:
                runomitta = None
                riveja = None
                rivin_pituus = None
                asetukset.append("Runon pituus: ")
                asetukset.append("Rivien pituus: ")

            if runomittavalikko_valinta == 1:
                runomitta = (5, 7, 5)
                if len(asetukset) > 5:
                    for _ in range(2):
                        asetukset.pop()

            if runomittavalikko_valinta == 2:
                runomitta = (5, 7, 5, 7, 7)
                if len(asetukset) > 5:
                    for _ in range(2):
                        asetukset.pop()

            asetukset[4] = f"Runomitta: {runomitat[runomittavalikko_valinta]}"
            paavalikko = TerminalMenu(asetukset)

        if paavalikko_valinta == 5:
            riveja = pyyda_numero(
                "Runon pituus (1-100 riviä): ",
                1,
                100,
            )

            asetukset[5] = f"Runon pituus: {riveja} riviä"
            paavalikko = TerminalMenu(asetukset)

        if paavalikko_valinta == 6:
            rivin_pituus = pyyda_numero(
                "Rivien pituus (1-20 sanaa): ",
                1,
                20,
            )

            asetukset[6] = f"Rivien pituus: {rivin_pituus} sanaa"
            paavalikko = TerminalMenu(asetukset)


if __name__ == "__main__":
    lataa_nltk_data()
    main()
