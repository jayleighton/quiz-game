import requests
import os
import time

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


class QuestionGeneretor:
    def __init__(self):
        """
        Creates an instance of the Question Generator class.
        Prompts the user to select the question category, difficulty and
        number of questions.
        Obtains questions via API and stores to an instance variable as a
        list of Question objects.
        """
        self.question_count = 0
        self.questions = {}
        self.question_category = 0
        self.difficulty = ""
        self.get_question_count()
        self.get_question_category()
        self.get_diffculty()
        self.get_questions()


    def get_question_category(self):
        """
        Prompts the user to select the question category from a list.
        """
        # Clear the screen
        os.system('clear')
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
                    self.question_category = category_list[selected_category -1]
                    break
                except ValueError as e:
                    os.system('clear')
                    print(f"\nInvalid category selected.\nPlease enter a category between 1 and {len(category_list)}")


    def get_diffculty(self):
        """
        Prompts the user for the difficulty level.
        The user can choose from Easy, Medium, Hard or Any
        """
        # Clear the screen
        os.system('clear')
        print(LOGO)
        # Prompt user to select difficulty
        print("Choose a difficulty\n")
        difficulty = input("(E)asy, (M)edium, (H)ard, or (A)ny\n")
        if difficulty[0].lower() == 'e':
            self.difficulty = 'easy'
        elif difficulty[0].lower() == 'm':
            self.difficulty = 'medium'
        elif difficulty[0].lower() == 'h':
            self.difficulty = 'hard'
        else:
            self.difficulty = 'any'


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
        
        print("Getting questions")
        result = requests.get(url=TRIVIA_URL, params=params)
        result.raise_for_status()
        # Validate the question list is not empty
        if len(result.json()['results']) == 0 and self.difficulty != 'any':
            # Set the difficulty to Any
            del params['difficulty']
            print("No questions for difficulty selected.")
            print('Fetching questions for "Any" difficulty.\nPlease wait...')
            # Wait 5 seconds due to API restriction
            time.sleep(5)
            # Call the API again
            result = requests.get(url=TRIVIA_URL, params=params)
            result.raise_for_status()
        # Save the questions to the instance variable
        self.questions = result.json()['results']

 
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
                self.question_count = question_amount
                # Exit the While loop
                break
            except ValueError:
                # Input error, prompt again
                os.system('clear')
                print(LOGO)
                print("Please enter a valid value between 10 and 40")


