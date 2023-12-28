import requests
import sys
import time
from clearmixin import ClearMixin

# Category List
CATEGORIES = {
    'General Knowledge': 9,
    'Entertainment: Film': 11,
    'Entertainment: Television': 14,
    'Entertainment: Music': 12,
    'Sports': 21,
    'Geography': 22,
    'Animals': 27,
    'History': 23,
    'Mythology': 20,
    'Science and Nature': 17,
    'Any': 0,
}


class QuestionGeneretor(ClearMixin):
    def __init__(self):
        """
        Creates an instance of the Question Generator class.
        Prompts the user to select the question category, difficulty and
        number of questions.
        Obtains questions via API and stores to an instance variable as a
        list of Question objects.
        """
        self.message = ""
        self.question_count = self.get_question_count()
        self.question_category = self.get_question_category()
        self.difficulty = self.get_difficulty()
        self.question_type = self.get_question_type()
        self.questions = self.get_questions()

    def get_question_category(self):
        """
        Prompts the user to select the question category from a list.
        """
        while True:
            self.show_logo()
            print(self.message)
            print("Please select a category from the list:")
            # Validate category dict is not blank
            if len(CATEGORIES) > 0:
                # Create a list of categories
                category_list = [category for category in CATEGORIES.keys()]
                # Generate the list to display to the user
                for index in range(len(category_list)):
                    print(f"{index + 1}: {category_list[index]}")
                try:
                    # Validate input
                    selected_category = int(input(
                        "Please enter your category number:\n"))
                    if selected_category < 1 or\
                            selected_category > len(category_list):
                        raise ValueError(selected_category)
                    return category_list[selected_category - 1]
                    break
                except ValueError as e:
                    # Clear screen and set error message
                    self.clear_screen()
                    self.message = f"\nInvalid category selected.\nPlease "\
                        f"enter a category between 1 and {len(category_list)}"
                else:
                    self.message = ""
                    self.clear_screen()

    def get_difficulty(self):
        """
        Prompts the user for the difficulty level.
        The user can choose from Easy, Medium, Hard or Any
        """
        DIFFICULTY_LIST = ['Easy', 'Medium', 'Hard', 'Any']
        # Clear the screen
        self.clear_screen()
        # Prompt user to select difficulty
        while True:
            self.show_logo()
            print(self.message)
            try:
                print("Please choose a difficulty:")
                # Prepare difficulty options
                difficulty_string = ""
                for index in range(len(DIFFICULTY_LIST)):
                    text = f'{index + 1}. {DIFFICULTY_LIST[index]}\n'
                    difficulty_string += text
                # Get user selection
                difficulty = int(input(difficulty_string))
                if difficulty < 1 or difficulty > len(DIFFICULTY_LIST):
                    raise ValueError()
            except ValueError:
                # Clear the screen and generate error message
                self.clear_screen()
                self.message = "Invalid difficulty entered. Please try again"
            else:
                difficulty = DIFFICULTY_LIST[difficulty-1].lower()
                self.message = ""
                self.clear_screen()
                return difficulty

    def get_question_type(self):
        """
        Prompts the user to select the type of questions for the quiz.
        Valid answers are True/False or Multiple Choice
        """
        self.clear_screen()
        # Loop until a valid selection is made
        while True:
            self.show_logo()
            print(self.message)
            print("What type of questions do you want?")
            try:
                # Read the user input
                response = int(input("1. True/False\n2. Multiple choice\n"))
                # Validate user input
                if response < 1 or response > 2:
                    raise ValueError()
            except ValueError:
                # Clear screen and print error
                self.clear_screen()
                self.message = "Invalid selection. Please try again\n"

            else:
                # Return the type of questions selected
                self.message = ""
                self.clear_screen()
                if response == 1:
                    return 'boolean'
                elif response == 2:
                    return 'multiple'

    def get_questions(self):
        """
        Uses the answers from the user to fetch the questions via API.

        """
        # Set the amount of questions parameter and the question type
        params = {
            'amount': self.question_count,
            'type': self.question_type,
        }

        # Check the category and add the parameter if not any
        if self.question_category != 'Any':
            params['category'] = CATEGORIES[self.question_category]

        # Check the difficulty and add the parameter if not any
        if self.difficulty != 'any':
            params['difficulty'] = self.difficulty

        results = self.post_request(
            parameters=params,
            message="Getting questions",
            wait_time=0)
        # Validate the question list is not empty
        if len(results) == 0 and self.difficulty != 'any':
            # Set the difficulty to Any
            del params['difficulty']
            # Call the API again
            post_message = 'No questions for difficulty selected.\n'
            post_message += 'Fetching questions for "Any" difficulty.\n'
            post_message += 'Please wait 5 seconds...'
            results = self.post_request(
                parameters=params, message=post_message,
                wait_time=5)
        # Save the questions to the instance variable
        return results

    def post_request(self, parameters, message, wait_time: int):
        """
        Use the parameters and message to process the post request.
        """
        TRIVIA_URL = 'https://opentdb.com/api.php'
        # Print the user message
        print(message)
        if wait_time > 0:
            time.sleep(wait_time)
        result = requests.get(url=TRIVIA_URL, params=parameters)
        result.raise_for_status()
        return result.json()['results']

    def get_question_count(self):
        """
        Prompt the user for the number of questions.
        Validates the amount entered and stores to an instance variable
        """
        print("Welcome to the Quiz Game")
        while True:
            self.show_logo()
            print(self.message)
            try:
                # Prompt for the number of questions
                print("How many questions would you like?\n")
                q_string = "Enter a number between 10 and 40, or 0 to quit\n"
                question_amount = int(input(q_string))
                # Validate the input
                if question_amount == 0:
                    print('Exiting')
                    sys.exit()
                if question_amount < 10 or question_amount > 40:
                    raise ValueError()
            except ValueError:
                # Input error, prompt again
                self.clear_screen()
                self.message = "Please enter a valid value between 10 and 40"
            else:
                self.message = ""
                self.clear_screen()
                # Return the question count selected
                return question_amount
