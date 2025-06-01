def decode(encoded_sentence):
    words = encoded_sentence.split()
    decoded_words = []

    for word in words:
        trimmed_word = word[3:-3]

        if len(trimmed_word) > 5:
            original_word = trimmed_word[-2:] + trimmed_word[0:-5]
        else:
            if trimmed_word[0] == trimmed_word[-1]:
                original_word = trimmed_word[0]
            else:
                original_word = trimmed_word[-1] + trimmed_word[0]

        decoded_words.append(original_word)
    return ' '.join(decoded_words)
