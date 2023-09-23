from src.trie import Trie

class MarkovKetju():
    def __init__(self, korpus: list, taso: int):
        """Alustaa markov-ketjun. Ketjulle annetaan korpus, joka on lista lauseita, jotka itsessään ovat listoja sanoja, sekä halutun markov-ketjun taso."""
        self.korpus = korpus
        self.sanajonojen_pituus = taso + 1
        self.trie = Trie()

    def luo_sanajonot(self):
        """Luo kaikki sanajonot sille annetusta korpuksesta. Sanajonojen pituus on markov-ketjun taso + 1."""
        sanajonot = []

        for lause in self.korpus:
            for sanajono in map(list, zip(*(lause[i:] for i in range(self.sanajonojen_pituus)))):
                sanajonot.append(sanajono)

        return sanajonot

    def generoi_trie(self):
        """Lisää sanajonot trieen."""
        for sanajono in self.luo_sanajonot():
            self.trie.lisaa(sanajono)
