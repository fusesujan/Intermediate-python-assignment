from typing import Dict

'''
Given a dictionary with students' names as keys and
their respective scores as values, create a new dictionary that contains only the
students who scored more than 80 using dictionary comprehension.

'''

def filter_students_by_score(students_scores: Dict[str, int], threshold: int) -> Dict[str, int]:
    """
    Filter students by their scores.

    Args:
        students_scores (Dict[str, int]): A dictionary with students' names as keys and their scores as values.
        threshold (integer): The minimum score required for a student to be included in the new dictionary.

    Returns:
        Dict[str, int]: A dictionary containing students who scored more than the specified threshold.
    """

    filtered_students = {name: score for name, score in students_scores.items() if score > threshold}

    return filtered_students

students_scores_dict = {
    "John": 85,
    "Alice": 78,
    "Bob": 92,
    "Jane": 95,
    "Mike": 80
}

# Filter students with scores more than 80
filtered_students_dict = filter_students_by_score(students_scores_dict, 80)

print(filtered_students_dict)
