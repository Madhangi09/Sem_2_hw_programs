#1
class StringCounter:
    def __init__(self, input_string):
        self.input_string = input_string
    def count_characters(self):
        alphabetic = sum(1 for char in self.input_string if char.isalpha())
        numeric = sum(1 for char in self.input_string if char.isdigit())
        special = len(self.input_string) - (alphabetic + numeric)
        return alphabetic, numeric, special
# Input from the user
input_string = input("Enter a string: ")
# Create an object of StringCounter
counter = StringCounter(input_string)
# Get the counts of alphabetic, numeric, and special characters
alphabetic, numeric, special = counter.count_characters()
# Output the results
print(f"Alphabetic Characters: {alphabetic}")
print(f"Numeric Characters: {numeric}")
print(f"Special Characters: {special}")

#2
class StringValidator:
    def __init__(self, input_string):
        self.input_string = input_string
    def validate(self):
        has_alpha = False
        has_special = False
        for char in self.input_string:
            if char.isalpha():
                has_alpha = True
            elif not char.isalnum():  # Non-alphanumeric characters are considered special
                has_special = True
        return has_alpha and has_special
# Input from the user
input_string = input("Enter a string: ")
# Create an object of StringValidator
validator = StringValidator(input_string)
# Check if the string contains both alphabetic and special characters
if validator.validate():
    print("The string contains both alphabets and special characters.")
else:
    print("The string does not contain both alphabets and special characters.")

