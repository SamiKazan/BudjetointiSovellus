from tkinter import ttk, StringVar, constants
from services.main_service import budgeting_service


class BudgetingUI:
    def __init__(self, root, handle_logout, handle_new_budget):
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout
        self.handle_new_budget = handle_new_budget
        self.budget_list_frame = None
        self.budget_list_UI = None

        self.initialize()

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def logout_handler(self):
        budgeting_service.logout()
        self.handle_logout()

    def initialize_budgets(self):
        if self.budget_list_UI:
            self.budget_list_UI.close()
        budgets = budgeting_service.get_budgets()

        self.budget_list_UI = BudgetingListUI(
            self.budget_list_frame,
            budgets
        )
        self.budget_list_UI.show()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.budget_list_frame = ttk.Frame(master=self.frame)

        self.initialize_budgets()

        self.budget_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )
        new_budget_button = ttk.Button(master=self.frame, text="Create new budget",
                                       command=self.handle_new_budget)

        new_budget_button.grid(padx=5, pady=5, sticky=constants.E)

        logout_button = ttk.Button(master=self.frame, text="Logout",
                                   command=self.logout_handler)

        logout_button.grid(padx=5, pady=5, sticky=constants.E)

        self.frame.grid_columnconfigure(0, weight=2, minsize=1000)


class BudgetingListUI:
    def __init__(self, root, budgets):
        self.root = root
        self.budgets = budgets
        self.frame = None

        self.initialize()

    # Lisää VIEW nappi (näyttää kaikki tiedot)
    # Lisää DELETE nappi

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def initialize_budget_item(self, budget):
        item_frame = ttk.Frame(master=self.frame)
        label = ttk.Label(master=item_frame, text=budget.name)

        label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        for budget in self.budgets:
            self.initialize_budget_item(budget)
