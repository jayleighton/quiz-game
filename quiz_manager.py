from question_object import Question
import math
from clearmixin import ClearMixin
import html
import random


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
        self.multiple_answer_list = []
        self.clear_screen()

    def has_question(self) -> bool:
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
            self.show_logo()
            print(self.message)
            try:
                # Display the question
                q_text = self.current_question.question_text
                print(f"Q.{self.question_number}: {q_text}")
                # Get the user answer
                user_answer = input(self.show_answer_prompt())
                # Check that an answer was provided
                if self.current_question.question_type == 'boolean':
                    if len(user_answer) == 0:
                        raise ValueError()
                    elif user_answer[0].lower() != 't' and\
                            user_answer[0].lower() != 'f':
                        raise ValueError()
                if self.current_question.question_type == 'multiple':
                    if int(user_answer) < 1 or \
                            int(user_answer) > len(self.multiple_answer_list):
                        raise ValueError()
            except ValueError:
                self.clear_screen()
                self.message = "Invalid answer supplied. Please try again\n"
                if self.current_question.question_type == 'multiple':
                    self.message += f"Please select and answer between 1 and "\
                        f"{len(self.multiple_answer_list)}"
                else:
                    self.message += "Please select (T)rue or (F)alse"

            else:
                # Check the users answer against for the current question
                self.check_answer(user_answer)
                break

    def show_answer_prompt(self) -> str:
        """
        Formulates the answer prompt based on the question type.
        returns the answer prompt as a string
        """
        # Validate question type
        if self.current_question.question_type == "boolean":
            return "\n(T)rue or (F)alse\n"
        elif self.current_question.question_type == 'multiple':
            # Create list from incorrect and correct answers
            self.multiple_answer_list = self.current_question.incorrect_answers
            # Check that the correct answer is not in the list before appending
            if self.current_question.question_answer not in \
                    self.multiple_answer_list:
                self.multiple_answer_list.append(
                    self.current_question.question_answer)
            # Randomize the list
            random.shuffle(self.multiple_answer_list)
            # Create the result string
            result = "\n"
            for index in range(len(self.multiple_answer_list)):
                # Remove special characters from list
                self.multiple_answer_list[index] = html.unescape(
                    self.multiple_answer_list[index])
                # Formulate line to add to result string
                result += f"{index + 1}. "\
                    f"{html.unescape(self.multiple_answer_list[index])}\n"
            return result

    def check_answer(self, users_answer: str):
        """
        Receives the users answer as a parameter and check it against the
        correct answer
        Sets the answer response
        """
        correct_answer = self.current_question.question_answer
        # Validate the question type
        if self.current_question.question_type == 'boolean':
            if users_answer[0].lower() == correct_answer[0].lower():
                self.message = "Well Done! That is correct\n"
                self.score += 1
            else:
                self.message = f"Incorrect! The correct answer was: "\
                    f"{correct_answer}\n"
        elif self.current_question.question_type == 'multiple':
            if self.multiple_answer_list[int(users_answer)-1] == \
                                                correct_answer:
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
        self.show_logo()
        # Print the result of the last question
        print(self.message)
        print("Quiz Complete!\n")
        # Set the message based on the calculated percentage
        if result < 50:
            print("Better luck next time...")
        elif result < 80:
            print("Well done!")
        else:
            print("Excellent!")
        # Print the result
        print(f"Your score is: {self.score}/{self.question_number}"
              f", {math.floor(result)}% ")
