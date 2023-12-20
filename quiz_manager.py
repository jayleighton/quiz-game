from question_object import Question
import os
from question_data import LOGO
import math
from clearmixin import ClearMixin


class QuizManager(ClearMixin):
    def __init__(self, question_list):
        """
        Creates an instance of the Quiz Manager class.
        Manages the scoring, displaying of questions,
        and answer validation
        """
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.current_question = None
        self.message = ""
        self.clear_screen()


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
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            print(LOGO)
            print(self.message)
            try:
                # Display the question
                q_text = self.current_question.question_text
                print(f"Q.{self.question_number}: {q_text}")
                # Get the user answer
                user_answer = input('(T)rue or (F)alse\n')
                    
                # Check that an answer was provided
                if len(user_answer) == 0:
                    raise ValueError()
            except ValueError:
                self.clear_screen()
                print("Invalid answer supplied.\nPlease try again\n")
            else:
                # Check the users answer against for the current question
                self.check_answer(user_answer)
                break


    def check_answer(self, users_answer):
        """
        Receives the users answer as a parameter and check it against the
        correct answer
        Sets the answer response
        """
        correct_answer = self.current_question.question_answer
        if users_answer[0].lower() == correct_answer[0].lower():
            self.message = "Well Done! That is correct\n"
            self.score += 1
        else:
            self.message = f"Incorrect! The correct answer was: "\
                f"{correct_answer}\n"
        # Clear the display
        self.clear_screen()


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
