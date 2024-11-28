from tkinter import Tk
from ui.ui import UI

#VIIKKO 5 tee pääsivu, sille DB ja muut toiminnallisuudet
#VIIKKO 6 error messaget näkyville.
#VIIKKO 7 bugfixaus
def main():
    window = Tk()
    window.title("Budgeting app")

    show_ui = UI(window)
    show_ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
