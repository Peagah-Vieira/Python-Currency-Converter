import requests
import tkinter
from tkinter import ttk


class App(ttk.Frame):
    def convert(self):
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

        fromCurrency = self.fromMenuVariable.get()
        toCurrency = self.toMenuVariable.get()
        amount = self.valueEntry.get()

        querystring = {"from": fromCurrency,
                       "to": toCurrency, "amount": amount}

        headers = {
            "X-RapidAPI-Key": "2b92c53d6cmshf2ab4279c4cd26bp116325jsneeb3fc7daee9",
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        convertedAmount = response.json()

        toStringAmount = str(convertedAmount["result"]["convertedAmount"])

        self.resultLabel['text'] = str(
            amount) + " " + fromCurrency + " = "+toStringAmount + " " + toCurrency

    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Creating List
        self.fromMenuList = ["", "USD", "EUR", "GBP", "CAD", "BRL"]
        self.toMenuList = ["", "EUR", "USD", "GBP", "CAD", "BRL"]

        # Creating Control Variables
        self.fromMenuVariable = tkinter.StringVar(value=self.fromMenuList[1])
        self.toMenuVariable = tkinter.StringVar(value=self.toMenuList[1])

        # Creating Widgets
        self.setupWidgets()

    def setupWidgets(self):
        # First Frame
        self.resultFrame = tkinter.LabelFrame(
            self, font=('Ivy 8 normal'), text="Result Frame")
        self.resultFrame.grid(row=0, column=0, sticky="NEWS", padx=10, pady=5)

        self.resultLabel = ttk.Label(self.resultFrame, text="")
        self.resultLabel.grid(row=0, column=0, padx=10, pady=10)

        # Second Frame
        self.mainFrame = tkinter.LabelFrame(
            self, font=('Ivy 8 normal'), text="Main Frame")
        self.mainFrame.grid(row=1, column=0, sticky="NEWS", padx=10, pady=5)

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
            row=2, column=0, sticky="NEWS", padx=10, pady=10)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Currency Converter")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Setting the Theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    # Setting a minsize and maxsize for the window, and placing in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    root.maxsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) -
                      (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) -
                      (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()
