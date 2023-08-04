'''
Write a Python function that takes an arbitrary number of positional
arguments and returns the sum of all the numbers. Test your function with various
input cases.
'''

def sum_of_arbitary_numbers(*args):
    sum_result = 0
    for num in args:
        sum_result += num
    return sum_result


test_first = sum_of_arbitary_numbers(10, 20, 30, 40, 50)
print(test_first)

test_second = sum_of_arbitary_numbers()
print(test_second)

print(sum_of_arbitary_numbers(1,-8,5,7,)) 



