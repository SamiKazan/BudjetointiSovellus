from entities.budgets import Budgets
from database_connection import get_database_connection


class BudgetingRepository:
    """
    Class for database related budget to operations
    """

    def __init__(self, connection):
        """Class constructor

        ARGS:
            _connection: Connection to databse
        """
        self._connection = connection

    def create_budget(self, budget):
        """Creates new budget for user

        Args:
            budget: An instance of the Budget class containing the budget details.
        """
        d_b = self._connection.cursor()

        d_b.execute("""
            insert into budgets
                    (id, user, name, income, rent, bills, hobbies, misc)
            values (?, ?, ?, ?, ?, ?, ?, ?)
            """,
                    (str(budget.id), budget.user, budget.name, budget.income,
                     budget.rent, budget.bills, budget.hobbies, budget.misc)
                    )
        self._connection.commit()

    def find_budgets(self, user):
        """Returns users' budgets

        Args:
            user: string, users' username

        returns:
            list of budgets
        """
        budgets = []
        d_b = self._connection.cursor()
        d_b.execute("select * from budgets where user = ?", (user,))

        # github copilot auttoi tässä
        rows = d_b.fetchall()
        for row in rows:
            budget = Budgets(
                user=row["user"],
                name=row["name"],
                income=row["income"],
                rent=row["rent"],
                bills=row["bills"],
                hobbies=row["hobbies"],
                misc=row["misc"]
            )
            budget.id = row["id"]
            budgets.append(budget)
        return budgets
        # loppuu

    def delete_budget(self, budget_id):
        """Deletes spesific budget

        Args:
            budget_id: specific budgets id
        """
        d_b = self._connection.cursor()
        d_b.execute("delete from budgets where id = ?", (str(budget_id),))
        self._connection.commit()
        return


budget_repository = BudgetingRepository(get_database_connection())
