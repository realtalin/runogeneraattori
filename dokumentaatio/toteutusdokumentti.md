# Toteutus

### Rakenne

Ohjelma päärakenne koostuu kahdesta pääluokasta Trie ja MarkovKetju.

Triessä on toteutettu Trie-tietorakenne. Trien metodeja ovat solujen lisääminen ja lapsien etsiminen.

MarkovKetju sisältää metodit sanajonojen luomiseen opetusdatasta, sanajonojen tallentamiseen Trieen, seuraavan sanan valitsemisen edellisten perusteella sekä lauseen generoimisen.

Tokenoija-moduulin tokenoi_teksti-apufunktio muuttaa raa'an merkkijonon (esim. romaani) lauseiksi ja sanoiksi, eli tokenoi sen.

Runogeneroija-moduulin funktiot luovat Markovin ketjun ja generoivat runoja käyttäjän antamilla parametreilla.

Käyttöliittymä on yksinkertainen terminaalivalikko. Se on toteutettu tiedostossa main.py.

### Jatkokehitettävää

Generoitujen lauseiden laatua voisi parantaa suodattamalla niitä jonkinlaisen esimerkiksi lauseenjäseniä tunnistamalla. Olisi myös kiva jos projektissa olisi mahdollista valita muitakin tekstejä kuin vain englanninkielisiä, parhaassa tapauksessa jopa omia tekstitiedostoja.

Käyttöliittymän toteutus oli hyvin nopea, ja jos sitä haluasi jatkokehittää, olisi järkevää toteuttaa se siistimmin ja modulaarisemmin. Esimerkiksi valikoille kannataisi tehdä oma luokka tai omia luokkia. Myös käyttäjän valintojen validoinnissa on puutteita. Tällä hetkellä ohjelma antaa käyttäjän tehdä asioita väärässä järjestyksessa, jolloin ohjelma kaatuisi ilman try-except-blokkia. Olisi järkevämpää ohjata käyttäjä väkisin tekemään valinnat oikeassa järjestyksessä.

Testit on luotu iteratiivisesti ohjelman kehittyessä, ja jotkut niistä ovat hieman vanhentuneita, vaikkakin toimivia. Testaus olisi selvämpää, jos testejä refaktoroitaisiin ja konsolidoitaisiin.

### Laajat kielimallit

Käytin ChatGPT:tä lauseengenerointialgoritmini `MarkovKetju.generoi_lause()` debuggaamiseen.

### Lähteet

- [AlgoritmaOnline, Text Generation With Markov Chains](https://algoritmaonline.com/text-generating-with-markov-chains/)
- [Bespoyasov A. (2021), Text Generation with Markov Chains](https://bespoyasov.me/blog/text-generation-with-markov-chains/)
- [Clark A. (2011), Find all consecutive sub-sequences of length n in a sequence](https://stackoverflow.com/a/6670974)
- [smci (2017), Change nltk.download() path directory from default ~/ntlk_data](https://stackoverflow.com/a/47082481)
- [Wikipedia, Trie](https://en.wikipedia.org/wiki/Trie)
- [Wikipedia, Markov chain](https://en.wikipedia.org/wiki/Markov_chain)