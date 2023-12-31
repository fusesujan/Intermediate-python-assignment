'''
Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.

'''



class University:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def display_details(self):
        print(f"University: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f"  - {department.get_name()}")


class Department(University):
    def __init__(self, name, location, head_of_department):
        super().__init__(name, location)
        self._head_of_department = head_of_department
        self._courses_offered = []

    def add_course(self, course):
        self._courses_offered.append(course)

    def get_name(self):
        return f"{self._name} Department"

    def display_details(self):
        print(f"Department: {self._name}")
        print(f"Location: {self._location}")
        print(f"Head of Department: {self._head_of_department}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f"  - {course}")


# Example usage:
if __name__ == "__main__":
    uni = University("Pokhara University", "Mulpani,Bhaktapur")

    department1 = Department("Computer Science", "Building A", "Krishna Bikram Shah")
    department1.add_course("Artificial Intelligence")
    department1.add_course("Database management system")
    uni.add_department(department1)

    department2 = Department("Ict", "Building B", "Madan Raj upreti")
    department2.add_course("Computer Network")
    department2.add_course("Data Communication")
    uni.add_department(department2)

    uni.display_details()
