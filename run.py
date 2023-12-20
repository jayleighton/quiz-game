from question_data import QuestionGeneretor
import html
from question_object import Question
from quiz_manager import QuizManager
import os


def main():

    # Game loop
    while True:
        # Initialize question generator
        question_generator = QuestionGeneretor()
        question_data = question_generator.questions

        # Loop through questions, create Question object and add to list
        question_list = []
        for question_data in question_data:
            question_text = html.unescape(question_data['question'])
            question_answer = html.unescape(question_data['correct_answer'])
            incorrect_answers = question_data['incorrect_answers']
            question_type = question_data['type']
            new_question = Question(question_text, question_answer,
                                    incorrect_answers, question_type)
            question_list.append(new_question)

        # Initialize the quiz manager
        quiz_manager = QuizManager(question_list)

        # Clear the console
        os.system('clear')

        # Run the game while more questions are available
        while quiz_manager.has_question():
            quiz_manager.next_question()

        # Display the score
        quiz_manager.show_result()

        # Check if users wants to play again
        result = input("\nDo you want to play again? Y / N\n")
        if result.upper() != 'Y':
            print("Thanks for playing!")
            break
        else:
            os.system('clear')


main()
