import random
from trie import Trie


class MarkovKetju():
    def __init__(self, korpus: list, taso: int):
        """Alustaa markov-ketjun

        Parametrit:
            korpus (list): Lista lauseita, jotka ovat itsessään listoja sanoja
            taso (int): Markov-ketjun taso
        """

        self.korpus = korpus
        self.taso = taso
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

    def valitse_sana(self, sanajono: list):
        """Valitsee satunnaisesti frekvenssit painoina sanajonon viimeisen sanan lapsisolmun

        Parametrit:
            sanajono (list): Lista sanoja (str)

        Palautusarvot:
            False: jos sanajonon viimeinen sana on lehtisolmu
            str: jos sanajonon viimeisellä sanalla on vähintään yksi lapsi
        """
        lapset = self.trie.hae_lapset(sanajono)
        if lapset == False:
            return False

        valittu_sana = random.choices(
            list(lapset), weights=[solmu.frekvenssi for solmu in lapset.values()])
        return valittu_sana[0]

    def generoi_lause(self, max_pituus: int):
        """Generoi lauseen käyttämällä luokan trieä

        Parametrit:
            max_pituus (int): Lauseen maksimipituus

        Palautusarvo:
            list: Lista sanoista (str), eli lause
        """
        lause = []
        alkutila = [self.valitse_sana([""])]
        for sana in alkutila:
            lause.append(sana)

        for _ in range(max_pituus - 1):
            seuraava_sana = self.valitse_sana(alkutila)
            if seuraava_sana == False:
                return lause
            lause.append(seuraava_sana)

            if len(alkutila) >= self.taso:
                uusi_tila = []
                for sana in alkutila[1:]:
                    uusi_tila.append(sana)
            else:
                uusi_tila = alkutila

            uusi_tila.append(seuraava_sana)
            alkutila = uusi_tila

        return lause
