from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global rep
    window.after_cancel(timer)
    rep = 0
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1
    if rep == 8:
        count_dodwn(LONG_BREAK_MIN * 60)
        title.config(text="Break", fg=RED)

    elif rep % 2 == 0:
        count_dodwn(SHORT_BREAK_MIN * 60)
        title.config(text="Break", fg=PINK)
    else:
        count_dodwn(WORK_MIN * 60)
        title.config(text="working", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_dodwn(count):
    global rep

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_dodwn, count - 1)
    else:
        start_timer()
        check = ""
        for _ in range(math.floor(rep / 2)):
            check += "🗹"
            check_label.config(text=check, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pamadora")
window.config(pady=50, padx=100, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.grid(row=0, column=1)

check_label = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

star_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
star_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()
