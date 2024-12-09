from tkinter import Tk
from ui.ui import UI

# VIIKKO 6 error messaget, poista budgetti, docstring
# näkee budgetin kaikki tiedot(uusi ikkuna), laskee paljon jäljellä

def main():
    window = Tk()
    window.title("Budgeting app")

    show_ui = UI(window)
    show_ui.start()

    window.mainloop()

if __name__ == "__main__":
    main()
