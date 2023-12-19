from question_object import Question


class QuizManager:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.current_quesion = None
    
    def has_question(self):
        return self.question_number < len(self.question_list)
    