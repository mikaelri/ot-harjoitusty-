from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Quiz Application")

    window.geometry("600x400")
    window.minsize(600, 400)
    window.maxsize(600, 400)

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
