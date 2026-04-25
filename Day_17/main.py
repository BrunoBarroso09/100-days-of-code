from pyproject_hooks import quiet_subprocess_runner

from data import question_data
from quiz_model import Model
from quiz_logic import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Model(question_text, question_answer)
    print(new_question)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Thanks for completing that!\nYour final score is: {quiz.score}/{quiz.question_number}")