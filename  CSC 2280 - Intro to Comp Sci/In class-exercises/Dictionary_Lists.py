import random
question_ans_dict = {
                    "Yes?" : 'Yes',
                    "No?" : 'Yes',
                    "Maybe?" : 'No',
                    "I don't know?" : 'No',
                    }

score = 0
questions = list(question_ans_dict.keys())

i = 1
while True:
    question = random.choice(questions)
    print(f'Question {i} : {question}')
    i = i + 1
    
    user = input("Answer: ")
    
    if user.lower() == 'exit':
        print("Your final score is:", score)
        break
    
    correct_ans = question_ans_dict[question]
    
    if user.lower() == correct_ans.lower():
        score = score + 1
        print(f"Correct! Your score is {score}")
        print('-------------')
    else:
        print(f'Correct Answer: {correct_ans} \n')
        print(f'Incorrect Answer! Your score is {score}')
        print('-------------')
    



for i in range(10):
    question = random.choice(questions)
    
    print(f'Question {i + 1} : {question}')
    user_input = input('Answer: ')
    right_answer = question_ans_dict[question]
    
    if user_input.lower() == right_answer.lower():
        score = score + 1
        print(f'Correct Answer! Your score is {score}')
        print('------------------')
    else:
        print(f'Correct Answer: {right_answer}')
        print(f'Incorrect Answer! Your score is {score}')
        print('------------------')
