'''
Write a Python function concat_strings that takes any number of strings as
arguments and returns a single concatenated string.
'''

def string_concat(*args):
    # print(args,"KKKKK")
    concat_result = ''
    for each in args:
        concat_result += each
    return concat_result

print("Taking 3 input from user \n")
print("\nThe output afte concatenating the string is:\t",string_concat(input("first input:\t"), input("second input:\t"),input("third input:\t")))
    