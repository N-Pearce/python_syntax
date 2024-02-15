def print_upper_words(words, must_start_with):
    '''Given list of words, print each word in uppercase'''

    for word in words:
        word = word.upper()
        for letter in must_start_with:
            if word.startswith(letter.upper()):
                print(word)

print_upper_words(['blue', 'red', 'green', 'elephant'], must_start_with = {'g', 'r'})