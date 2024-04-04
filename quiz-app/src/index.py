from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.title("Quiz Application")

    window.geometry("800x600")
    window.minsize(800, 600)
    window.maxsize(800, 600)

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
