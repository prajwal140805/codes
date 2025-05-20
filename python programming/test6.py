import requests
import html
import random

print("_______________________________________________________________________________________________ ")
print('\n')
print("*******************************WELCOME TO KAUN BANEGA CROREPATI*******************************")

# Game intro
while True:
    print("********************************press ENTER key to continue**********************************")
    print("_______________________________________________________________________________________________ ")
    print('\n')
    c = input()
    if c == '':
        break

print("****************************************Game Rules********************************************")
print("1. 10 questions will be fetched from an online trivia database.")
print("2. Each question has 4 options. Choose the correct one.")
print("3. If you answer correctly, you win increasing amounts.")
print("4. If you answer incorrectly, you take home only the minimum guaranteed amount.")
print("5. You can quit the game after any question.")
print('\n')

# Start game
while True:
    c = input(
        "******************************press ENTER key to start the game********************************")
    if c == '':
        break

# Fetch questions from Open Trivia DB
url = "https://opentdb.com/api.php?amount=10&type=multiple"
response = requests.get(url)
data = response.json()

questions = data['results']

amounts = [2000, 5000, 10000, 50000, 100000,
           200000, 500000, 1000000, 5000000, 10000000]
min_amounts = [0, 0, 10000, 10000, 10000,
               200000, 200000, 200000, 1000000, 1000000]

amount = 0
min_amount = 0

for i, q in enumerate(questions):
    print("_______________________________________________________________________________________________ ")
    question_text = html.unescape(q['question'])
    correct_answer = html.unescape(q['correct_answer'])
    options = [html.unescape(opt)
               for opt in q['incorrect_answers']] + [correct_answer]
    random.shuffle(options)

    print(
        f"{i+1}. {question_text}:[for rupees {amounts[i]} minimum {min_amounts[i]}]")
    for idx, opt in enumerate(options):
        print(f"{chr(65+idx)}) {opt}")

    # Get user input
    answer = input("Lock the option: ").upper()
    while answer not in ['A', 'B', 'C', 'D']:
        answer = input("Please enter a valid option (A/B/C/D): ").upper()

    selected_option = options[ord(answer) - 65]

    if selected_option == correct_answer:
        print("Correct answer!")
        amount = amounts[i]
        min_amount = min_amounts[i]

        if amount == 10000000:
            print("Congratulations! You are the winner of Kaun Banega Crorepati!")
            print("*************You have won rupees: ", amount, "*************")
            break

        print("Your current amount is: ", amount)
        print("If the next question is wrong, you will win only rupees: ", min_amount)
        if i < 9:
            print(
                "If the next question is correct, you will win rupees: ", amounts[i+1])
        print("_______________________________________________________________________________________________ ")
        print("Press ENTER to continue or type 'q' to quit:")
        b = input()
        if b.lower() == 'q':
            print("You have exited the game.")
            print("You have won rupees: ", amount)
            break
        elif b == '':
            continue
        else:
            break
    else:
        print("Wrong answer!")
        print("The correct answer was:", correct_answer)
        amount = min_amount
        break

if amount == 0:
    print("You lost the game.")
elif amount > 0 and amount < 10000000:
    print("Congratulations! You won rupees:", amount)
