# Toteutus

Ohjelma päärakenne koostuu kahdesta pääluokasta Trie ja MarkovKetju.

Triessä on toteutettu Trie-tietorakenne. Trien metodeja ovat solujen lisääminen ja lapsien etsiminen.

MarkovKetju sisältää metodit sanajonojen luomiseen opetusdatasta, sanajonojen tallentamiseen Trieen, seuraavan sanan valitsemisen edellisten perusteella sekä lauseen generoimisen.

Tokenoija-moduulin tokenoi_teksti-apufunktio muuttaa raa'an merkkijonon (esim. romaani) lauseiksi ja sanoiksi, eli tokenoi sen.

Runogeneroija-moduulin funktiot luovat ketjun ja generoivat runoja käyttäjän antamilla parametreilla.

Käyttöliittymä on toteutettu tiedostossa main.py.