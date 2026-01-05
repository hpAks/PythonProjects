

class QuizBrain:
    def __init__(self, quiz_list):
        self.question_number = 0
        self.score = 0
        self.quiz_list = quiz_list

    def still_has_question(self):
        return self.question_number < len(self.quiz_list)

    def check_answer(self, given_answer, actual_answer):
        if given_answer.lower() == actual_answer.lower():
            self.score +=1
            print(f"That's correct! Your score is : {self.score}/{self.question_number}")
            return True
        else:
            print(f"Oops.. That's wrong.. Correct answer: {actual_answer}")
            return False

    def next_question(self):
        if self.question_number < len(self.quiz_list):
            response = self.quiz_list[self.question_number]
            self.question_number += 1
            return response
        else:
            return ""
