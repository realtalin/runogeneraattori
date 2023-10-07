class TrieSolmu:
    def __init__(self):
        """Alustaa solmun"""
        self.lapset = {}
        self.on_lehtisolmu = False
        self.frekvenssi = 0


class Trie:
    def __init__(self):
        """Alustaa trien tyhjällä aloitussolmulla"""
        self.aloitussolmu = TrieSolmu()

    def lisaa(self, sanajono: list):
        """Lisää trieen yhden sanajonon, joka on lista sanoja"""
        solmu = self.aloitussolmu
        for sana in sanajono:
            if sana not in solmu.lapset:
                solmu.lapset[sana] = TrieSolmu()
            solmu = solmu.lapset[sana]
            solmu.frekvenssi += 1
        solmu.on_lehtisolmu = True

    def hae_lapset(self, sanajono: list):
        """Hakee kaikki sanajonon viimeisen sanan lapset. Jos
           sanajono on tyhjä, palauttaa alkusolmun lapset.
        Args:
            sanajono (list): Lista sanoja

        Returns:
            dict: Sanakirja jossa sana:solmu-pareja
        """
        solmu = self.aloitussolmu
        for sana in sanajono:
            if sana not in solmu.lapset:
                if sana == "":
                    return solmu.lapset
                return False
            solmu = solmu.lapset[sana]
        return solmu.lapset
