'''
Given two lists of integers, create a list that contains the
product of each element of the first list with the corresponding element in the
second list using list comprehension.
'''

def get_element(size):
    user_list = []
    for i in range(size):
        user_input = int(input(f"Enter element {i + 1}: "))
        user_list.append(user_input)
    return user_list


# takng the size of the list from user input
len_input = int(input("enter the length of list"))

print("For List 1")
listone = get_element(len_input)

print("For List 2")
listtwo = get_element(len_input)

products_list = [x * y for x, y in zip(listone, listtwo)]

print("The final product of each element of those two list is: ",products_list)

