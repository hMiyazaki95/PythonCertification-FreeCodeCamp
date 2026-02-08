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


Mutable:
lst = [1, 2, 3]
lst[0] = 99      # ✅ works
print(lst)       # [99, 2, 3]

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

my_str = 'Hello world'
print(my_str[8:])  # rld exclude first 8 characters from index 0 to 7 and print characters from index 8 to -1

my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)  # Hello world
Slicing a string Won't Modify the Original String

my_str = 'Hello world'
print(my_str[:])  # Hello world
This slicing prints entire strings 

string[start:stop:step] # optional step parameter


[start:stop number of last character :step each how many string]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
print(my_str[0:11:3]) # Hlwl
python3 python.p
y
Hlwl

Reverse with step parameter:
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH

filename = "report.final.pdf"
extension = filename[::-1].split(".", 1)[0][::-1]
print(extension)  # pdf

this can be helpful to check if the string is Palindrome or not 

can find the file extension

cleaner, faster, and more pythonic than for loop

Comming String Methods:

.uppper() -> make all string uppercase
.lower() -> make string all lowercase
.strip() -> remove space
.replace(old, new) -> example .replace('hello', 'hi') -> replace the hellow with hi
.sprit() -> this split the word for exmaple -> ['hello', 'world']


join = connect elements together into a single string, using a separator

my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world


.startswith(prefix)
returns boolean indicating if a string starts with the specified prefix 

.endswith(suffix)
Returns a boolean indicating if a string ends with the specified suffix.

.find(substring)
Returns the index of the first occurrence (first string) of substring, or -1 if it doesn't find one.
Example:
world_index = my_str.find('world')
print(world_index)  # 6

.count(substring)
Returns the number of times a substring appears in a string

.capitalize()
Returns a new string with the first character capitalized and the other characters lowercased.

.isupper()
Return True if all letters in the string are uppercase and False if not.

.islower()
Returns True if all letters in the string are lowercase and False if not.

.title()
Returns a new string with the first letter of each word capitalized.

