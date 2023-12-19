from question_object import Question
import os

class QuizManager:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.current_quesion = None
        os.system('clear')
    
    def has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        self.current_quesion = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            try:
                user_answer = input(f"Q.{self.question_number}: {self.current_quesion.question_text}. True/False\n")
                if len(user_answer) == 0:
                    raise ValueError()
            except ValueError:
                os.system('clear')
                print("Invalid answer supplied.\nPlease try again\n")
            else:
                self.check_answer(user_answer)
                break

    def check_answer(self, users_answer):
        correct_answer = self.current_quesion.question_answer
        if users_answer[0].lower() == correct_answer[0].lower():
            print("Well Done! That is correct\n")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}\n")
