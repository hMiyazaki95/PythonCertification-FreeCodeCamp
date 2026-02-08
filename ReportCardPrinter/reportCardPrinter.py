#Create the variable called name and assign Alice to it
#name = 'Alice'

# print the name variable
# print(name) # Output: Hello World

# Use the type() function with name as its argument and print the output like the example.
#print(type(name))

# Boolean values represent a yes-or-no condition, and they are often used to make decisions in code. There are only two boolean values: True and
# Declare a variable named is_student and assign it the value True.
#is_student = True

# Print both is_student and type(is_student) on the same line using a comma , as shown in the example. Then, check the output in the terminal that shows the value of is_student, and its type as bool (boolean).
#print(is_student,type(is_student)) # True <class 'bool'>

# Remove the earlier outputs of the name variable. Then, print name and type(name) together on one line separated by a comma like the previous step.
name = 'Alice'
print(name, type(name))
is_student = True
print(is_student, type(is_student))

# Declare a variable named age and assign it the integer value 20.
age = 20
# Then, print the value and data type of age together separated by a comma. Check the output in the terminal that shows the value of age, and its type as int (integer).
print(age, type(age))

# Output 
# Alice <class 'str'>
# True <class 'bool'>
# 20 <class 'int'>

#Although both age and score are numbers, they may not be the same kind. Python provides a function called isinstance() to check this.
# Declare a variable named score and assign it the value 80.5.
score = 80.5
# Use isinstance() to check whether score is an int, and print the result to the terminal as shown in the example above.
# print(isinstance(score, int)) 
# Output -> False

# Replace int with float in the existing isinstance() call to confirm this.
print(isinstance(score, float))
# Finally, print score and its data type to complete the report card.
print(score, type(score))

### OUTPUT ###
# python3 reportCardPrinter.py
# Alice <class 'str'>
# True <class 'bool'>
# 20 <class 'int'>
# True
# 80.5 <class 'float'>

