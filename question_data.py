import requests
from pprint import pprint

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

def get_questions(number_of_questions, question_category):
    params = {
        'amount': number_of_questions,
        'category': question_category,
        'type': 'boolean'
    }

    result = requests.get(url=TRIVIA_URL, params=params)
    return result.json()['results']




