# Testaus

[Yksikkötestauksen kattavuusraportti](https://app.codecov.io/gh/realtalin/runogeneraattori)

Trie ja MarkovKetju -luokat, runogeneroijan funktio generoi_runo sekä tokenoijan kaksi funktiota on testattu käyttäen Pythonin unittest-kirjastoa. Testeissä kokeillaan metodeja oikeellisilla, itse keksityillä syötteillä. Testeissä tarkistetaan lopputuloksen oikeellisuus lukuisten väitteiden avulla.

Testit voidaan toistaa komennolla ```poetry run invoke testaa```.