'''
Given two lists - one containing keys and another
containing values, create a dictionary using dictionary comprehension.

'''


from typing import List, Any, Dict

def creating_dictionary(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
    """
    Create a dictionary using dictionary comprehension.

    Args:
        keys (List[Any]): List of keys for the dictionary.
        values (List[Any]): List of values for the dictionary.

    Returns:
        Dict[Any, Any]: A dictionary where keys are taken from the 'keys' list
        and values are taken from the 'values' list.
    """
    # Length of both lists is the same, raise value error
    if len(keys) != len(values):
        raise ValueError("The number of keys and values must be the same.")

    dictionary = {keys[i]: values[i] for i in range(len(keys))}

    return dictionary

# two lists
keys_list = ["name", "age", "city"]
values_list = ["John", 30, "New York"]


result_dictionary = creating_dictionary(keys_list, values_list)

print(result_dictionary)
