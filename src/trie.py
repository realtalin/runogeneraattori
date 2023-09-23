class TrieSolmu:
    def __init__(self):
        """Luo solmun, jolla on kolme atribuuttia. Attribuutteja muutetaan Trien lisaa-metodissa."""
        self.lapset = {}
        self.on_lehtisolmu = False
        self.frekvenssi = 0


class Trie:
    def __init__(self):
        """Alustaa trien tyhjällä aloitussolmulla."""
        self.aloitussolmu = TrieSolmu()

    def lisaa(self, sanajono: list):
        """Lisää trieen yhden sanajonon, joka on lista sanoja."""
        solmu = self.aloitussolmu
        for sana in sanajono:
            if sana not in solmu.lapset:
                solmu.lapset[sana] = TrieSolmu()
            solmu = solmu.lapset[sana]
            solmu.frekvenssi += 1
        solmu.on_lehtisolmu = True
