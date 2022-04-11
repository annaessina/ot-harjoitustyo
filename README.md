# Ohjelmistotekniikka

##  Laskin
Tämän laskimen avulla käyttäjä pystyy laskemaan erilaisia matemaattisia laskuja.

[vaatimusmaarittely.md](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[changelog.md](https://github.com/annaessina/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

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

