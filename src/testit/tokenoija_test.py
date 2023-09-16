import unittest
import nltk

from src.tokenoija import puhdista_teksti, tokenoi_teksti

class TestTokenoija(unittest.TestCase):
    def test_puhdista_teksti(self):
        teksti = "--Tässä tekstissä on (joitain) turhia ""merkkejä""."
        puhdistettu = puhdista_teksti(teksti)
        self.assertEqual(puhdistettu, "Tässä tekstissä on joitain turhia merkkejä.")

    def test_tokenoi_teksti(self):
        nltk.download('punkt')
        teksti = "Eka lause. Toka lause."
        tokenoitu = tokenoi_teksti(teksti)
        self.assertEqual(tokenoitu, [["Eka", "lause", "."], ["Toka", "lause", "."]])
