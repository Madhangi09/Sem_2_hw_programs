#1
class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name=",self.name)
class Student(Person):
    def __init__(self,name,stu_id):
        super().__init__(name)
        self.stu_id=stu_id
    def printDetails(self):
        self.display()
        print("Student Id=",self.stu_id)
s=Student('Mad','23')
s.printDetails()


#2

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: {self.name} \nSalary: {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def printDetails(self):
        self.display()
        print("Department:",self.dept)
e=Manager('Mad',100000,'AI')
e.printDetails()
