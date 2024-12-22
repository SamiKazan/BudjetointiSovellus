from tkinter import ttk, constants, StringVar
from services.main_service import budgeting_service


class BudgetingUI:
    """User interface for showing budgets
    """

    def __init__(self, root, handle_logout, handle_new_budget, handle_view_details):
        """Class constructor, creates budget page view

        Args:
            root:
                TKinter-element, page view initialization
            handle_logout:
                callable, returns to login page, logs user out
            handle_new_budget:
                callable, opens create_budget page
            handle_view_details:
                callable, opens view_budget_details page, passed to other class
        """
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_new_budget = handle_new_budget
        self._budget_list_frame = None
        self._budget_list_UI = None
        self._handle_view_details = handle_view_details
        self._message = None
        self._message_label = None

        self.initialize()

    def show(self):
        self._frame.pack(fill=constants.X)

    def close(self):
        self._frame.destroy()

    def logout_handler(self):
        budgeting_service.logout()
        self._handle_logout()

    def initialize_budgets(self):
        if self._budget_list_UI:
            self._budget_list_UI.close()
        budgets = budgeting_service.get_budgets()

        def refresh_on_delete():
            self.initialize_budgets()

        self._budget_list_UI = BudgetingListUI(
            self._budget_list_frame,
            budgets,
            refresh_on_delete,
            self._handle_view_details,
            self.show_message
        )
        self._budget_list_UI.show()

    def show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._budget_list_frame = ttk.Frame(master=self._frame)

        self.initialize_budgets()

        self._budget_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

        self._message = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame,
                                        textvariable=self._message)
        self._message_label.grid(padx=5, pady=5, sticky=constants.NW)

        new_budget_button = ttk.Button(master=self._frame, text="Create new budget",
                                       command=self._handle_new_budget)
        new_budget_button.grid(row=1, column=0, padx=5,
                               pady=5, sticky=constants.E)

        current_user = ttk.Label(master=self._frame,
                                 text=f"Logged in as {budgeting_service.get_user()}")
        current_user.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)

        logout_button = ttk.Button(master=self._frame, text="Logout",
                                   command=self.logout_handler)
        logout_button.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)

        self._frame.grid_columnconfigure(0, weight=2, minsize=700)


class BudgetingListUI:
    """User interface for showing list of budgets"""

    def __init__(self, root, budgets, refresh_on_delete, handle_view_details, show_message):
        """Class constructor creates list of budgets

        Args:
            root:
                TKinter-element, page view initialization
            budgets:
                list, list of budgets
            refresh_on_delete:
                callable, refreshes page on call
            handle_view_details:
                callable, opens view_budget_details page for specific budget
        """
        self._root = root
        self._budgets = budgets
        self._frame = None
        self._refresh = refresh_on_delete
        self._handle_view_details = handle_view_details
        self._showmessage = show_message

        self.initialize()

    def view_details_handler(self, budget):
        self._handle_view_details(budget)

    def deletion_handler(self, budget_id, budget_name):
        budgeting_service.delete_budget(budget_id)
        self._refresh()
        self._showmessage(f"Deleted: {budget_name}")

    def show(self):
        self._frame.pack(fill=constants.X)

    def close(self):
        self._frame.destroy()

    def initialize_budget_item(self, budget):
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(master=item_frame, text=budget.name)
        label.grid(row=0, column=0, padx=5, pady=10, sticky=constants.W)

        delete_button = ttk.Button(master=item_frame, text="Delete",
                                   command=lambda: self.deletion_handler(budget.id, budget.name))
        delete_button.grid(row=0, column=3, padx=5, pady=5, sticky=constants.E)

        difference = ttk.Label(
            master=item_frame, text=f"Money left over: {budgeting_service.show_difference(budget)}")
        difference.grid(row=0, column=1, padx=5, pady=5, sticky=constants.E)

        details_button = ttk.Button(master=item_frame, text="Details",
                                    command=lambda: self.view_details_handler(budget))
        details_button.grid(row=0, column=2, padx=5,
                            pady=5, sticky=constants.E)

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.grid(row=self._budgets.index(budget),
                        column=0, padx=5, pady=5, sticky=constants.EW)

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for budget in self._budgets:
            self.initialize_budget_item(budget)
