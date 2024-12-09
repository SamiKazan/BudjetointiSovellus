import uuid

class Budgets:
    def __init__(self, user, name, income, rent, bills, hobbies, misc):
        self.user = user
        self.name = name
        self.id = uuid.uuid4()
        self.income = income
        self.rent = rent
        self.bills = bills
        self.hobbies = hobbies
        self.misc = misc
