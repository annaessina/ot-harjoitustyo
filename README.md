# Ohjelmistotekniikka

##  Laskin
Tämän laskimen avulla käyttäjä pystyy laskemaan erilaisia matemaattisia laskuja.

[Vaatimusmäärittely](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Ohjelman asennus:

```bash
poetry install
```

## Ohjelman käynnistäminen:

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

