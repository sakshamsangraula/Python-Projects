from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:

# whenever the UI is created a QuizBrain object is also passed in so make sure that only QuizBrain
# objects are accepted by doing "quiz: QuizBrain"

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # score label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 20, "normal"))
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Some Question",
                                                     fill="black",
                                                     font=("Ariel", 15, "italic"),
                                                     # set the width to 280 (width less than canvas)
                                                     # so that the text wraps
                                                     width=280)
        # also add vertical padding outside the canvas
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # added self. to things that should be accessed anywhere in the class and didn't add it to
        # images because they don't have to be accessed anywhere else in the class
        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        # change the background back to white
        self.canvas.config(bg="white")
        # keep going if we have enough questions left
        if self.quiz.still_has_questions():
            # update the score text every time we go to the next question if we still have questions
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # if we don't have any other questions left, let the user know and disable the two buttons
            self.canvas.itemconfig(self.question_text,
                                   text="You've reached the end of the quiz!")
            self.check_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

     # if the user chooses the check button, call the check answer function with "True"
    def true_pressed(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    # if the user chooses the check button, call the check answer function with "False"
    def false_pressed(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # change the background to green if it is right and red if it's wrong and
        # go to the next question after 1 second either way
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # make sure to only include the function name and don't actually call the function with
        # parenthesis in the window.after function
        self.window.after(1000, self.get_next_question)








    # Python Hints and Arrows

    # This function only accepts a string so that we don't accidentally send the wrong input
    # and catch this bug before getting an error after running it

    # this function also outputs an int and it promises this so we can only return an int
    # def type_name(name: str) -> int:
    #     if name == "Name":
    #         return 0
    #     else:
    #         return 1