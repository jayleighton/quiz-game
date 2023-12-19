import question_data as QD 
import html

questions = QD.get_questions(10, 9)
for question in questions:
    answer = question['correct_answer']
    question = html.unescape(question['question'])
    print(question)
    print(answer)