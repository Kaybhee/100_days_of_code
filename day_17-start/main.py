from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    q1 = i['question']
    a1 = i['correct_answer']
    new_question = Question(q1, a1)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
# print(quiz)
while quiz.still_has_questions:
    quiz.next_question() 


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
