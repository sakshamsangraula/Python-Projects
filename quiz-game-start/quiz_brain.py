
# create a QuizBrain class


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        """ See if user's answer is the same as the actual answer"""
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")

        print(f"The correct answer was {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()

    def next_question(self):
        self.question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {self.question.text}. (True/False)?: ")
        self.check_answer(user_ans, self.question.answer)
        # self.ans = self.question["answer"]
        # if user_ans == self.ans:
        #     # call the next question method
        #     self.question_number += 1



