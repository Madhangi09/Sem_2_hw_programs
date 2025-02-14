class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")
    def calculate_yearly_salary(self):
        return self.salary * 12
emp1 = Employee("John", 101, 5000)
emp1.display_info()
print("Yearly Salary:", emp1.calculate_yearly_salary())
