from functools import reduce

def calculate_factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif number == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, number + 1))

input_number = int(input("Enter any number to calculate the factorial: \t"))
factorial_result = calculate_factorial(input_number)
print(f"The factorial of {input_number} is: {factorial_result}")
