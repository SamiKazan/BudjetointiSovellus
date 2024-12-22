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

Seuraavat sekvenssikaaviot kuvaavat osan sovelluksen logiikan toiminnallisuudelta.


### Sisäänkirjautumisen sekvenssikaavio
Sovellus etenee seuraavasti, kun syötetään käyttäjätunnus ja salasana sekä painetaan Login:

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant BudgetingService
    participant UserRepository
    
    User->>UI: click login
    UI->>BudgetingService: login("asd", "asd123")
    BudgetingService->>UserRepository: find("asd")
    UserRepository-->>BudgetingService: User
    BudgetingService-->>UI: User
    UI->UI: show_budgeting_page()
```

### Budgtin luomisen sekvenssikaavio

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant BudgetingService
    participant BudgetingRepository

    User ->>UI: click Create new budget
    UI -->>User: opens create new budget page
    User ->>UI: user enters content, click Create Budget
    UI ->>BudgetingService: create_budget(content)
    BudgetingService ->>BudgetingRepository: create_budget(content)
    BudgetingRepository ->BudgetingRepository: id for budget
    BudgetingRepository -->>BudgetingService: 
    BudgetingService -->>UI: 
    UI->UI: show_budgeting_page()
```

### Budgetin poiston sekvenssikaavio

```mermaid
sequenceDiagram
    participant User
    participant UI
    participant BudgetingService
    participant BudgetingRepository

    User ->>UI: click Delete
    UI ->>BudgetingService: delete_budget(budget_id)
    BudgetingService ->>BudgetingRepository: delete_budget(budget_id)
    BudgetingRepository ->BudgetingRepository: delete budget from DB
    BudgetingRepository -->>BudgetingService: 
    BudgetingService -->>UI: 
    UI->UI: show_budgeting_page()
```

### Muut toiminnot
Sovellus toteuttaa muut toiminnot suunnilleen samalla tavalla, jossa käyttöliittymä kutsuu BudgetingServiceä oikealla metodilla, joka sitten kutsuu Budgeting- tai UserRepositorya. Toiminto palaa taas lopulta käyttöliittymään tarvittavilla tiedoilla päivitetyllä näkymällä.

## Ohjelman rakenteeseen jääneet heikkoudet
  - Ohjelman käyttöliittymien metodit message ovat samat jokaisessa, joten siitä olisi voinut tehdä oma luokkansa.
