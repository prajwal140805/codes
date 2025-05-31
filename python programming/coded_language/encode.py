import random
import os
sentence = input("Enter a sentence:-")
words = sentence.split()
os.system('cls')
print("The code for this is:-", end=" ")

for word in words:
    start_letter = ""
    for i in range(3):

        num = random.randint(1, 26)
        letter = chr(num+96)
        start_letter += letter
    end_letter = ""
    for i in range(3):
        num = random.randint(1, 26)
        letter = chr(num+96)
        end_letter += letter
    mid_letter = ""
    for i in range(3):
        num = random.randint(1, 26)
        letter = chr(num+96)
        mid_letter += letter
        if len(word) > 2:
            modified_word = start_letter + \
                word[2:]+mid_letter+word[0:2]+end_letter

        else:
            if len(word) == 2:
                modified_word = start_letter + \
                    word[1]+mid_letter+word[0]+end_letter
            else:
                modified_word = start_letter + \
                    word[0]+mid_letter+word[0]+end_letter

    print(modified_word, end=" ")
print("\n")
