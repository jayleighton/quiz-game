import requests
from pprint import pprint
import os

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
    'Science and Nature': 17
}


class QuestionGeneretor:

    def __init__(self):
        self.question_count = 0
        self.questions = {}
        self.question_category = 0
        self.difficulty = ""
        self.get_question_count()
        self.get_question_category()
        self.get_diffculty()
        self.get_questions()

    def get_question_category(self):
        os.system('clear')
        print(LOGO)
        while True:
            print("Please select a category from the list:")
            if len(CATEGORIES) > 0:
                category_list = [category for category in CATEGORIES.keys()]
                for index in range(len(category_list)):
                    print(f"{index + 1}: {category_list[index]}")
                try:
                    selected_category = int(input("Please enter your category number:\n"))
                    if selected_category < 1 or selected_category > 10:
                        raise ValueError(selected_category)
                    self.question_category = category_list[selected_category -1]
                    break
                except ValueError as e:
                    os.system('clear')
                    print(f"\nInvalid category selected.\nPlease enter a category between 1 and {len(category_list)}")
    
    def get_diffculty(self):
        os.system('clear')
        print(LOGO)
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
        params = {
            'amount': self.question_count,
            'category': CATEGORIES[self.question_category],
            'type': 'boolean'
        }

        result = requests.get(url=TRIVIA_URL, params=params)
        self.questions = result.json()['results']

    def get_question_count(self):
        print(LOGO)
        print("Welcome to the Quiz Game")
        while True:
            
            try:
                question_amount = int(input("How many questions would you like?:\nEnter a number between 10 and 40, or 0 to quit\n"))
                if question_amount == 0:
                    print('Exiting')
                    break
                if question_amount < 10 or question_amount > 40:
                    raise ValueError()
                self.question_count = question_amount
                return self.question_count
            except ValueError:
                os.system('clear')
                print(LOGO)
                print("Please enter a valid value between 10 and 40")
            
            

