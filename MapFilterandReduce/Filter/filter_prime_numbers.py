def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime_numbers(numbers):
    # Using filter function to keep only the prime numbers in the list
    prime_numbers = list(filter(is_prime, numbers))
    return prime_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_list = filter_prime_numbers(input_list)
print(prime_list)
