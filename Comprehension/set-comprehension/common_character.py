'''
Given two strings, write a Python program to create a set
using set comprehension that contains all the characters that are common in both
strings.

'''


def common_characters_in_strings(str1, str2):
    
    common_chars_set = {char for char in str1 if char in str2}

    return common_chars_set


string1 = input("Enter first string :\t")
string2 = input("Enter second string :\t")

common_characters_set = common_characters_in_strings(string1, string2)

print(common_characters_set)
