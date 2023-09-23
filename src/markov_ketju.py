from src.trie import Trie

class MarkovKetju():
    def __init__(self, korpus: list, taso: int):
        """Alustaa markov-ketjun

        Parametrit:
        korpus: Lista lauseita, jotka ovat itsessään listoja sanoja
        taso: Markov-ketjun taso
        """

        self.korpus = korpus
        self.sanajonojen_pituus = taso + 1
        self.trie = Trie()

    def luo_sanajonot(self):
        """Luo kaikki taso + 1 pitkät sanajonot korpuksen lauseista"""
        sanajonot = []

        for lause in self.korpus:
            for sanajono in map(list, zip(*(lause[i:] for i in range(self.sanajonojen_pituus)))):
                sanajonot.append(sanajono)

        return sanajonot

    def generoi_trie(self):
        """Lisää sanajonot trieen"""
        for sanajono in self.luo_sanajonot():
            self.trie.lisaa(sanajono)
