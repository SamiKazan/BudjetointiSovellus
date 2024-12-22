from tkinter import ttk, constants, StringVar
from services.main_service import budgeting_service


class CreateBudgetUI:
    """user interface for budget creation page"""

    def __init__(self, root, handle_create_budget):
        """Class constructor, creates newbudget page

        Args:
            root:
                TKinter-element, page view initialization
            handle_create_budget:
                callable, creates new budget on call. gets unique id
        """
        self._root = root
        self._frame = None
        self._handle_create_budget = handle_create_budget
        self._enter_name = None
        self._enter_income = None
        self._enter_rent = None
        self._enter_bills = None
        self._enter_hobbies = None
        self._enter_misc = None
        self._message = None
        self._message_label = None

        self.initialize()

    def show(self):
        self._frame.pack(fill=constants.X)

    def close(self):
        self._frame.destroy()

    def create_budget_handler(self):
        if self._enter_name.get() == '':
            self.show_message("Enter title for budget")
            return

        name = str(self._enter_name.get())
        try:
            income = float(self._enter_income.get() or 0)
            rent = float(self._enter_rent.get() or 0)
            bills = float(self._enter_bills.get() or 0)
            hobbies = float(self._enter_hobbies.get() or 0)
            misc = float(self._enter_misc.get() or 0)
        except:
            self.show_message(
                "Income must be a number or use a dot for decimal numbers")
            return

        content = {
            "name": name,
            "income": income,
            "rent": rent,
            "bills": bills,
            "hobbies": hobbies,
            "misc": misc
        }
        budgeting_service.create_budget(content)
        self._handle_create_budget()

    def name_input(self):
        label = ttk.Label(master=self._frame, text="Name")

        self._enter_name = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_name.grid(padx=5, pady=5, sticky=constants.EW)

    # Tuotettu github copilotilla
    def income_input(self):
        label = ttk.Label(master=self._frame, text="Income")
        self._enter_income = ttk.Entry(master=self._frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_income.grid(padx=5, pady=5, sticky=constants.EW)

    def rent_input(self):
        label = ttk.Label(master=self._frame, text="Rent")
        self._enter_rent = ttk.Entry(master=self._frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_rent.grid(padx=5, pady=5, sticky=constants.EW)

    def bills_input(self):
        label = ttk.Label(master=self._frame, text="Bills")
        self._enter_bills = ttk.Entry(master=self._frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_bills.grid(padx=5, pady=5, sticky=constants.EW)

    def hobbies_input(self):
        label = ttk.Label(master=self._frame, text="Hobbies")
        self._enter_hobbies = ttk.Entry(master=self._frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_hobbies.grid(padx=5, pady=5, sticky=constants.EW)

    def misc_input(self):
        label = ttk.Label(master=self._frame, text="Miscellaneous")
        self._enter_misc = ttk.Entry(master=self._frame)
        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_misc.grid(padx=5, pady=5, sticky=constants.EW)
    # loppuu

    def show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.name_input()
        self.income_input()
        self.rent_input()
        self.bills_input()
        self.hobbies_input()
        self.misc_input()

        self._message = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame,
                                        textvariable=self._message)
        self._message_label.grid(padx=5, pady=5)

        button = ttk.Button(
            master=self._frame, text="Create Budget", command=self.create_budget_handler)
        button.grid(padx=5, pady=5, sticky=constants.EW)

        cancel_button = ttk.Button(master=self._frame, text="Cancel",
                                   command=self._handle_create_budget)
        cancel_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=2, minsize=600)
