from collections import Counter
import unittest
from markov_ketju import MarkovKetju


class TestMarkovKetju(unittest.TestCase):
    def setUp(self):
        self.korpus = [
            ["Sateen", "jälkeen", "maa", "tuoksuu", "raikkaalta"],
            ["Sateen", "jälkeen", "ilma", "on", "yleensä", "raikas", "ja", "puhdas"],
        ]

    def test_generoi_tason_2_trie(self):
        ketju = MarkovKetju(self.korpus, 2)

        self.assertEqual(len(ketju.trie.aloitussolmu.lapset), 7)

        self.assertEqual(ketju.trie.aloitussolmu.lapset["Sateen"].frekvenssi, 2)
        self.assertEqual(ketju.trie.aloitussolmu.lapset["jälkeen"].frekvenssi, 2)

        self.assertEqual(ketju.trie.aloitussolmu.lapset["maa"].frekvenssi, 1)
        self.assertEqual(ketju.trie.aloitussolmu.lapset["raikas"].frekvenssi, 1)

        self.assertEqual(
            ketju.trie.aloitussolmu.lapset["Sateen"].lapset["jälkeen"].frekvenssi, 2
        )

        self.assertTrue("tuoksuu" not in ketju.trie.aloitussolmu.lapset)
        self.assertTrue("puhdas" not in ketju.trie.aloitussolmu.lapset)

        self.assertTrue(
            ketju.trie.aloitussolmu.lapset["ilma"]
            .lapset["on"]
            .lapset["yleensä"]
            .on_lehtisolmu
        )
        self.assertTrue(
            ketju.trie.aloitussolmu.lapset["maa"]
            .lapset["tuoksuu"]
            .lapset["raikkaalta"]
            .on_lehtisolmu
        )

        self.assertEqual(
            ketju.trie.aloitussolmu.lapset["ilma"]
            .lapset["on"]
            .lapset["yleensä"]
            .frekvenssi,
            1,
        )
        self.assertEqual(
            ketju.trie.aloitussolmu.lapset["maa"]
            .lapset["tuoksuu"]
            .lapset["raikkaalta"]
            .frekvenssi,
            1,
        )

    def test_generoi_tason_3_trie(self):
        ketju = MarkovKetju(self.korpus, 3)

        self.assertEqual(len(ketju.trie.aloitussolmu.lapset), 5)

        self.assertTrue("maa" not in ketju.trie.aloitussolmu.lapset)
        self.assertTrue("raikas" not in ketju.trie.aloitussolmu.lapset)
        self.assertTrue("tuoksuu" not in ketju.trie.aloitussolmu.lapset)
        self.assertTrue("puhdas" not in ketju.trie.aloitussolmu.lapset)

        self.assertTrue(
            ketju.trie.aloitussolmu.lapset["ilma"]
            .lapset["on"]
            .lapset["yleensä"]
            .lapset["raikas"]
            .on_lehtisolmu
        )
        self.assertTrue(
            ketju.trie.aloitussolmu.lapset["jälkeen"]
            .lapset["maa"]
            .lapset["tuoksuu"]
            .lapset["raikkaalta"]
            .on_lehtisolmu
        )

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

        self.assertTrue(7400 < maarat["koira"] < 7600)
        self.assertTrue(2400 < maarat["kissa"] < 2600)

    def test_generoi_lause_yksi_sanajono_triessa_oikean_pituinen_lause(self):
        korpus = [["Minä", "olen", "ihminen"]]

        ketju = MarkovKetju(korpus, 2)

        lause = ketju.generoi_lause(3)

        self.assertEqual(lause, ["Minä", "olen", "ihminen"])

    def test_generoi_lause_yksi_sanajono_triessa_lyhyt_lause(self):
        korpus = [["Minä", "olen", "ihminen"]]

        ketju = MarkovKetju(korpus, 2)

        lause = ketju.generoi_lause(2)

        self.assertEqual(lause, ["Minä", "olen"])

    def test_generoi_lauseita_kaksi_sanajonoa_triessa(self):
        korpus = [["Minä", "en", "ole", "ihminen"]]

        ketju = MarkovKetju(korpus, 2)

        lauseet = []

        for _ in range(100):
            lauseet.append(ketju.generoi_lause(3))

        self.assertTrue(["Minä", "en", "ole"] in lauseet)
        self.assertTrue(["en", "ole", "ihminen"] in lauseet)

    def test_tavuja_lauseessa(self):
        ketju = MarkovKetju(self.korpus, 3)

        tavuja_1 = ketju.tavuja_lauseessa(["I", "am", "a", "human"])
        tavuja_2 = ketju.tavuja_lauseessa(["I", "am", "a", "monster"])

        self.assertEqual(tavuja_1, 5)
        self.assertEqual(tavuja_2, 5)
