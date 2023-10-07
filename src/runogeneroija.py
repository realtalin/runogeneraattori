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
    ketju.generoi_trie()

    return ketju


def generoi_runo(ketju, riveja, rivin_pituus):
    """Generoi runon

    Args:
        ketju (MarkovKetju): Markov-ketju, jonka sanajonot ja trie on generoitu
        riveja (int): Rivien määrä
        rivin_pituus (int): Rivien maksimipituus

    Returns:
        str: Runo merkkijonoina rivinvaihtoineen
    """
    lauseet = []
    for _ in range(riveja):
        lauseet.append(ketju.generoi_lause(rivin_pituus))

    lauseet_merkkijonoina = [" ".join(lause) for lause in lauseet]

    runo = "\n"
    for lause in lauseet_merkkijonoina:
        runo += lause + "\n"

    return runo
