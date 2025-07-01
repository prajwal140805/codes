import random

def encode(sentence):
    words = sentence.split()
    result = []

    for word in words:
        start_letter = ''.join([chr(random.randint(97, 122)) for _ in range(3)])
        end_letter = ''.join([chr(random.randint(97, 122)) for _ in range(3)])
        mid_letter = ''.join([chr(random.randint(97, 122)) for _ in range(3)])

        if len(word) > 2:
            modified_word = start_letter + word[2:] + mid_letter + word[0:2] + end_letter
        elif len(word) == 2:
            modified_word = start_letter + word[1] + mid_letter + word[0] + end_letter
        else:
            modified_word = start_letter + word[0] + mid_letter + word[0] + end_letter

        result.append(modified_word)
    return ' '.join(result)
