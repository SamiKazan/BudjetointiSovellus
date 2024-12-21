from tkinter import ttk, constants, StringVar
from services.main_service import budgeting_service


class CreateaccountUI:
    """user interface for account creation
    """
    def __init__(self, root, handle_create_user, handle_show_login_UI):
        """Class constructor, creates account creation page.

        Args:
            root:
                TKinter-element, page view initialization
            handle_create_user:
                callable, called on account creation, args: username, password
            handle_show_login_UI:
                callable, shows login page on call
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_UI = handle_show_login_UI
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

    def creation_handler(self):
        username = self._enter_username.get()
        password = self._enter_password.get()

        if len(username) < 3:
            self.show_message("Username must be 3 characters long")
            return
        if len(password) < 5:
            self.show_message("Password must be 5 characters long")
            return

        user = budgeting_service.create_account(username, password)

        if user:
            self._handle_create_user()
        else:
            self.show_message("Username already in use")
            return

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

        create_user_button = ttk.Button(master=self._frame, text="Create user",
                                        command= self.creation_handler)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        cancel_button = ttk.Button(master=self._frame, text="Cancel",
                                   command=self._handle_show_login_UI)
        cancel_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=2, minsize=600)
