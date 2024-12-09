from tkinter import ttk, constants
from services.main_service import budgeting_service


class CreateBudgetUI:
    def __init__(self, root, handle_create_budget):
        self.root = root
        self.frame = None
        self.handle_create_budget = handle_create_budget
        self.enter_name = None
        self.enter_income = None
        self.enter_rent = None
        self.enter_bills = None
        self.enter_hobbies = None
        self.enter_misc = None

        self.initialize()

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def create_budget_handler(self):
        name = str(self.enter_name.get())
        income = float(self.enter_income.get())
        rent = float(self.enter_rent.get())
        bills = float(self.enter_bills.get())
        hobbies = float(self.enter_hobbies.get())
        misc = float(self.enter_misc.get())

        content = {
            "name": name,
            "income": income,
            "rent": rent,
            "bills": bills,
            "hobbies": hobbies,
            "misc": misc
        }
        budgeting_service.create_budget(content)
        self.handle_create_budget()

    def name_input(self):
        label = ttk.Label(master=self.frame, text="Name")

        self.enter_name = ttk.Entry(master=self.frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_name.grid(padx=5, pady=5, sticky=constants.EW)

    # Tuotettu github copilotilla
    def income_input(self):
        label = ttk.Label(master=self.frame, text="Income")
        self.enter_income = ttk.Entry(master=self.frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_income.grid(padx=5, pady=5, sticky=constants.EW)

    def rent_input(self):
        label = ttk.Label(master=self.frame, text="Rent")
        self.enter_rent = ttk.Entry(master=self.frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_rent.grid(padx=5, pady=5, sticky=constants.EW)

    def bills_input(self):
        label = ttk.Label(master=self.frame, text="Bills")
        self.enter_bills = ttk.Entry(master=self.frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_bills.grid(padx=5, pady=5, sticky=constants.EW)

    def hobbies_input(self):
        label = ttk.Label(master=self.frame, text="Hobbies")
        self.enter_hobbies = ttk.Entry(master=self.frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_hobbies.grid(padx=5, pady=5, sticky=constants.EW)

    def misc_input(self):
        label = ttk.Label(master=self.frame, text="Miscellaneous")
        self.enter_misc = ttk.Entry(master=self.frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_misc.grid(padx=5, pady=5, sticky=constants.EW)
    # loppuu

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.name_input()
        self.income_input()
        self.rent_input()
        self.bills_input()
        self.hobbies_input()
        self.misc_input()

        button = ttk.Button(
            master=self.frame, text="Create Budget", command=self.create_budget_handler)
        button.grid(padx=5, pady=5, sticky=constants.EW)

        cancel_button = ttk.Button(master=self.frame, text="Cancel",
                                   command=self.handle_create_budget)
        cancel_button.grid(padx=5, pady=5, sticky=constants.EW)

        self.frame.grid_columnconfigure(0, weight=2, minsize=600)
