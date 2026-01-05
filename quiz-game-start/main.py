from sqlalchemy.sql.sqltypes import NullType

import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data_info in data.question_data:
    quest = Question(data_info.get("question"), data_info.get("correct_answer"))
    question_bank.append(quest)

quiz = QuizBrain(question_bank)
go_on = True
while quiz.still_has_question() and go_on:
    next_quest = quiz.next_question()
    ans = input(f"Q.{quiz.question_number} : {next_quest.text} (True/False): ")
    if not quiz.check_answer(ans.lower(), next_quest.answer.lower()) :
        go_on = False
    print("\n")
print(f"Well done! Your final score is {quiz.score}")

