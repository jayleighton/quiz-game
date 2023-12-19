from question_object import Question


class QuizManager:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.current_quesion = None
    
    def has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        self.current_quesion = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}. {self.current_quesion.question_text}. True/False\n")

