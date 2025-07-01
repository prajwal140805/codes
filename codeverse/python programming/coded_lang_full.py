import random
import os


def Encode():
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
    print("_______________________________________________________________________________________________ ")


def Decode():
    encoded_sentence = input("Enter the encoded sentence:- ")
    words = encoded_sentence.split()
    print("Decoded sentence is:-", end=" ")

    for word in words:
        trimmed_word = word[3:-3]
        if len(trimmed_word) > 5:
            trimmed_word = word[3:-3]
            original_word = trimmed_word[-2:] + trimmed_word[0:-5]

        else:
            trimmed_word = word[3:-3]
            if trimmed_word[0] == trimmed_word[-1]:
                original_word = trimmed_word[0]
            else:
                original_word = trimmed_word[-1] + trimmed_word[0]

        print(original_word, end=" ")
    print("\n")


print("_______________________________________________________________________________________________ ")
print("*********************************WELCOME TO CODED LANGUAGE*************************************!")
while (True):
    print("Choose an option:", end="")
    print("Choose an option:")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    print("_______________________________________________________________________________________________ ")

    choice = (input())
    os.system('cls')

    if choice == '1':
        Encode()
    elif choice == '2':
        Decode()

    elif choice == '3':
        print("Exitting the program.....")

        break
    else:
        print("Invalid choice! Please try again.....")
        print("_______________________________________________________________________________________________ ")
