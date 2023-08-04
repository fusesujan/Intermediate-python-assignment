def check_prime(number):
    is_prime = "Prime" if number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)) else "Not Prime"
    return is_prime



input_number = int(input("Enter any number to check if it is prime or not:\t"))
result = check_prime(input_number)
print(f"{input_number} is {result}.")
