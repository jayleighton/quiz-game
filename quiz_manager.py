from question_object import Question
import os
from question_data import LOGO
import math


class QuizManager:
    def __init__(self, question_list):
        """
        Creates an instance of the Quiz Manager class.
        Manages the scoring, displaying of questions,
        and answer validation
        """
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.current_quesion = None
        self.message = ""
        os.system('clear')


    def has_question(self):
        """
        Returns True if more questions are available
        """
        return self.question_number < len(self.question_list)


    def next_question(self):
        """
        Gets the next question from the list and displays to the user.
        """
        # Set the current question
        self.current_quesion = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            print(LOGO)
            print(self.message)
            try:
                # Get the user answer
                user_answer = input(f"Q.{self.question_number}: "
                    f"{self.current_quesion.question_text}. True / False\n")
                # Check that an answer was provided
                if len(user_answer) == 0:
                    raise ValueError()
            except ValueError:
                os.system('clear')
                print("Invalid answer supplied.\nPlease try again\n")
            else:
                # Check the users answer against for the current question
                self.check_answer(user_answer)
                break


    def check_answer(self, users_answer):
        """
        Receives the users answer as a parameter and check it against the correct answer
        Sets the answer response
        """
        correct_answer = self.current_quesion.question_answer
        if users_answer[0].lower() == correct_answer[0].lower():
            self.message = "Well Done! That is correct\n"
            self.score += 1
        else:
            self.message = f"Incorrect! The correct answer was: "\
                "{correct_answer}\n"
        # Clear the display
        os.system('clear')


    def show_result(self):
        """
        Called to display the current correct score count to the user
        A percentage score is also provided as feedback to the user
        """
        # Calculate correct percentage
        result = (self.score / self.question_number) * 100
        print(LOGO)
        print("Quiz Complete!\n")
        # Set the message based on the calculated percentage
        if result < 50:
            print("Better luck next time...")
        elif result < 80:
            print("Well done!")
        else:
            print("Excellent!")
        # Print the result
        print(f"\nYour score is: {self.score}/{self.question_number}"
            f", {math.floor(result)}% ")
