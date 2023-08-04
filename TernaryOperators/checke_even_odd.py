def check_odd_even(number):
    result = "Even" if number % 2 == 0 else "Odd"
    return result

input_number = int(input("Enter any number :\t"))
result = check_odd_even(input_number)
print(f"The number {input_number} is: {result}")
