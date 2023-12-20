import requests
import os
import time
from clearmixin import ClearMixin

LOGO = """
         ______     __  __     __     ______        ______     ______     __    __     ______    
        /\  __ \   /\ \/\ \   /\ \   /\___  \      /\  ___\   /\  __ \   /\ "-./  \   /\  ___\   
        \ \ \/\_\  \ \ \_\ \  \ \ \  \/_/  /__     \ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\   
         \ \___\_\  \ \_____\  \ \_\   /\_____\     \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\ 
          \/___/_/   \/_____/   \/_/   \/_____/      \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/ 

"""

TRIVIA_URL = 'https://opentdb.com/api.php'

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
        self.question_count = self.get_question_count()
        self.questions = {}
        self.question_category = self.get_question_category()
        self.difficulty = self.get_diffculty()
        self.question_type = self.get_question_type()
        
        
        
        self.get_questions()


    def get_question_category(self):
        """
        Prompts the user to select the question category from a list.
        """
        # Clear the screen
        self.clear_screen()
        print(LOGO)
        while True:
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
                    selected_category = int(input("Please enter your category number:\n"))
                    if selected_category < 1 or selected_category > len(category_list):
                        raise ValueError(selected_category)
                    return category_list[selected_category -1]
                    break
                except ValueError as e:
                    self.clear_screen()
                    print(f"\nInvalid category selected.\nPlease enter a category between 1 and {len(category_list)}")


    def get_diffculty(self):
        """
        Prompts the user for the difficulty level.
        The user can choose from Easy, Medium, Hard or Any
        """
        # Clear the screen
        self.clear_screen()
        # Prompt user to select difficulty
        while True:
            print(LOGO)
            print("Choose a difficulty\n")
            try:
                difficulty = input("(E)asy, (M)edium, (H)ard, or (A)ny\n")
                if len(difficulty) == 0:
                    raise ValueError()
            except ValueError:
                self.clear_screen()
                print("No difficulty entered")
                print("Please try again")
            else:
                if difficulty[0].lower() == 'e':
                    difficulty = 'easy'
                elif difficulty[0].lower() == 'm':
                    difficulty = 'medium'
                elif difficulty[0].lower() == 'h':
                    difficulty = 'hard'
                else:
                    difficulty = 'any'
            
                return difficulty


    def get_question_type(self):
        """
        Prompts the user to select the type of questions for the quiz.
        Valid answers are True/False or Multiple Choice
        """
        self.clear_screen()
        # Loop until a valid selection is made
        while True:
            print(LOGO)
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
                print("Invalid selection")
                print("Please try again")

            else:
                # Return the type of questions selected
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
            'type': 'boolean',
        }
        
        # Check the category and add the parameter if not any
        if self.question_category != 'Any':
            params['category'] = CATEGORIES[self.question_category]

        # Check the difficulty and add the parameter if not any
        if self.difficulty != 'any':
            params['difficulty'] = self.difficulty
        
        
        results = self.post_request(parameters=params, message="Getting questions")
        # Validate the question list is not empty
        if len(results) == 0 and self.difficulty != 'any':
            # Set the difficulty to Any
            del params['difficulty']
            print("No questions for difficulty selected.")
            print('Fetching questions for "Any" difficulty.\nPlease wait...')
            # Wait 5 seconds due to API restriction
            time.sleep(5)
            # Call the API again
            results = self.post_request(parameters=params, message='Fetching questions for "Any" difficulty.\nPlease wait...')
        # Save the questions to the instance variable
        self.questions = results

 
    def post_request(self, parameters, message):
        
        result = requests.get(url=TRIVIA_URL, params=parameters)
        result.raise_for_status()

        return result.json()['results']

    def get_question_count(self):
        """
        Prompt the user for the number of questions.
        Validates the amount entered and stores to an instance variable
        """
        print(LOGO)
        print("Welcome to the Quiz Game")
        while True:
            try:
                # Prompt for the number of questions
                print("How many questions would you like?\n")
                question_amount = int(input("Enter a number between 10 and 40, or 0 to quit\n"))
                # Validate the input
                if question_amount == 0:
                    print('Exiting')
                    break
                if question_amount < 10 or question_amount > 40:
                    raise ValueError()
                # Store the number of questions to the instance variable
                return question_amount
                # Exit the While loop
                break
            except ValueError:
                # Input error, prompt again
                self.clear_screen()
                print(LOGO)
                print("Please enter a valid value between 10 and 40")


