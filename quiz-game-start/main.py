from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# loop through the question data and create a question bank list with a list of objects

question_bank = []
for question in question_data:
    ques = question["question"]
    ans = question["correct_answer"]
    # create a question object and add it to the list
    question_obj = Question(ques, ans)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")

# for question in question_bank:
#     print(question.text)
#     print(question.answer)

