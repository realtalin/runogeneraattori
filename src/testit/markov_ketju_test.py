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
        ketju.generoi_trie()

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
        ketju.generoi_trie()

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
