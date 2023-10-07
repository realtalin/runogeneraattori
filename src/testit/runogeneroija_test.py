import unittest
from unittest.mock import MagicMock
from runogeneroija import generoi_runo


class TestRunogeneroija(unittest.TestCase):
    def setUp(self):
        self.ketju = MagicMock()
        self.ketju.generoi_lause = MagicMock(return_value=["Minä", "olen", "ihminen"])

    def test_generoi_yksi_rivi(self):
        runo = generoi_runo(self.ketju, 1, 3)

        self.assertEqual(runo, "\nMinä olen ihminen\n")
        self.ketju.generoi_lause.assert_called_with(3)

    def test_generoi_kolme_rivia(self):
        runo = generoi_runo(self.ketju, 3, 3)

        self.assertEqual(
            runo, "\nMinä olen ihminen\nMinä olen ihminen\nMinä olen ihminen\n"
        )
        self.ketju.generoi_lause.assert_called_with(3)
