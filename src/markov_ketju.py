import random
import syllables
from trie import Trie


class MarkovKetju:
    """Luokka lauseiden generoimiseen opetusdatasta"""

    def __init__(self, korpus: list, taso: int):
        """Alustaa markov-ketjun

        Parametrit:
            korpus (list): Lista lauseita, jotka ovat itsessään listoja sanoja
            taso (int): Markov-ketjun taso
        """

        self.taso = taso
        self.sanajonojen_pituus = taso + 1
        self.trie = self.__generoi_trie(korpus)

    def __luo_sanajonot(self, korpus):
        """Luo kaikki taso + 1 pitkät sanajonot korpuksen lauseista"""
        sanajonot = []

        for lause in korpus:
            for sanajono in map(
                list, zip(*(lause[i:] for i in range(self.sanajonojen_pituus)))
            ):
                sanajonot.append(sanajono)

        return sanajonot

    def __generoi_trie(self, korpus):
        """Lisää sanajonot trieen"""
        trie = Trie()
        for sanajono in self.__luo_sanajonot(korpus):
            trie.lisaa(sanajono)

        return trie

    def tavuja_lauseessa(self, sanajono: list):
        """Arvioi tavujen määrän engalnninkielisessä lauseessa"""
        tavuja = 0
        for sana in sanajono:
            tavuja += syllables.estimate(sana)
        return tavuja

    def valitse_sana(self, sanajono: list):
        """Valitsee satunnaisesti
        sanajonon viimeisen sanan lapsisolmun

        Parametrit:
            sanajono (list): Lista sanoja (str)

        Palautusarvot:
            False: jos sanajonon viimeinen sana on lehtisolmu
            str: jos sanajonon viimeisellä sanalla on vähintään yksi lapsi
        """
        lapset = self.trie.hae_lapset(sanajono)
        if lapset is False:
            return False

        sana = random.choices(
            list(lapset), weights=[solmu.frekvenssi for solmu in lapset.values()]
        )
        return sana[0]

    def generoi_lause_pituudella(self, pituus):
        """Generoi vakiopituisen lauseen

        Parametrit:
            pituus (int): Lauseen pituus

        Palautusarvo:
            list: Lista sanoista (str), eli lause
        """
        lause = []
        alkutila = [self.valitse_sana([""])]
        for sana in alkutila:
            lause.append(sana)

        for _ in range(pituus - 1):
            seuraava_sana = self.valitse_sana(alkutila)
            if seuraava_sana is False:
                return self.generoi_lause_pituudella(pituus)
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

    def generoi_lause_tavuilla(self, tavuja):
        """Generoi lauseen jossa on tietty määrä tavuja

        Parametrit:
            tavuja (int): Lauseen tavujen määrä

        Palautusarvo:
            list: Lista sanoista (str), eli lause
        """
        lause = []
        alkutila = [self.valitse_sana([""])]
        for sana in alkutila:
            lause.append(sana)

        while True:
            seuraava_sana = self.valitse_sana(alkutila)
            if seuraava_sana is False:
                return self.generoi_lause_tavuilla(tavuja)
            lause.append(seuraava_sana)

            if len(alkutila) >= self.taso:
                uusi_tila = []
                for sana in alkutila[1:]:
                    uusi_tila.append(sana)
            else:
                uusi_tila = alkutila

            uusi_tila.append(seuraava_sana)
            alkutila = uusi_tila

            if self.tavuja_lauseessa(lause) < tavuja:
                continue

            if self.tavuja_lauseessa(lause) == tavuja:
                break

            if self.tavuja_lauseessa(lause) > tavuja:
                return self.generoi_lause_tavuilla(tavuja)

        return lause
