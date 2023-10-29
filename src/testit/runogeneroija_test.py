import unittest
from unittest.mock import MagicMock
from runogeneroija import generoi_runo_pituudella, generoi_runo_runomitalla


class TestRunogeneroija(unittest.TestCase):
    def setUp(self):
        self.ketju = MagicMock()
        self.ketju.generoi_lause_pituudella = MagicMock(
            return_value=["Minä", "olen", "ihminen"]
        )
        self.ketju.generoi_lause_tavuilla = MagicMock(return_value=["oikea tavumäärä"])

    def test_generoi_yksi_rivi(self):
        runo = generoi_runo_pituudella(self.ketju, 1, 3)

        self.assertEqual(runo, "\nMinä olen ihminen")
        self.ketju.generoi_lause_pituudella.assert_called_with(3)

    def test_generoi_kolme_rivia(self):
        runo = generoi_runo_pituudella(self.ketju, 3, 3)

        self.assertEqual(
            runo, "\nMinä olen ihminen\nMinä olen ihminen\nMinä olen ihminen"
        )
        self.ketju.generoi_lause_pituudella.assert_called_with(3)

    def test_generoi_runomittalla(self):
        runo = generoi_runo_runomitalla(self.ketju, (3, 5, 7))

        self.assertEqual(runo, "\noikea tavumäärä\noikea tavumäärä\noikea tavumäärä")
        self.ketju.generoi_lause_tavuilla.assert_any_call(3)
        self.ketju.generoi_lause_tavuilla.assert_any_call(5)
        self.ketju.generoi_lause_tavuilla.assert_any_call(7)
