import uuid


class Budgets:
    """Class, that defines a budget

    Attributes:
        user: User object, that defines budgets' owner
        name: string, name of the budget
        id: UUID, unique identifier for the budget
        income: float, monthly income
        rent: float, monthly rent
        bills: float, monthly bills
        hobbies: float, monthly hobbies expenses
        misc: float, miscellaneous monthly expenses
    """

    def __init__(self, user, name, income, rent, bills, hobbies, misc):
        """Class constructor, that creates a new budget.

        Args:
            user: User object, that defines budget's owner.
            name: string, name of the budget.
            income: float, monthly income.
            rent: float, monthly rent.
            bills: float, monthly bills.
            hobbies: float, monthly hobbies expenses.
            misc: float, miscellaneous monthly expenses.
        """
        self.user = user
        self.name = name
        self.id = uuid.uuid4()
        self.income = income
        self.rent = rent
        self.bills = bills
        self.hobbies = hobbies
        self.misc = misc
