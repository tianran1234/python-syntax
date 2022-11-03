def print_upper_words(words):
    """print out each word on a separate line, but in all uppercase"""
    for word in words:
        print(word.upper())

def print_upper_words(words):
    for word in words:
        if word.upper().startswith("E"):
             print(word.upper())

def print_upper_words(words,must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.upper().startswith(letter.upper()):
                print(word.upper())
       
