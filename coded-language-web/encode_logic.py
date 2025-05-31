import random

def encode_word(word):
    if not word:
        return ""
    
    # Generate random letters
    start_letters = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    end_letters = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    mid_letters = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    
    if len(word) > 2:
        return start_letters + word[2:] + mid_letters + word[:2] + end_letters
    elif len(word) == 2:
        return start_letters + word[1] + mid_letters + word[0] + end_letters
    else:  # Single character
        return start_letters + word[0] + mid_letters + word[0] + end_letters

def encode_sentence(sentence):
    words = sentence.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)