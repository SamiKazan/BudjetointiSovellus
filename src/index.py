from tkinter import Tk
from ui.ui import UI

# VIIKKO 6 docstring, sekvenssikaavio
# VIIKKO 7 error messaget, tietoturva/salaus, difference värinvaihto, loput

def main():
    window = Tk()
    window.title("Budgeting app")

    show_ui = UI(window)
    show_ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()
