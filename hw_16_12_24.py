#1
class User:
    def __init__(self,username,password):
        self._username=username
        self.set_password(password)
    def set_password(self,password):
        if len(password)>=8 and any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
            self._password=password
        else:
            raise ValueError("Password must be at least 8 characters long, include a number, and a special character")
    def check_password(self,input_password):
        return self._password==input_password


#2
class Product:
    def __init__(self,name,price,stock):
        self._name=name
        self.set_price(price)
        self.set_stock(stock)
    def set_price(self, price):
        if price>0:
            self._price=price
        else:
            raise ValueError("Price must be greater than 0")
    def set_stock(self,stock):
        if isinstance(stock,int) and stock>=0:
            self._stock=stock
        else:
            raise ValueError("Stock must be a non-negative integer")
    def get_stock(self):
        return self._stock


#3
class Student:
    def __init__(self,name,age,marks):
        self._name=name
        self.set_age(age)
        self.set_marks(marks)
    def set_age(self,age):
        if 5<=age<=100:
            self._age=age
        else:
            raise ValueError("Age must be between 5 and 100")
    def set_marks(self,marks):
        if 0<=marks<=100:
            self._marks=marks
        else:
            raise ValueError("Marks must be between 0 and 100")
    def get_details(self):
        return self._name,self._age,self._marks


# Example usage
try:
    user=User("Mad","Password1!")
    print(user.check_password("Password1!"))  # True

    product=Product("Laptop",1200,5)
    print(product.get_stock())  # 5

    student=Student("Ani",16,85)
    print(student.get_details())  
except ValueError as e:
    print(e)
