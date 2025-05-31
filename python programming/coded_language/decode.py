def Decode():
    encoded_sentence = input("Enter the encoded sentence:- ")
    words = encoded_sentence.split()
    print("Decoded sentence is:-", end=" ")

    for word in words:
        trimmed_word=word[3:-3]
        if len(trimmed_word) > 5:
            trimmed_word=word[3:-3]
            original_word = trimmed_word[-2: ] + trimmed_word[0:-5]  
            
        else: 
            trimmed_word=word[3:-3]
            if trimmed_word[0]==trimmed_word[-1]:
                original_word =  trimmed_word[0] 
            else:
                original_word = trimmed_word[-1 ] + trimmed_word[0 ]
    
            

        print(original_word, end=" ")
    print("\n")


