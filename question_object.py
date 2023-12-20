class Question:
    def __init__(self, question_text, question_answer, incorrect_answers):
        """
        Creates an instance of the Question object.
        Stores the question and answer text using instance variables
        """
        self.question_text = question_text
        self.question_answer = question_answer
        self.incorrect_answers = incorrect_answers
        print(self.incorrect_answers)