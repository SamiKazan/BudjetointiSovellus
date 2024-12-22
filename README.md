# Ohjelmistotekniikka, harjoitustyö

<p><b>Harjoitustyö:</b> <i>Budjetointisovellus</i></p>  

<p>Budjetointisovelluksessa luodaan budjetteja. Budjetin luodessa asetetaan tulot ja kaikki menot lajiteltuna(laskut, harrastukset, yms), josta sitten näkee paljon kulujen jälkeen jää käyttörahaa.</p>  

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/vaatimusmaatittely.md)  

[Työaikakirjanpito](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/arkkitehtuuri.md)

[Changelog](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/changelog.md)

[Käyttöohje](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/kayttoohje.md)

[Testausdokumentaatio](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/dokumentaatio/testaus.md)

## Asennus

1. Asenna riippuvuudet terminaalikomennolla:

    poetry install

2. Suorita alustustoiminpide:

    poetry run invoke build

3.  Käynnistä sovellus:

    poetry run invoke start

## Komentorivi toiminnot

Ohjelman käynnistys:

    poetry run invoke start

Ohjelman testaus:

    poetry run invoke test

Ohjelman testikattavuusraportti:

    poetry run invoke coverage-report

Ohjelman alustus:

    poetry run invoke build

Ohjelman pylint tarkistus:

    poetry run invoke lint

Ohjelman koodin formatointiin:

    poetry run invoke format
