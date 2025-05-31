def decode_word(encoded_word):
    if len(encoded_word) < 6:
        return encoded_word
    
    trimmed_word = encoded_word[3:-3]
    n = len(trimmed_word)
    
    if n > 5:
        return trimmed_word[-2:] + trimmed_word[:n-5]
    else:
        if n == 0:
            return ""
        if trimmed_word[0] == trimmed_word[-1]:
            return trimmed_word[0]
        return trimmed_word[-1] + trimmed_word[0]

def decode_sentence(encoded_sentence):
    words = encoded_sentence.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)