variable = 3.1
print(variable)
print(isinstance(score, float))
# check if the variable is int in this case
# isinstance(value, type)
# if the not the function returns false
print(isInstance(variable, int)) 
# show type and print type
print(variable, type(variable))
# isinstance(5, int)        # True
# isinstance(3.14, float)  # True
# isinstance(True, bool)   # True
# isinstance("hi", str)    # True


Reassignment:
✅ s = "hello" → s = "hallo" → s = 2 → all valid
Immutability
❌ s[1] = "a" → invalid (string immutability)

Interpolation:  use f string

name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15

print(my_str[0])  # H first character
print(my_str[6])  # w
print(my_str[-1]) # d last character

String Slicing
string[start:stop]

my_str = 'Hello world'
print(my_str[1:4]) # ell 1 to before 4

my_str = 'Hello world'
print(my_str[:7])  # Hello w beginning to before 7
