from question_data import QuestionGeneretor
import html
from question_object import Question
from quiz_manager import QuizManager
import os


def main():

    while True:

        question_generator = QuestionGeneretor()
        question_data = question_generator.questions

        question_list = []
        for question_data in question_data:
            question_text = html.unescape(question_data['question'])
            question_answer = question_data['correct_answer']
            new_question = Question(question_text, question_answer)
            question_list.append(new_question)

        quiz_manager = QuizManager(question_list)
        # Clear the console
        os.system('clear')

        # Run the game while questions are available
        while quiz_manager.has_question():
            quiz_manager.next_question()

        quiz_manager.show_result()

        # Check if users wants to play again
        result = input("\nDo you want to play again? Y / N\n")
        if result.upper() != 'Y':
            print("Thanks for playing!")
            break
        else:
            os.system('clear')


main()
# question_generator = QuestionGeneretor()
# question_data = question_generator.questions