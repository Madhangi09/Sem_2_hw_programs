#1without class
n_name=input("Enter the student name:")
n_rollno=int(input("Enter the Roll No.:"))
s=int(input("Enter the marks 1:"))
a=int(input("Enter the marks 2:"))
b=int(input("Enter the marks 3:"))
c=int(input("Enter the marks 4:"))
d=int(input("Enter the marks 5:"))
tot=a+b+c+d+e
per=(tot/500)*100
if per>=85:
    print("Grade S")
elif per>=75:
    print("Grade A")
elif per>=65:
    print("Grade B")
elif per>=55:
    print("Grade C")
elif per>=50:
    print("Grade D")
else:
    print("Invalid Input")

#1with class
class Student:
    def __init__(self,name,rollno,mark1,mark2,mark3):
        self.name=name
        self.rollno=rollno
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.per=((mark1+mark2+mark3)/3)*100
    def grade(self):
        if self.per>=85:
            print("grade is S")
        elif self.per>=75:
            print("grade is A")
        elif self.per>=65:
            print("grade is B")
        elif self.per>55:
            print("grade is C")
        elif self.per>=50:
            print("grade is D")
        else:
            print("Invalid Input")
obj=Student("Mad",23,78,89,90)
obj.grade()



#2
class Student:
    def __init__(self,name,age,course,grade):  #self is the current instance of the class
        self.name=name
        self.age=age
        self.course=course
        self.grade=grade
    def show(self):
        print(f"student Details-Student Name {self.name},Student Age {self.age},Student Course {self.course},Student Grade {self.grade}")
    def __del__(self):
        print("ALL DETAILS ARE DELETED")
n=Student("Mad",17,"AI","A")
n.show()
del n
