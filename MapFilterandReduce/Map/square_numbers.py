'''

[map] Write a Python function square_numbers that takes a list of integers as
input and uses the map function to return a new list containing the square of each
element.

'''

def give_square(userlist):
    # square_list = []
    # for i in userlist:
    #     square_list.append(i*i)
    # OR using list Comprehension
    square_list=list(map(lambda x: x ** 2, userlist))
    return square_list


def take_user_input():
    numbers = []
    print("Enter an number (or 'q'/'Q' to finish): ")
    while True:
        try:
            user_input = input()
            if user_input.lower() == 'q':
                break
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter an Number.")

    return numbers

input_numbers = take_user_input()
print(give_square(input_numbers))
