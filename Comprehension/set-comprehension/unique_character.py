'''

Given a list of words, write a Python program to create a set
using set comprehension that contains all the unique characters present in the
words.

'''


def unique_characters_in_words(words):
   
    # Set comprehension 
    unique_chars_set = {char for word in words for char in word}

    return unique_chars_set

words_list = ["Sujan", "Sharma", "Bhattarai", "IamvalidSB"]

# Get the set of unique characters from the list of words
unique_characters_set = unique_characters_in_words(words_list)

print(unique_characters_set)
