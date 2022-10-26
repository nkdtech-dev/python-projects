from tkinter import *

BACKGROND = "#7DE5ED"
CANVAS_COLOR = "#81C6E8"
TEXT_COLOR = "#5837D0"
FONT = ("arial", 13, 'bold')
BUTTON_COLOR = "#5DA7DB"


class GuiFunctions(Tk):
    def __init__(self):
        super().__init__()
        self.title("All in one converter app")
        self.minsize(width=350, height=550)
        self.maxsize(width=350, height=550)
        self.config(padx=10, pady=10, bg=BACKGROND)
        self.canvas = Canvas(width=300, height=500, bg=CANVAS_COLOR, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.currency_button()
        self.weight_button()
        self.length_button()
        self.temperature_button()
        self.area_button()
        self.weight_button()
        self.display_screen()
        self.exit_Button()

    def currency_button(self):
        self.currency = Button(bg=BUTTON_COLOR,
                               text="Currency convertor",
                               fg=TEXT_COLOR, font=FONT,
                               command=self.currency_function)
        self.currency.place(x=80, y=270)

    def weight_button(self):
        self.weight = Button(bg=BUTTON_COLOR, text="Weight convertor", fg=TEXT_COLOR, font=FONT)
        self.weight.place(x=90, y=310)

    def area_button(self):
        self.area = Button(bg=BUTTON_COLOR, text="Area convertor", fg=TEXT_COLOR, font=FONT)
        self.area.place(x=100, y=390)

    def temperature_button(self):
        self.temperature = Button(bg=BUTTON_COLOR, text="temperature convertor", fg=TEXT_COLOR, font=FONT)
        self.temperature.place(x=65, y=230)

    def length_button(self):
        self.length = Button(bg=BUTTON_COLOR, text="length convertor", fg=TEXT_COLOR, font=FONT)
        self.length.place(x=92, y=350)

    def display_screen(self):
        self.display = Canvas(width=250, height=150)
        self.display.place(x=20, y=50)
        self.label = Label(text="All in one converter app",
                           bg=CANVAS_COLOR,
                           fg=TEXT_COLOR,
                           font=("time new roman", 18, "bold"), )
        self.label.place(x=5, y=10)
        self.type1 = Entry(bg=BACKGROND)
        self.type1.place(x=23, y=70, height=25, width=150)
        self.type2 = Entry(bg=BACKGROND)
        self.type2.place(x=23, y=160, height=25, width=150)

    def exit_Button(self):
        exit = Button(bg="red", text="exit", fg=TEXT_COLOR, font=FONT, padx=20)
        exit.place(x=210, y=450)

    def currency_function(self):
        self.label.config(text="Currency converter",
                          bg=CANVAS_COLOR,
                          fg=TEXT_COLOR,
                          font=("time new roman", 18, "bold"), )
