def check_leap_year(year):
    result = "Leap Year" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Not a Leap Year"
    return result


input_year = int(input("Enter any year to check if it is leap or not"))
result = check_leap_year(input_year)
print(f"{input_year} is {result}.")
