from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    qsn=Question(question_text,question_answer)
    question_bank.append(qsn)

quiz=QuizBrain(question_bank)

while quiz.still_has_qsn():
    quiz.next_qsn()

print(f"you've completed the quiz\n"
      f"Your final score was: {quiz.score}/{quiz.qsn_num}")