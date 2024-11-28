from entities.budgets import Budgets
from database_connection import get_database_connection

class BudgetingRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_budget(self, budget):
        d_b = self.connection.cursor()

        d_b.execute("""
            insert into budgets
                    (id, user, name, income, rent, groceries, hobbies, misc)
            values (?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            (str(budget.id), budget.user, budget.name, budget.income,
            budget.rent, budget.groceries, budget.hobbies, budget.misc)
        )
        self.connection.commit()

    def find_budgets(self, user):
        budgets = []
        d_b = self.connection.cursor()
        d_b.execute("select * from budgets where user = ?", (user,))
        
        # github copilot auttoi tässä
        rows = d_b.fetchall()
        for row in rows:
            budget = Budgets(
                user= row["user"],
                name= row["name"],
                income= row["income"],
                rent= row["rent"],
                groceries= row["groceries"],
                hobbies= row["hobbies"],
                misc= row["misc"]
            )
            budget.id = row["id"]
            budgets.append(budget)
        return budgets
        # loppuu



budget_repository = BudgetingRepository(get_database_connection())