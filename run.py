from question_data import QuestionGeneretor
import html
from question_object import Question
from quiz_manager import QuizManager

question_generator = QuestionGeneretor()
question_data = question_generator.questions

question_list = []
for question_data in question_data:
    question_text = question_data['question']
    question_answer = question_data['correct_answer']
    new_question = Question(question_text, question_answer)
    question_list.append(new_question)

quiz_manager = QuizManager(question_list)
print("Quiz Manager Created")
print(quiz_manager.has_question())

# if len(CATEGORIES) > 0:
#             count = 1
#             for category in CATEGORIES:
#                 print(f"{count}. {category}")
#                 count += 1

# print(len(QD.CATEGORIES))

# questions = QD.get_questions(10, 9)
# for question in questions:
#     answer = question['correct_answer']
#     question = html.unescape(question['question'])
#     print(question)
#     print(answer)