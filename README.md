# Ohjelmistotekniikka

##  Laskin
Tämän laskimen avulla käyttäjä pystyy laskemaan erilaisia matemaattisia laskuja. Käyttäjä pystyy kirjautumaan sisään ja  laskinhistoria jää talteen.

[Vaatimusmäärittely](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

[Releases](https://github.com/annaessina/ot-harjoitustyo/releases)

[Käyttöohje](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/testausdokumentti.md)

## Ohjelman asennus:

Riippuvuuksien asennus:

```bash
poetry install
```

Alusrustoimenpiteiden suorittaminen:

```bash
poetry run invoke build
```

Sovelluksen käynnistys

```bash
poetry run invoke start
```

## Testien suoritus:

```bash
poetry run invoke test
```

## Testikattavuusraportin luominen:

```bash
poetry run invoke coverage-report
```

## Pylint tarkistukset:

```bash
poetry run invoke lint
```

