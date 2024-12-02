# Arkkitehtuurikuvaus

## Rakenne

![image](https://github.com/user-attachments/assets/f8f14fc4-437d-43ed-b7c7-84f30612a1c8)

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

Pakkauskaavio
![image](https://github.com/user-attachments/assets/65508fd2-fba1-427b-be41-e56b60d3e8b7)
