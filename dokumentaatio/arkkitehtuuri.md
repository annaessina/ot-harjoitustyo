# Arkkitehtuuri

UI eli user interface sisältää käyttöliittymän eli ensin sisäänkirjautumissivus, missä käyttäjä voi myös luoda uuden käyttäjän ja sitten laskimensivun. Services sisältää kaikki tarvittavat funktiot, jotta tiedostojen lukeminen ja tallentaminen onnistuisi. Entities sisältää käyttäjätiedoston. Repositories vastaa repositorioista eli tässä tapauksessa sisältää kaiken datan.


![arkkitehtuuri](https://user-images.githubusercontent.com/101710774/163023821-40d78101-b826-49fd-b39a-d57ac3a4d667.png)

## Sovelluslogiikka

Sovelluslogiikassa ilmenee kaksi tietokantaa: record ja user. User-tietokanta sisältää käyttäjän käyttäjätunnuksen sekä salasanan. Record-tietokanta sisältää kaikkien matemaattisten laskujen tulokset.



Seuraavat funktiot tekevät tarvittavat tehtävät käyttäjää varten: login, create_user, delete_user.
Seuraavat funktiot tekevät tarvittavat operaatiot recordsin kanssa: add_new_record, show_all_records, delete_all_records.


## Tietokantaoperaatiot

Kaikki käyttämä data tallentuu kahteen tietokantaan.

# Päätoiminnallisuudet

Käyttäjän luominen:

Uuden käyttäjän tilin luominen toimii alla olevan kuvan mukaisesti.

Sisäänkirjautuminen:

Jo olemassa olevan käyttäjän sisäänkirjautuminen toimii alla olevan kuvan mukaisesti.

Records luominen:

Kun kaikki tarvittavat matemaattiset operaatiot on suoritettu, uuden recordin kirjaaminen ja luominen tietokantaan toimii alla olevan kuvan mukaisesti.
