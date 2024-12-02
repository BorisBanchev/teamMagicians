Acceptance criterias for modifying a reference:
    - Käyttäjä voi muokata lisäämänsä lähteen tietoja lomakkeella
    - Käyttäjä voi valita peruuta syötettyään uudet tiedot
    - Kun käyttäjä tallentaa muutokset, muutokset tallennetaan tietokantaan
    - Järjestelmä antaa virheviestin, jos muokkaus epäonnistuu

*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos


*** Test Cases ***
