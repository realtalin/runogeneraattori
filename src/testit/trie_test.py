import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_luo_tyhja_trie(self):
        tyhja_trie = Trie()

        self.assertEqual(len(tyhja_trie.aloitussolmu.lapset), 0)
        self.assertEqual(tyhja_trie.aloitussolmu.frekvenssi, 0)

    def test_lisaa_yksi_sanapari(self):
        self.trie.lisaa(["Minä", "olen"])

        self.assertTrue("Minä" in self.trie.aloitussolmu.lapset)
        self.assertTrue("olen" not in self.trie.aloitussolmu.lapset)
        self.assertTrue("olen" in self.trie.aloitussolmu.lapset["Minä"].lapset)
        self.assertEqual(self.trie.aloitussolmu.lapset["Minä"].frekvenssi, 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"].lapset["olen"].frekvenssi, 1
        )
        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"].lapset["olen"].on_lehtisolmu, True
        )

    def test_lisaa_yksi_sanakolmikko(self):
        self.trie.lisaa(["Minä", "olen", "ihminen"])

        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"]
            .lapset["olen"]
            .lapset["ihminen"]
            .frekvenssi,
            1,
        )
        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"]
            .lapset["olen"]
            .lapset["ihminen"]
            .on_lehtisolmu,
            True,
        )

    def test_lisaa_kaksi_sanaparia_ei_paallekkaisyyksia(self):
        self.trie.lisaa(["Minä", "olen"])
        self.trie.lisaa(["Sinä", "et"])

        self.assertTrue("Minä" in self.trie.aloitussolmu.lapset)
        self.assertTrue("Sinä" in self.trie.aloitussolmu.lapset)
        self.assertTrue("olen" in self.trie.aloitussolmu.lapset["Minä"].lapset)
        self.assertTrue("et" in self.trie.aloitussolmu.lapset["Sinä"].lapset)
        self.assertTrue("olen" not in self.trie.aloitussolmu.lapset["Sinä"].lapset)
        self.assertTrue("et" not in self.trie.aloitussolmu.lapset["Minä"].lapset)

    def test_lisaa_kaksi_sanaparia_yksi_paallekkaisuus(self):
        self.trie.lisaa(["Minä", "olen"])
        self.trie.lisaa(["Minä", "en"])

        self.assertEqual(len(self.trie.aloitussolmu.lapset), 1)
        self.assertEqual(self.trie.aloitussolmu.lapset["Minä"].frekvenssi, 2)
        self.assertEqual(len(self.trie.aloitussolmu.lapset["Minä"].lapset), 2)
        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"].lapset["olen"].frekvenssi, 1
        )
        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"].lapset["en"].frekvenssi, 1
        )

    def test_lisaa_kaksi_sanaparia_kaksi_paallekkaisyytta(self):
        self.trie.lisaa(["Minä", "olen"])
        self.trie.lisaa(["Minä", "olen"])

        self.assertEqual(len(self.trie.aloitussolmu.lapset), 1)
        self.assertEqual(self.trie.aloitussolmu.lapset["Minä"].frekvenssi, 2)
        self.assertEqual(len(self.trie.aloitussolmu.lapset["Minä"].lapset), 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset["Minä"].lapset["olen"].frekvenssi, 2
        )

    def test_hae_lapset_haettava_sanajono_on(self):
        self.trie.lisaa(["Minä", "olen", "ihminen"])
        self.trie.lisaa(["Minä", "olen", "koira"])
        self.trie.lisaa(["Minä", "olen", "kissa"])

        hakutulos = self.trie.hae_lapset(["Minä", "olen"])

        self.assertTrue("ihminen" in hakutulos)
        self.assertTrue("koira" in hakutulos)
        self.assertTrue("kissa" in hakutulos)
        self.assertEqual(len(hakutulos), 3)

    def test_hae_lapset_haettavaa_sanajonoa_ei_ole(self):
        self.trie.lisaa(["Minä", "olen", "ihminen"])

        mina_hakutulos = self.trie.hae_lapset(["Minä", "en"])
        sina_hakutulos = self.trie.hae_lapset(["Sinä", "olet"])

        self.assertFalse(mina_hakutulos)
        self.assertFalse(sina_hakutulos)

    def test_hae_lapset_tyhjalla_sanajonolla(self):
        self.trie.lisaa(["Minä", "olen", "ihminen"])
        self.trie.lisaa(["Sinä", "olet", "ihminen"])

        hakutulos = self.trie.hae_lapset([""])

        self.assertTrue("Minä" in hakutulos)
        self.assertTrue("Sinä" in hakutulos)
        self.assertEqual(len(hakutulos), 2)