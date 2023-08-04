'''
Given a list of strings, create a new list that contains only the
strings with more than 5 characters using list comprehension.
'''


original_list = ["fusemachines", "ctvt", "artificial", "lpfrg", "trlf", "intellicence", "ekbna", "company"]

# creating a list of elements that contain only those having character more than 5
new_list = [string for string in original_list if len(string) > 5]

print(new_list)
