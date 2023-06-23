import tkinter
from tkinter import ttk


class app(ttk.Frame):
    def __init__(self, parent):
        return


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Currency Converter")

    # Setting the Theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    root.mainloop()
