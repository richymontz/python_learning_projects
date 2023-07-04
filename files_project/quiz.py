questions_file = open('questions.txt', 'r')
question_lines = [line.strip().split('=') for line in questions_file.readlines()]
questions_file.close()

couples = list(zip(*question_lines))
questions, answers = list(couples[0]), list(couples[1])

total_questions = len(questions)
score = 0

for i, question in enumerate(questions):
    user_answer = input(f'{question} = ')

    if user_answer == answers[i]: score += 1

result_file = open('result.txt', 'w')
result_file.write(f'Your final score is {score}/{total_questions}.')
result_file.close()
