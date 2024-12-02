from tkinter import Tk
from ui.ui import UI

# Login ei toimi kunnolla(tyhjä ruutu vaikka oikeat tiedot)
# create_account päästää appiin vaikka username on jo otettu
# VIIKKO 6 error messaget, poista budgetti,
# näkee budgetin kaikki tiedot(uusi ikkuna), laskee paljon jäljellä


def main():
    window = Tk()
    window.title("Budgeting app")

    show_ui = UI(window)
    show_ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
