'''
Given three lists list1, list2, and list3, each containing
integers, write a Python program using list comprehension to generate a new list of
unique triplets (x, y, z) where x is from list1, y is from list2, and z is from list3, such
that x + y + z = 0. 
'''


def find_unique_triplets(list1, list2, list3):
    triplets = set()
    # List comprehension to find triplets (x, y, z) where x + y + z = 0
    triplets = {(x, y, z) for x in list1 for y in list2 for z in list3 if x + y + z == 0}
    return triplets


list1 = [1, -2, 3]
list2 = [2, -3, 6]
list3 = [-3, 5, 7, -9]

triplet_result = find_unique_triplets(list1, list2, list3)
print(triplet_result)
