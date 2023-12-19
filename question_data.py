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

    def get_question_category(self):
        print("Please select a category from the list:")
        if len(CATEGORIES) > 0:
            count = 1
            for category in CATEGORIES:
                print(f"{count}. {category}")
                count += 1
        selected_category
        

    def get_questions(self, question_category):
        params = {
            'amount': number_of_questions,
            'category': question_category,
            'type': 'boolean'
        }

        result = requests.get(url=TRIVIA_URL, params=params)
        return result.json()['results']

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
            
            

