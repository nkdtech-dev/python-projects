from tkinter import *

window = Tk()
window.title("miles to km converter")
window.minsize(width=300, height=200)
window.config(pady=70)


def conver_miles_km():
    result = int(text.get())*1.609
    equality_lable.config(text=f"is equal to         {result}          kilometer", font=("arial", 15, "bold"))
    equality_lable.config(pady=70)


mile = Label(text="miles", font=("arial", 15, "bold"))
mile.grid(column=2, row=0)

equality_lable = Label(text=f"is equal to         {0}          kilometer", font=("arial", 15, "bold"))
equality_lable.grid(column=1, row=1)

button = Button(text="Calculate", font=("arial", 13, "bold"), command=conver_miles_km)
button.grid(column=1, row=2)
text = Entry()
text.insert(END, string="0")
text.focus()
text.grid(column=1, row=0)
window.mainloop()
