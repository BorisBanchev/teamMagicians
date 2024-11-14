## TeamMagician

Team Product and Sprint Backlog: https://docs.google.com/spreadsheets/d/1M6PnnOBQbmud6kSEFh_Pxoa-kk0jIUnGVv0p_7QD7ms/edit?usp=sharing

# käynnistysohjeet

Kloonaa repositorio omalle koneellesi

`git clone https://github.com/BorisBanchev/teamMagicians.git`

Siirry oikeaan hakemistoon, johon repositorio kloonattiin

`cd teamMagicians`

Alusta projekti ja asenna riippuvuudet juurihakemistossa:
`poetry install`

Luo sovellukseen PostgreSQL-tietokanta esim. käyttämällä (https://aiven.io)

Luo .env ympäristö tiedosto seuraavilla muuttujilla:

`DATABASE_URL=<tietokannan osoite>`  
`SECRET_KEY=<salainen-avain>`  
`TEST_ENV=true`

Käynnistä virtuaaliympäristö:
`poetry shell`

Luo sovelluksen tietokantataulu ja käynnistä sovellus:
`python3 src/db_helper.py`
`python3 src/index.py`
