from tkinter import ttk, StringVar, constants
from services.main_service import budgeting_service


class BudgetingUI:
    def __init__(self, root, handle_logout):
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout

        self.initialize()

    def show(self):
        self.frame.pack(fill=constants.X)

    def close(self):
        self.frame.destroy()

    def logout_handler(self):
        budgeting_service.logout()
        self.handle_logout()

    def new_budget_input(self):
        label = ttk.Label(master=self.frame, text="New Budget")

        self.enter_budget_name = ttk.Entry(master=self.frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self.enter_budget_name.grid(padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.new_budget_input()

        logout_button = ttk.Button(master=self.frame, text="Logout",
                                        command=self.logout_handler)
        
        logout_button.grid(padx=5, pady=5, sticky=constants.E)

        self.frame.grid_columnconfigure(0, weight=2, minsize=800)
