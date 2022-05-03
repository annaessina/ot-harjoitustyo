# Arkkitehtuuri

UI eli user interface sisältää käyttöliittymän eli ensin sisäänkirjautumissivus, missä käyttäjä voi myös luoda uuden käyttäjän ja sitten laskimensivun. Services sisältää kaikki tarvittavat funktiot, jotta tiedostojen lukeminen ja tallentaminen onnistuisi. Entities sisältää käyttäjätiedoston. Repositories vastaa repositorioista eli tässä tapauksessa sisältää kaiken datan.

![Rakenne](https://user-images.githubusercontent.com/101710774/166513779-64bf1789-6e44-4cef-8f72-2449315c203d.png)


## Sovelluslogiikka

Sovelluslogiikassa ilmenee kaksi tietokantaa: record ja user. User-tietokanta sisältää käyttäjän käyttäjätunnuksen sekä salasanan. Record-tietokanta sisältää kaikkien matemaattisten laskujen tulokset.

![Sovelluslogiikka](https://user-images.githubusercontent.com/101710774/166513872-54635ebc-8855-47a9-b844-08461b8d6ba8.png)


Seuraavat funktiot tekevät tarvittavat tehtävät käyttäjää varten: login, create_user, delete_user.
Seuraavat funktiot tekevät tarvittavat operaatiot recordsin kanssa: add_new_record, show_all_records, delete_all_records.

![sovelluslogiikka2](https://user-images.githubusercontent.com/101710774/166513937-9dbe1853-de2e-46f7-a56f-afa15f15a6e7.png)


## Tietokantaoperaatiot

Kaikki käyttämä data tallentuu kahteen tietokantaan.

# Päätoiminnallisuudet

Käyttäjän luominen:

Uuden käyttäjän tilin luominen toimii alla olevan kuvan mukaisesti.

![Päätoiminnallisuudet(käyttäjän luominen)](https://user-images.githubusercontent.com/101710774/166514038-213ccc31-7410-4ba1-950c-4c3dfbdb451e.png)


Sisäänkirjautuminen:

Jo olemassa olevan käyttäjän sisäänkirjautuminen toimii alla olevan kuvan mukaisesti.

![sisäänkirjautuminen](https://user-images.githubusercontent.com/101710774/166514126-d32b165f-0c7d-472d-96f8-d56f4e052789.png)


Records luominen:

Kun kaikki tarvittavat matemaattiset operaatiot on suoritettu, uuden recordin kirjaaminen ja luominen tietokantaan toimii alla olevan kuvan mukaisesti.

![records_luominen](https://user-images.githubusercontent.com/101710774/166514196-20ce5d2d-ceae-4722-b26e-2df53b64cad8.png)

