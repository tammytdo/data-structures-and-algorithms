def repeated_word(str):
    split_string = str.lower().split(' ')
    str_words = []

    for word in split_string:
        if word in str_words:
            return word
        str_words.append(word)
        
    return None