from question_object import Question
import os
from question_data import LOGO
import math


class QuizManager:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.current_quesion = None
        self.message = ""
        os.system('clear')

    def has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_quesion = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            print(LOGO)
            print(self.message)
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
            self.message = "Well Done! That is correct\n"
            self.score += 1
        else:
            self.message = f"Incorrect! The correct answer was: {correct_answer}\n"
        # Clear the display
        os.system('clear')

    def show_result(self):
        result = (self.score / self.question_number) * 100
        print(LOGO)
        print("Quiz Complete!\n")
        if result < 50:
            print("Better luck next time.")
        elif result < 80:
            print("Well done!")
        else:
            print("Excellent work!")

        print(f"Your score is: {self.score}/{self.question_number}, {math.floor(result)}%")