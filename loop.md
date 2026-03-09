
<!-- Iterate the list of strings using loop -->
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

Rust
Java
Python
C++

<!-- Iterate the char in the string -->

for char in 'code':
    print(char)
c
o
d
e


<!-- Nested for loop -->

categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)

<!-- Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana -->

<!-- While loop -->
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!') // input 3


<!-- 
Exmaple result
Guess the number (1-5): 2
Wrong! Try again.
Guess the number (1-5): 1
Wrong! Try again.
Guess the number (1-5): 3
You got it! -->

<!-- break statement -->
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

<!-- 
result
Naomi -->

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

<!-- Result -->
program checks if developer is equal to Naomi then continue instead of printing so continue skips the Naomi and print rest of element in the list

Jess
Tom

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")



for num in range(1, 5):
    print(num)

1 = index 0
5 = not inclusive
1 2 3 4

<!-- third argument is the number inclement  -->
for num in range(2, 11, 2):
    print(num)

Range function only accept the Intergiers

for num in range(40, 0, -10):
    print(num)

<!-- decrement by 10 from 40
40 30 20 10
 -->

<!-- the list constructor is used to convert an iterable into a list -->

numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]


keep track of the indext for each element

languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

Instead of doing above you can use the enumerate() function

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
<!-- 
[(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')] 
-->

refactored version

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
<!-- 
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese 
-->


Enumerate and Zip Functions

<!-- Basic for loop to iterate list -->
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for language in languages:
    print(language)

<!-- track index by incrementing index variable in loop -->

languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0

for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

<!-- use enumerate function to group the index and element in the list and convert its returned value into a list with the list() function-->

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))

# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

<!-- This Python code loops through a list of languages using enumerate() to get both the index (position) and the language name, and prints them together for each item. -->


languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

<!-- we can add the value of starting index as a argument in the enumerate() which start at 0 as a default value -->
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages, 1): 
    print(f'Index {index} and language {language}')

<!-- zip function will iterate over multiple iterables in parallel-->

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

<!-- using the zip() function  in for loop-->
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')



<!-- Questions

What does the enumerate() function do?


It is used to print the memory addresses for each element in a list.

It is used to create tuples and sets from lists and return an enumerate object.

It is used to keep track of the index of an iterable and return an enumerate object.

It is used to speed up the performance for your Python applications.

Which of the following optional arguments in the enumerate() function specifies the starting value for the count?


set

position

start

count

What does the zip() function do?


It is used to iterate over multiple iterables in parallel.

It is used to create zip files.

It is used to break out of a nested loop.

It is used to create an iterable that saves memory starting from a list.
-->