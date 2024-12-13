class Student:
    def __init__(self):  # Corrected the method name to __init__
        self.student_id = input("Enter the student ID (e.g., STU1234): ")
        self.name = input("Enter the student's name: ")
        self.grade = input("Enter the student's grade (e.g., 5th Grade): ")

    def valid_id(self):
        # Check if student ID is in the format "STU1234"
        if len(self.student_id) == 7 and self.student_id[:3] == "STU" and self.student_id[3:].isdigit():
            print("Valid student ID")
        else:
            print("Invalid student ID. It must start with 'STU' followed by 4 digits.")

    def valid_name(self):
        # Check if name is at least 2 characters long and contains only alphabets and spaces
        if len(self.name) >= 2 and all(char.isalpha() or char.isspace() for char in self.name):
            print("Valid name")
        else:
            print("Invalid name. Name must be at least 2 characters long and contain only alphabets and spaces.")

    def valid_grade(self):
        # Check if grade is in the format "Xth Grade" where X is a number between 1 and 12
        parts = self.grade.split(' ')
        if len(parts) == 2 and parts[1].lower() == "grade" and parts[0][:-2].isdigit():
            number = int(parts[0][:-2])  # Extract the grade number
            if 1 <= number <= 12:
                print("Valid grade")
            else:
                print("Invalid grade. Grade must be between 1 and 12.")
        else:
            print("Invalid grade. It must be in the format 'Xth Grade'.")

    def display(self):
        # Display the student's details
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grade: {self.grade}")

# Main program execution
s = Student()  # Create an instance of the Student class
s.valid_id()  # Validate student ID
s.valid_name()  # Validate student name
s.valid_grade()  # Validate student grade
s.display()  # Display student details

