import uuid


class Budgets:
    def __init__(self, user, name, income, rent, groceries, hobbies, misc):
        self.user = user
        self.name = name
        self.id = uuid.uuid4()
        self.income = income
        self.rent = rent
        self.groceries = groceries
        self.hobbies = hobbies
        self.misc = misc
