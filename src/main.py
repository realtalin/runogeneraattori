from os import path
import nltk
from simple_term_menu import TerminalMenu
from runogeneroija import generoi_ketju, generoi_runo


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
        "Teksti: ",
        "Markovin ketjun taso: ",
        "Runon pituus: ",
        "Rivien pituus: ",
        "Generoi runo",
        "Lopeta",
    ]

    tekstit = [
        "Emma, Jane Austen",
        "Moby-Dick, Herman Melville",
        "Hamlet, William Shakespeare",
    ]

    menu = TerminalMenu(asetukset)
    teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")

    while True:
        menu_valinta = menu.show()

        if menu_valinta == 0:
            tekstimenu = TerminalMenu(tekstit)
            tekstimenu_valinta = tekstimenu.show()

            if tekstimenu_valinta == 0:
                teksti = nltk.corpus.gutenberg.raw("austen-sense.txt")

            elif tekstimenu_valinta == 1:
                teksti = nltk.corpus.gutenberg.raw("melville-moby_dick.txt")

            elif tekstimenu_valinta == 2:
                teksti = nltk.corpus.gutenberg.raw("shakespeare-hamlet.txt")

            asetukset[0] = f"Teksti: {tekstit[tekstimenu_valinta]}"
            menu = TerminalMenu(asetukset)

        if menu_valinta == 1:
            taso = pyyda_numero("Markovin ketjun taso (1-6): ", 1, 6)
            ketju = generoi_ketju(teksti, taso)

            asetukset[1] = f"Markovin ketjun taso: {taso}"
            menu = TerminalMenu(asetukset)

        if menu_valinta == 2:
            riveja = pyyda_numero(
                "Runon pituus (1-100): ",
                1,
                100,
            )

            asetukset[2] = f"Runon pituus: {riveja}"
            menu = TerminalMenu(asetukset)

        if menu_valinta == 3:
            rivin_pituus = pyyda_numero(
                "Rivien pituus (1-20): ",
                1,
                20,
            )

            asetukset[3] = f"Rivien pituus: {rivin_pituus}"
            menu = TerminalMenu(asetukset)

        if menu_valinta == 4:
            try:
                print(generoi_runo(ketju, riveja, rivin_pituus))
            except UnboundLocalError:
                print(
                    "Valitse ensin teksti, ketjun taso, runon pituus ja rivien pituus"
                )

        if menu_valinta == 5:
            break


if __name__ == "__main__":
    lataa_nltk_data()
    main()
