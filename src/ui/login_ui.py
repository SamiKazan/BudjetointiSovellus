from tkinter import ttk, constants, StringVar
from services.main_service import budgeting_service


class LoginUI:
    """user interface for logging in
    """
    def __init__(self, root, handle_login, handle_show_create_account_UI):
        """Class construcotr creats login page

        Args:
            root:
                TKinter-element, page view initialization
            handle_login:
                callable, called when trying to login
            _handle_show_create_account_UI:
                callable, shows create_account page on call
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_show_create_account_UI = handle_show_create_account_UI
        self._frame = None
        self._enter_username = None
        self._enter_password = None
        self._message = None
        self._message_label = None

        self.initialize()

    def show(self):
        self._frame.pack(fill=constants.X)

    def close(self):
        self._frame.destroy()

    def login_handler(self):
        username = self._enter_username.get()
        password = self._enter_password.get()

        user = budgeting_service.login(username, password)
        
        if user != None:
            self._handle_login()
        else:
            self.show_message("Wrong username or password")

    def username_input(self):
        label = ttk.Label(master=self._frame, text="Username")

        self._enter_username = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_username.grid(padx=5, pady=5, sticky=constants.EW)

    def password_input(self):
        label = ttk.Label(master=self._frame, text="Password")

        self._enter_password = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._enter_password.grid(padx=5, pady=5, sticky=constants.EW)

    def show_message(self, message):
        self._message.set(message)
        self._message_label.grid()

    def initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.username_input()
        self.password_input()

        self._message = StringVar(self._frame)
        self._message_label = ttk.Label(master=self._frame,
                                        textvariable=self._message)
        self._message_label.grid(padx=5, pady=5)

        # tehty github copilotilla
        login_button = ttk.Button(
            self._frame, text="Login", command=self.login_handler)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        create_user_button = ttk.Button(master=self._frame, text="Dont have Account? Create one here",
                                        command=self._handle_show_create_account_UI)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        # loppuu

        self._frame.grid_columnconfigure(0, weight=2, minsize=800)
