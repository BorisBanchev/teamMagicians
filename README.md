# TeamMagician

[![CI badge](https://github.com/BorisBanchev/teamMagicians/workflows/CI/badge.svg)](https://github.com/BorisBanchev/teamMagicians/actions)

[Team Product and Sprint Backlog](https://docs.google.com/spreadsheets/d/1M6PnnOBQbmud6kSEFh_Pxoa-kk0jIUnGVv0p_7QD7ms/edit?usp=sharing)

### Definition of done: ###
- Kaikki kyseiseen user storyyn liittyvät hyväksymiskriteerit on täytetty 
- Käyttäjälle näytetään selkeät ja ymmärrettävät virheviestit kaikissa tyypillisimmissä virhetilanteissa.
- Virheviestit vastaavat käyttäjän toimintaa ja ohjaavat käyttäjää korjaamaan ongelman.
- Unit testit ja end-to-end-testit on kirjoitettu ja ne suoritetaan onnistuneesti.
- Testit on automatisoitu.
- README.md sisältää kaikki tarvittavat tiedot ohjelmiston ajamiseen ja käyttöönottoon, kuten:
    - Ohjeet ympäristön asennukseen ja konfigurointiin.
    - Mahdolliset ulkoiset riippuvuudet ja miten ne asentaa.
## Käynnistysohjeet

Kloonaa repositorio omalle koneellesi

```shell
git clone https://github.com/BorisBanchev/teamMagicians.git
```

Siirry oikeaan hakemistoon, johon repositorio kloonattiin

```shell
cd teamMagicians
```

Alusta projekti ja asenna riippuvuudet juurihakemistossa:

```shell
poetry install
```

Luo .env -tiedosto seuraavilla muuttujilla:

```env
DATABASE_URL=<tietokannan osoite>
SECRET_KEY=<salainen-avain>
TEST_ENV=true
```

Käynnistä virtuaaliympäristö:

```shell
poetry shell
```

Luo sovelluksen tietokantataulu (ensimmäisellä käynnistyksellä) ja käynnistä sovellus:

```shell
python3 src/db_helper.py
python3 src/index.py
```
