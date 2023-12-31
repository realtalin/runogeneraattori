from tokenoija import tokenoi_teksti
from markov_ketju import MarkovKetju


def generoi_ketju(teksti, taso):
    """Generoi MarkovKetju-objektin

    Args:
        teksti (str): Teksti, esim. kokonainen romaani
        taso (int): Markov-ketjun taso

    Returns:
        MarkovKetju: Ketjuobjekti
    """
    tokenoitu_teksti = tokenoi_teksti(teksti)
    ketju = MarkovKetju(tokenoitu_teksti, taso)

    return ketju


def generoi_runo_pituudella(ketju, riveja, rivin_pituus):
    """Generoi runon rivimäärällä ja tietyn pituisilla riveillä

    Args:
        ketju (MarkovKetju): Markov-ketju, jonka sanajonot ja trie on generoitu
        riveja (int): Rivien määrä
        rivin_pituus (int): Rivien pituus

    Returns:
        str: Runo merkkijonona rivinvaihtoineen
    """
    lauseet = []
    for _ in range(riveja):
        lauseet.append(ketju.generoi_lause_pituudella(rivin_pituus))

    return lauseet_runoksi(lauseet)


def generoi_runo_runomitalla(ketju, runomitta: tuple):
    """Generoi runon runomitan mukaan

    Args:
        ketju (MarkovKetju): Markov-ketju, jonka sanajonot ja trie on generoitu
        runomitta (tuple): Tuple, jonka arvot ovat lauseiden tavujen määriä

    Returns:
        str: Runo merkkijonona rivinvaihtoineen
    """
    lauseet = []
    for tavuja in runomitta:
        lauseet.append(ketju.generoi_lause_tavuilla(tavuja))

    return lauseet_runoksi(lauseet)


def lauseet_runoksi(lauseet: list):
    """Luo listasta lauseita runon, joka on yksi merkkijono

    Args:
        lauseet (list): Lista lauseita, jotka ovat listoja sanoja

    Returns:
        str: Runo merkkijonona rivinvaihtoineen
    """
    lauseet_merkkijonoina = [" ".join(lause) for lause in lauseet]

    runo = ""
    for lause in lauseet_merkkijonoina:
        runo += "\n" + lause

    return runo
