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
        self._show_login_page()

    def _hide_current_page(self):
        if self.current_page:
            self.current_page.close()
        self.current_page = None

    def _show_login_page(self):
        self._hide_current_page()
        self.current_page = LoginUI(
            self.root, self._show_budgeting_page, self._show_create_account_page)
        self.current_page.show()

    def _show_create_account_page(self):
        self._hide_current_page()
        self.current_page = CreateaccountUI(
            self.root, self._show_budgeting_page, self._show_login_page)
        self.current_page.show()

    def _show_budgeting_page(self):
        self._hide_current_page()
        self.current_page = BudgetingUI(
            self.root, self._show_login_page, self._show_create_budget_page, self._show_view_deails_page)
        self.current_page.show()

    def _show_create_budget_page(self):
        self._hide_current_page()
        self.current_page = CreateBudgetUI(
            self.root, self._show_budgeting_page)
        self.current_page.show()

    def _show_view_deails_page(self, budget):
        self._hide_current_page()
        self.current_page = ViewBudgetDetailsUI(
            self.root, budget, self._show_budgeting_page)
        self.current_page.show()
