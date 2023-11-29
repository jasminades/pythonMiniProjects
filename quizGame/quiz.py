quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What is the capital of Brazil?", "answer": "Brasília"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "What is the capital of Russia?", "answer": "Moscow"},
    {"question": "What is the capital of South Africa?", "answer": "Pretoria"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "What is the capital of Mexico?", "answer": "Mexico City"},
    {"question": "What is the capital of Italy?", "answer":"Rome"}
]

score = 0

for question_dict in quiz:
    print(question_dict['question'])
    user_answer = input ("Answer? ")

    if user_answer.lower() == question_dict['answer'].lower():
        print("Correct! ")
        score += 1
        print("Your score is: " + str(score))
    else:
        print("Wrong answer!")
        print("The correct answer is " + question_dict['answer'])
