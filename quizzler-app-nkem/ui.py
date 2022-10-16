from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizeBrainInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quize Brain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.right = PhotoImage(file="images/true.png")
        self.wrong = PhotoImage(file="images/false.png")
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="new_question",
            font=("arial", 20, "italic"), fill="black")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.true = Button(image=self.right, bg=THEME_COLOR, highlightthickness=0, command=self.true_press)
        self.true.grid(row=2, column=1)
        self.false = Button(image=self.wrong, bg=THEME_COLOR, highlightthickness=0, command=self.false_press)
        self.false.grid(row=2, column=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you have reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)