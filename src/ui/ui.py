from ui.login_ui import LoginUI
from ui.create_account_ui import CreateaccountUI


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
            self.root, None, self.show_create_account_page)
        self.current_page.show()

    def show_create_account_page(self):
        self.hide_current_page()
        self.current_page = CreateaccountUI(
            self.root, None, self.show_login_page)
        self.current_page.show()
