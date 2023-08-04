'''

[**kwargs] Write a Python function calculate_total_cost that calculates the total
cost of items purchased from a store. The function should accept multiple keyword
arguments, where the key is the item name, and the value is the item's price. The
function should return the total cost of all items.

'''


def calculate_total_cost(**kwargs):
    total_cost = 0
    i=1
    for item, price in kwargs.items():
        print(i,")",item)
        total_cost += price
        i+=1
    return total_cost


total_cost = calculate_total_cost(apple=200, banana=80, mango= 220)
print(f"Total cost: रु {total_cost}")
