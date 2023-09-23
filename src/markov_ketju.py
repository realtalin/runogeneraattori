from src.trie import Trie

class MarkovKetju():
    def __init__(self, korpus: list, taso: int):
        self.korpus = korpus
        self.sanajonojen_pituus = taso + 1
        self.trie = Trie()

    def luo_sanajonot(self):
        sanajonot = []

        for lause in self.korpus:
            for sanajono in map(list, zip(*(lause[i:] for i in range(self.sanajonojen_pituus)))):
                sanajonot.append(sanajono)

        return sanajonot

    def generoi_trie(self):
        for sanajono in self.luo_sanajonot():
            self.trie.lisaa(sanajono)
