# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraava:

![image](https://github.com/user-attachments/assets/f8f14fc4-437d-43ed-b7c7-84f30612a1c8)

UI sisältää käyttöliittymän, budgetservice sisältää sovelluslogiikan, repositories sisältää koodin tiedontietokantaan tallentamiseen,
entities sisältää luokat, jotka määrittelevät sovelluksen tietokohteita.

## Käyttöliittymä

Käyttöliittymässä on viisi(5) eri näkymää

    - Sisäänkirjautuminen
    - Käyttäjän luominen
    - Budgetointi sovelluksen pää näkymä
    - Budgetin luominen
    - Budgetin tarkastelu

Jokaisesta näkymästä on luotu omat luokkansa. Yksi näkymistä on aina enintään näkyvillä. UI kutsuu ainoastaan budgetservice luokan metodeja.

Sovelluksen pää sivu päivittyy uuden budgetin luodessa, poistaessa tai toisen käyttäjän kirjautuessa.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat Budgetingservice ja User, jotka kuvaavat käyttäjiä ja käyttäjien toimintoja:

```mermaid
 classDiagram
      Budgetingapp "*" --> "1" User
      class User{
          username
          password
      }
      class Budgetingapp{
          id
          budget
          expenses
      }
```

Toiminnoista vastaa luokka BudgetingService olio. Luokka näyttää käyttäliittymän toiminnoille omat metodit, esim:

    login(username, password)
    create_budget(content)
    get_budgets()

Ohjelman kuvaavampi pakkauskaavio:
![image](https://github.com/user-attachments/assets/65508fd2-fba1-427b-be41-e56b60d3e8b7)

## Tietojen pysyväistallennus

Repositories hakemiston luokat BudgetingRepository ja UserRepository hoitavat tietojen tallettamisen. Luokat BudgetingRepository ja UserRepository tallentaa tiedot SQLite-tietokantaan.

Budgetit ja käyttäjät tallennetaan SQLite-tietokannan tauluihin budgets ja users, joka alustetaan [initialize_database.py](https://github.com/SamiKazan/Ohjelmistotekniikka/blob/master/src/initialize_database.py) tiedostossa.

## Päätoiminnot

Seuraavat sekvenssikaaviot kuvaavat sovelluksen logiikan osalta toiminnallisuudelta.


# Sisäänkirjautumisen sekvenssikaavio

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant BudgetService
  participant UserRepository

  User->>UI: click login
  UI->>BudgetService: login("asd", "asd123")
  BudgetService->>UserRepository: find("asd")
  UserRepository-->>BudgetService: User
  BudgetService-->>UI: User
  UI->UI: show_budgeting_page()
```

# Budgtin luomisen sekvenssikaavio

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant BudgetService
  participant UserRepository


```

# Budgetin poiston sekvenssikaavio

```mermaid
sequenceDiagram
  participant User
  participant UI
  participant BudgetService
  participant UserRepository


```

## Ohjelman rakenteeseen jääneet heikkoudet
  - Ohjelman käyttöliittymien metodit message ovat samat jokaisessa, joten siitä olisi voinut tehdä oma luokkansa.