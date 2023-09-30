import unittest

from src.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_luo_tyhja_trie(self):
        tyhja_trie = Trie()

        self.assertEqual(len(tyhja_trie.aloitussolmu.lapset), 0)
        self.assertEqual(tyhja_trie.aloitussolmu.frekvenssi, 0)

    def test_lisaa_yksi_sanapari(self):
        sanapari = ['Minä', 'olen']
        self.trie.lisaa(sanapari)

        self.assertTrue('Minä' in self.trie.aloitussolmu.lapset)
        self.assertTrue('olen' not in self.trie.aloitussolmu.lapset)
        self.assertTrue('olen' in self.trie.aloitussolmu.lapset['Minä'].lapset)
        self.assertEqual(self.trie.aloitussolmu.lapset['Minä'].frekvenssi, 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['olen'].frekvenssi, 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['olen'].on_lehtisolmu, True)

    def test_lisaa_yksi_sanakolmikko(self):
        sanakolmikko = ['Minä', 'olen', 'ihminen']
        self.trie.lisaa(sanakolmikko)

        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['olen'].lapset['ihminen'].frekvenssi, 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['olen'].lapset['ihminen'].on_lehtisolmu, True)

    def test_lisaa_kaksi_sanaparia_ei_paallekkaisyyksia(self):
        sanapari_1 = ['Minä', 'olen']
        sanapari_2 = ['Sinä', 'et']
        self.trie.lisaa(sanapari_1)
        self.trie.lisaa(sanapari_2)

        self.assertTrue('Minä' in self.trie.aloitussolmu.lapset)
        self.assertTrue('Sinä' in self.trie.aloitussolmu.lapset)
        self.assertTrue('olen' in self.trie.aloitussolmu.lapset['Minä'].lapset)
        self.assertTrue('et' in self.trie.aloitussolmu.lapset['Sinä'].lapset)
        self.assertTrue(
            'olen' not in self.trie.aloitussolmu.lapset['Sinä'].lapset)
        self.assertTrue(
            'et' not in self.trie.aloitussolmu.lapset['Minä'].lapset)

    def test_lisaa_kaksi_sanaparia_yksi_paallekkaisuus(self):
        sanapari_1 = ['Minä', 'olen']
        sanapari_2 = ['Minä', 'en']
        self.trie.lisaa(sanapari_1)
        self.trie.lisaa(sanapari_2)

        self.assertEqual(len(self.trie.aloitussolmu.lapset), 1)
        self.assertEqual(self.trie.aloitussolmu.lapset['Minä'].frekvenssi, 2)
        self.assertEqual(len(self.trie.aloitussolmu.lapset['Minä'].lapset), 2)
        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['olen'].frekvenssi, 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['en'].frekvenssi, 1)

    def test_lisaa_kaksi_sanaparia_kaksi_paallekkaisyytta(self):
        sanapari_1 = ['Minä', 'olen']
        sanapari_2 = ['Minä', 'olen']
        self.trie.lisaa(sanapari_1)
        self.trie.lisaa(sanapari_2)

        self.assertEqual(len(self.trie.aloitussolmu.lapset), 1)
        self.assertEqual(self.trie.aloitussolmu.lapset['Minä'].frekvenssi, 2)
        self.assertEqual(len(self.trie.aloitussolmu.lapset['Minä'].lapset), 1)
        self.assertEqual(
            self.trie.aloitussolmu.lapset['Minä'].lapset['olen'].frekvenssi, 2)
