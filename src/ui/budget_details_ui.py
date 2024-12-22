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
        self._root = root
        self._frame = None
        self._budget = budget
        self._handle_close_page = handle_close_page
        self._message = None
        self._message_label = None

        self.initialize()

    def show(self):
        self._frame.pack(fill=constants.X)

    def close(self):
        self._frame.destroy()

    def show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(master=self._frame,
                          text=f"Details of {self._budget.name}")
        label.grid(row=0, column=0, padx=5, pady=8, sticky=constants.W)

        income = ttk.Label(master=self._frame,
                           text=f"Income: {self._budget.income}")
        income.grid(row=1, column=0, padx=5, pady=8, sticky=constants.W)

        rent = ttk.Label(master=self._frame, text=f"Rent: {self._budget.rent}")
        rent.grid(row=2, column=0, padx=5, pady=8, sticky=constants.W)

        bills = ttk.Label(master=self._frame,
                          text=f"Bills: {self._budget.bills}")
        bills.grid(row=3, column=0, padx=5, pady=8, sticky=constants.W)

        hobbies = ttk.Label(master=self._frame,
                            text=f"Hobbies: {self._budget.hobbies}")
        hobbies.grid(row=4, column=0, padx=5, pady=8, sticky=constants.W)

        misc = ttk.Label(master=self._frame,
                         text=f"Miscellaneous: {self._budget.misc}")
        misc.grid(row=5, column=0, padx=5, pady=8, sticky=constants.W)

        difference = ttk.Label(
            master=self._frame, text=f"Money left over: {budgeting_service.show_difference(self._budget)}")
        difference.grid(row=6, column=0, padx=5, pady=8, sticky=constants.W)

        return_button = ttk.Button(master=self._frame, text="Return",
                                   command=self._handle_close_page)
        return_button.grid(padx=5, pady=5, sticky=constants.E)

        self._frame.grid_columnconfigure(0, weight=2, minsize=600)
