from ui.login_ui import LoginUI
from ui.create_account_ui import CreateaccountUI
from ui.budgeting_ui import BudgetingUI
from ui.create_budget_ui import CreateBudgetUI
from ui.budget_details_ui import ViewBudgetDetailsUI


class UI:
    def __init__(self, root):
        self.root = root
        self.current_page = None

    def start(self):
        self.show_login_page()

    def hide_current_page(self):
        if self.current_page:
            self.current_page.close()
        self.current_page = None

    def show_login_page(self):
        self.hide_current_page()
        self.current_page = LoginUI(
            self.root, self.show_budgeting_page, self.show_create_account_page)
        self.current_page.show()

    def show_create_account_page(self):
        self.hide_current_page()
        self.current_page = CreateaccountUI(
            self.root, self.show_budgeting_page, self.show_login_page)
        self.current_page.show()

    def show_budgeting_page(self):
        self.hide_current_page()
        self.current_page = BudgetingUI(
            self.root, self.show_login_page, self.show_create_budget_page, self.show_view_deails_page)
        self.current_page.show()

    def show_create_budget_page(self):
        self.hide_current_page()
        self.current_page = CreateBudgetUI(self.root, self.show_budgeting_page)
        self.current_page.show()

    def show_view_deails_page(self, budget):
        self.hide_current_page()
        self.current_page = ViewBudgetDetailsUI(self.root, budget, self.show_budgeting_page)
        self.current_page.show()
