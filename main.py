import tkinter
from tkinter import ttk


class App(ttk.Frame):
    def convert(self):
        self.valueLabel = ttk.Label(
            self.resultFrame, font=('Ivy 10 bold'), text="1,00 Dólar dos EUA = 0,91777082 Euro")
        self.valueLabel.grid(row=0, column=0, padx=10, pady=10)

    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Creating List
        self.fromMenuList = ["", "USD", "BRL", "EUR"]
        self.toMenuList = ["", "USD", "BRL", "EUR"]

        # Creating Control Variables
        self.fromMenuVariable = tkinter.StringVar(value=self.fromMenuList[1])
        self.toMenuVariable = tkinter.StringVar(value=self.toMenuList[1])

        # Creating Widgets
        self.setupWidgets()

    def setupWidgets(self):
        # First Frame
        self.resultFrame = tkinter.LabelFrame(
            self, font=('Ivy 8 normal'), text="Result Frame")
        self.resultFrame.grid(row=0, column=0, sticky="NEWS", padx=20, pady=5)

        self.valueLabel = ttk.Label(self.resultFrame, text="")
        self.valueLabel.grid(row=0, column=0, padx=10, pady=10)

        # Second Frame
        self.mainFrame = tkinter.LabelFrame(
            self, font=('Ivy 8 normal'), text="Main Frame")
        self.mainFrame.grid(row=1, column=0, sticky="NEWS", padx=20, pady=5)

        self.valueLabel = ttk.Label(
            self.mainFrame, font=('Ivy 8 bold'), text="Value")
        self.valueLabel.grid(row=0, column=0, sticky="W")

        self.valueEntry = ttk.Entry(
            self.mainFrame, font=('Ivy 8 bold'), justify="center")
        self.valueEntry.grid(row=1, column=0)

        self.fromLabel = ttk.Label(
            self.mainFrame, font=('Ivy 8 bold'), text="From")
        self.fromLabel.grid(row=0, column=1, sticky="W")

        self.fromMenu = ttk.OptionMenu(
            self.mainFrame, self.fromMenuVariable, *self.fromMenuList)
        self.fromMenu.grid(row=1, column=1)

        self.toLabel = ttk.Label(
            self.mainFrame, font=('Ivy 8 bold'), text="To")
        self.toLabel.grid(row=0, column=2, sticky="W")

        self.toMenu = ttk.OptionMenu(
            self.mainFrame, self.toMenuVariable, *self.toMenuList)
        self.toMenu.grid(row=1, column=2)

        for widget in self.mainFrame.winfo_children():
            widget.grid_configure(padx=10, pady=2)

        # Third Frame
        self.buttonConvert = ttk.Button(
            self, text="Convert", style="Accent.TButton", command=self.convert)
        self.buttonConvert.grid(
            row=2, column=0, sticky="NEWS", padx=20, pady=10)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Currency Converter")

    app = App(root)
    app.pack()

    # Setting the Theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    root.mainloop()
