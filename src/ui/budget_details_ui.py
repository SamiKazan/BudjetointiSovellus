from tkinter import ttk, constants
from services.main_service import budgeting_service


class ViewBudgetDetailsUI:
    """User interface for budget details
    """
    def __init__(self, root, budget, handle_close_page):
        """Class constructor. creates budget details page

        Args:
            root:
                TKinter-element, container for page view
            budget:
                Budgets class, contains budget details
            handle_close_page:
                callable, returns to main app page on call
        """
        self.root = root
        self.frame = None
        self.budget = budget
        self.handle_close_page = handle_close_page

        self.initialize()

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        label = ttk.Label(master=self.frame, text=f"Details of {self.budget.name}")
        label.grid(row=0, column=0, padx=5, pady=8, sticky=constants.W)

        income = ttk.Label(master=self.frame, text=f"Income: {self.budget.income}")
        income.grid(row=1, column=0, padx=5, pady=8, sticky=constants.W)

        rent = ttk.Label(master=self.frame, text=f"Rent: {self.budget.rent}")
        rent.grid(row=2, column=0, padx=5, pady=8, sticky=constants.W)

        bills = ttk.Label(master=self.frame, text=f"Bills: {self.budget.bills}")
        bills.grid(row=3, column=0, padx=5, pady=8, sticky=constants.W)

        hobbies = ttk.Label(master=self.frame, text=f"Hobbies: {self.budget.hobbies}")
        hobbies.grid(row=4, column=0, padx=5, pady=8, sticky=constants.W)

        misc = ttk.Label(master=self.frame, text=f"Miscellaneous: {self.budget.misc}")
        misc.grid(row=5, column=0, padx=5, pady=8, sticky=constants.W)

        difference = ttk.Label(master=self.frame, text=f"Money left over: {budgeting_service.show_difference(self.budget)}")
        difference.grid(row=6, column=0, padx=5, pady=8, sticky=constants.W)

        return_button = ttk.Button(master=self.frame, text="Return",
                                   command=self.handle_close_page)
        return_button.grid(padx=5, pady=5, sticky=constants.E)

        self.frame.grid_columnconfigure(0, weight=2, minsize=600)