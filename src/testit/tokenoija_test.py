import unittest
import nltk
from tokenoija import tokenoi_teksti


class TestTokenoija(unittest.TestCase):
    def test_tokenoi_teksti(self):
        nltk.download('punkt')
        teksti = "Tämä on lause. Tässä lauseessa on--ajatusviiva. Tässä taas \"heittomerkit\"!"
        tokenoitu = tokenoi_teksti(teksti)

        self.assertEqual(tokenoitu, [["Tämä", "on", "lause"], [
                         "Tässä", "lauseessa", "on", "ajatusviiva"], ["Tässä", "taas", "heittomerkit"]])
