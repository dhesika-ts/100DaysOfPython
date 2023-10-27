from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UiInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score=0", bg=THEME_COLOR, fg='white', font=('Ariel', 15, 'normal'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=350, height=300)
        self.qsn = self.canvas.create_text(170, 150, text="Qsn", fill=THEME_COLOR, font=('Ariel', 20, 'italic'),
                                           width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.send_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.send_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.qsn, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.qsn, text=f"You've reached the end "
                                                  f"of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def send_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def send_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
