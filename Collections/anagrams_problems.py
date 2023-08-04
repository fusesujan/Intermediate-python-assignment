'''

Given an array of strings (str), group the anagrams together. You can return the
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

'''

from collections import defaultdict

def group_anagrams(words):
    """
    Group the anagrams together in the array of strings.

    Args:
        words (List[str]): List of strings.

    Returns:
        List[List[str]]: List of lists containing grouped anagrams.
    """
    anagrams_map = defaultdict(list)

    for word in words:
        sorted_word = tuple(sorted(word))
        anagrams_map[sorted_word].append(word)

    # Convert the values of the defaultdict to get the grouped anagrams
    grouped_anagrams = list(anagrams_map.values())

    return grouped_anagrams
words_array = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(words_array)

print(result)
