# Toteutus

Ohjelma päärakenne koostuu kahdesta pääluokasta Trie ja MarkovKetju.

Triessä on toteutettu Trie-tietorakenne. Trien metodeja ovat solujen lisääminen ja lapsien etsiminen.

MarkovKetju sisältää metodit sanajonojen luomiseen opetusdatasta, sanajonojen tallentamiseen Trieen, seuraavan sanan valitsemisen edellisten perusteella sekä lauseen generoimisen.

Tokenoija-moduulin tokenoi_teksti-apufunktio muuttaa raa'an merkkijonon (esim. romaani) lauseiksi ja sanoiksi, eli tokenoi sen.

Runogeneroija-moduulin funktiot luovat ketjun ja generoivat runoja käyttäjän antamilla parametreilla.

Käyttöliittymä on toteutettu tiedostossa main.py.

### Laajat kielimallit

Käytin ChatGPT:tä lauseengenerointialgoritmini `MarkovKetju.generoi_lause()` debuggaamiseen.

### Lähteet

- [AlgoritmaOnline, Text Generation With Markov Chains](https://algoritmaonline.com/text-generating-with-markov-chains/)
- [Bespoyasov A. (2021), Text Generation with Markov Chains](https://bespoyasov.me/blog/text-generation-with-markov-chains/)
- [Clark A. (2011), Find all consecutive sub-sequences of length n in a sequence](https://stackoverflow.com/a/6670974)
- [smci (2017), Change nltk.download() path directory from default ~/ntlk_data](https://stackoverflow.com/a/47082481)
- [Wikipedia, Trie](https://en.wikipedia.org/wiki/Trie)
- [Wikipedia, Markov chain](https://en.wikipedia.org/wiki/Markov_chain)