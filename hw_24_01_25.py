a = int(input(" Enter the no1:")) 
b = int(input(" Enter the no2:")) 
c = int(input(" Enter the no3:")) 
addition = a + b + c 
subtraction = a - b - c 
print(f"Addition – {addition}") 
print(f"Subtraction - {subtraction}") 
a = a ^ b 
b = a ^ b 
a = a ^ b 
b = b ^ c 
c = b ^ c 
b = b ^ c 
print("Before Swapping") 
print(f"First value – {a}") 
print(f"Second value – {b}") 
print(f"Third Value – {c}") 
print("After Swapping ") 
print(f"First value – {b}") 
print(f"Second Value – {c}") 
print(f"Third Value – {a}") 


name = input("Enter Name: ") 
print(f"Hi ! Your Entered Input is \"{name}\"") 
import re 
char = ''.join(re.findall(r'[a-zA-Z]', name)) 
spec_char = ''.join(re.findall(r'[^a-zA-Z0-9]', name)) 
print(f"Your entered Characters are – {char}") 
print(f"Your entered Special Characters are – {spec_char}")
