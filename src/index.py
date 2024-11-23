from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Budgeting app")

    show_ui = UI(window)
    show_ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
