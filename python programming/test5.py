# create kaun banega crorepati game 
q=[
["1. Who is the current Prime Minister of India ?:[for rupees 2000 minimum 0]",
    'A) Rahul Gandhi',
    'B) Narendra Modi',
    'C) Arvind Kejriwal',
    'D) Amit Shah'],
['2. Which party is currently ruling at the national level?:[for rupees 5000 minimum 0]',
    'A) Indian National Congress',
    'B) Aam Aadmi Party',
    'C) Bharatiya Janata Party (BJP)',
    'D) Communist Party of India'],
['3. Who is known as the "Father of the Indian Constitution"?:[for rupees 10000 minimum 0]',
    'A) Mahatma Gandhi',
    'B) Jawaharlal Nehru',
    'C) B.R. Ambedkar',
    'D) Sardar Vallabhbhai Patel'],
['4. What is the upper house of the Indian Parliament called?:[for rupees 50000 minimum 10000]',
    'A) Lok Sabha',
    'B) Rajya Sabha',
    'C) Vidhan Sabha',
    'D) Gram Sabha'],
['5. How many members are elected to the Lok Sabha?:[for rupees 100000 minimum 10000]',
    'A) 545',
    'B) 250',
    'C) 500',
    'D) 600'],
[ '6. Who is the head of the state government in India?:[for rupees 200000 minimum 10000]',
    'A) Governor',
    'B) Chief Minister',
    'C) President',
    'D) Prime Minister'],
['7. Which article of the Constitution grants special status to Jammu and Kashmir (before abrogation)?:[for rupees 500000 minimum 200000]',
    'A) Article 356',
    'B) Article 370',
    'C) Article 35A',
    'D) Article 368' ],
['8. Who is the first woman Prime Minister of India?:[for rupees 1000000 minimum 200000]',
    'A) Pratibha Patil',
    'B) Sonia Gandhi',
    'C) Indira Gandhi',
    'D) Sushma Swaraj'],
['9. Which body conducts elections in India?:[for rupees 5000000 minimum 1000000]',
    'A) Supreme Court',
    'B) Parliament',
    'C) Election Commission of India',
    'D) Prime Ministers Office' ],
['10. How many states are there in India (as of 2025)?:[for rupees 10000000 minimum 1000000]',
    'A) 28',
    'B) 29',
    'C) 27',
    'D) 30 ']
  ]
k=['B','C','C','B','A','B','B','C','C','A']
amount=0
min_amount=0
print("_______________________________________________________________________________________________ ")
print('\n')  
print ("*******************************WELCOME TO KAUN BANEGA CROREPATI*******************************")
 

c=0
while True:
    print (" ********************************press ENTER key to continue**********************************")
    
    print("_______________________________________________________________________________________________ ")
    print('\n') 
    c = input()
    if c == '':
        break
 
  
 
print ("****************************************Game Rules********************************************")
print ("1. There are 10 questions in total.")
print ("2. Each question has 4 options.")
print ("3. You have to select the correct option.")
print ("4. If you answer correctly, you will win the amount mentioned in the question.")
print ("5. If you answer incorrectly, you will win only minimum amount mentioned in the question.")
print ("6. You can quit the game at any time by pressing any key.")
print ("7.  while locking your answer, press your selected option key and then press ENTER key .")
c=0
print('\n')  
 
print('\n')
while True:
   
    c = input("******************************press ENTER key to start the game********************************")
    if c == '':
        break

print('\n')
print("_______________________________________________________________________________________________ ")
   
for question in q:
    for option in question: 
        print(option)
    a = input ("lock the option:")
    a= a.upper()
    while a not in ['A','B','C','D']:
        a = input ("Please enter a valid option")
        a= a.upper()
    if a == k[q.index(question)]:
        print("_______________________________________________________________________________________________ ")
        print ("Correct answer:                                              ")    
        if q.index(question) == 0:
            amount = 2000
        elif q.index(question) == 1:
            amount = 5000
        elif q.index(question) == 2:
            amount = 10000
            min_amount = 10000
        elif q.index(question) == 3:
            amount = 50000
        elif q.index(question) == 4:
            amount = 100000
        elif q.index(question) == 5:
            amount = 200000
            min_amount = 200000
        elif q.index(question) == 6:
            amount = 500000
        elif q.index(question) == 7:
            amount = 1000000
            min_amount = 1000000
        elif q.index(question) == 8:
            amount = 5000000
        elif q.index(question) == 9:
               
             amount = 10000000
        if amount == 10000000:
            print ("Congratulations you are the winner of Kaun Banega Crorepati") 
            print ("*************You have won rupees: ", amount,"*************")
            break
       
        
        print("                                                            ")  
        print ("Your current amount is: ", amount,"                              ")  
        print("if the next question is wrong, you will win only rupees: ", min_amount )
        
        if q.index(question) == 0:
            amount = 5000
        elif q.index(question) == 1:
            amount = 10000
           
        elif q.index(question) == 2:
            amount = 50000
        elif q.index(question) == 3:
            amount = 100000
        elif q.index(question) == 4:
            amount = 200000
            
        elif q.index(question) == 5:
            amount = 500000
        elif q.index(question) == 6:
            amount = 1000000
           
        elif q.index(question) == 7:
            amount = 5000000
        elif q.index(question) == 8:
             print ("you won the game" ) 
             amount = 10000000
        
        print("if the next question is correct, you will win rupees: ", amount )
        print("                                                            ") 
        print("________________________________________________________________________________________________ ")
        print('\n')  
        print("press ENTER key to continue or q to exit the game")
         
        print("________________________________________________________________________________________________ ")
        b = input()
         
        if b == 'q':
            print ("You have exited the game")
            print ("You have won rupees: ", amount)
            break
        elif b == '':
            continue
        else:
            break      
    else:
        print ("Wrong answer:")
        
        
         
        print ("The correct answer is: ", k[q.index(question)])
        amount = min_amount
        print ("Your current amount is: ", min_amount)
        break
if amount == 0:
    print ("You lost the game")
elif amount>0 and amount<10000000:
    print ("congratulations you won rupees:",amount)      

