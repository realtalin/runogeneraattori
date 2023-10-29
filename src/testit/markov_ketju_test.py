from collections import Counter
import unittest
from markov_ketju import MarkovKetju


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        self.korpus = [
            ["Sateen", "jälkeen", "maa", "tuoksuu", "raikkaalta"],
            ["Sateen", "jälkeen", "ilma", "on", "yleensä", "raikas", "ja", "puhdas"],
        ]

    def test_valitse_sana_sanajonolla_ei_lapsia(self):
        ketju = MarkovKetju(self.korpus, 2)

        self.assertFalse(ketju.valitse_sana(["ja", "puhdas"]))
        self.assertFalse(ketju.valitse_sana(["tuoksuu", "raikkaalta"]))

    def test_valitse_sana_sanajonolla_yksi_lapsi(self):
        ketju = MarkovKetju(self.korpus, 2)

        self.assertEqual(ketju.valitse_sana(["raikas", "ja"]), "puhdas")
        self.assertEqual(ketju.valitse_sana(["jälkeen", "maa"]), "tuoksuu")

    def test_valitse_sana_kaksi_mahdollista_valitsee_toisen(self):
        ketju = MarkovKetju(self.korpus, 2)

        valittu_sana = ketju.valitse_sana(["Sateen", "jälkeen"])
        self.assertTrue(valittu_sana in ["maa", "ilma"])

    def test_valitse_sana_kolme_mahdollista_eri_frekvensseilla(self):
        korpus = [
            ["Minä", "olen", "koira"],
            ["Minä", "olen", "koira"],
            ["Minä", "olen", "koira"],
            ["Minä", "olen", "kissa"],
        ]

        ketju = MarkovKetju(korpus, 2)

        valitut_sanat = []

        for _ in range(10000):
            valitut_sanat.append(ketju.valitse_sana(["Minä", "olen"]))

        maarat = Counter(valitut_sanat)

        self.assertTrue(7000 < maarat["koira"] < 8000)
        self.assertTrue(2000 < maarat["kissa"] < 3000)

    def test_generoi_lause_pituudella_yksi_sanajono_triessa_saman_pituinen_lause(self):
        korpus = [["Minä", "olen", "ihminen"]]

        ketju = MarkovKetju(korpus, 2)

        lause = ketju.generoi_lause_pituudella(3)

        self.assertEqual(lause, ["Minä", "olen", "ihminen"])

    def test_generoi_lause_pituudella_yksi_sanajono_triessa_lyhyt_lause(self):
        korpus = [["Minä", "olen", "ihminen"]]

        ketju = MarkovKetju(korpus, 2)

        lause = ketju.generoi_lause_pituudella(2)

        self.assertEqual(lause, ["Minä", "olen"])

    def test_generoi_lauseita_kaksi_sanajonoa_triessa(self):
        korpus = [["Minä", "en", "ole", "ihminen"]]

        ketju = MarkovKetju(korpus, 2)

        lauseet = []

        for _ in range(100):
            lauseet.append(ketju.generoi_lause_pituudella(3))

        self.assertTrue(["Minä", "en", "ole"] in lauseet)
        self.assertTrue(["en", "ole", "ihminen"] in lauseet)

    def test_generoi_lauseita_toinen_sanajono_liian_lyhyt(self):
        korpus = [
            ["Minä", "olen", "ihminen"],
            ["Minä", "olen", "koira", "enkä", "kissa"],
        ]

        ketju = MarkovKetju(korpus, 2)

        lauseet = []

        for _ in range(100):
            lauseet.append(ketju.generoi_lause_pituudella(4))

        self.assertTrue(["Minä", "olen", "ihminen" not in lauseet])
        self.assertTrue(["Minä", "olen", "koira", "enkä"] in lauseet)
        self.assertTrue(["olen", "koira", "enkä", "kissa"] in lauseet)

    def test_tavuja_lauseessa(self):
        ketju = MarkovKetju(self.korpus, 3)

        viisi_tavua = ketju.tavuja_lauseessa(["I", "am", "a", "human"])
        nelja_tavua = ketju.tavuja_lauseessa(["I", "am", "a", "dog"])

        self.assertEqual(viisi_tavua, 5)
        self.assertEqual(nelja_tavua, 4)

    def test_generoi_lause_tavuilla(self):
        korpus = [["I", "am", "a", "human"], ["I", "am", "a", "dog"]]
        ketju = MarkovKetju(korpus, 1)

        viisitavuiset = []
        nelitavuiset = []

        for _ in range(100):
            viisitavuiset.append(ketju.generoi_lause_tavuilla(5))
            nelitavuiset.append(ketju.generoi_lause_tavuilla(4))

        for lause in viisitavuiset:
            self.assertIn(lause, [["I", "am", "a", "human"]])

        for lause in nelitavuiset:
            self.assertIn(lause, [["I", "am", "a", "dog"], ["am", "a", "human"]])
