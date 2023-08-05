'''
Create a function create_student_report that takes the student's
name as the first argument, the student's age as the second argument, and an
arbitrary number of keyword arguments for the subjects and their respective
scores. The function should return a dictionary with the student's information and a
list of subjects along with their scores.
'''


def create_student_report(name, age, **kwargs):
    student_info = {
        'Name': name,
        'Age': age,
    }

    subjects = []
    scores = []

    for subject, score in kwargs.items():
        subjects.append(subject)
        scores.append(score)

    report = {
        'Student Info': student_info,
        'Subjects': subjects,
        'Scores': scores,
    }

    return report

# Example usage:
report = create_student_report('John', 20, Math=95, English=88, Science=92)
print(report)
