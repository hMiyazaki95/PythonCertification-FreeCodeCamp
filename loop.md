
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


<!-- generate even numbers -->
<!-- if the number is divisible by 2 then the current number will be appended at the end of the list

first, 2 will be added to the empty list -->
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


<!-- more readable  -->
<!-- 
[expression for item in iterable if condition]

| Part                   | Meaning                                      |
| ---------------------- | -------------------------------------------- |
| `num` (first one)      | **The value that will be added to the list** |
| 'num` (second one)     | ** The second num is the loop variable in the for loop.|
| `for num in range(21)` | Loop through numbers 0–20                    |
| `if num % 2 == 0`      | Only keep even numbers                       |


 -->
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

<!-- list comprehension -->
<!-- create a new list of tuples indicating which numbers are even or odd -->
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

<!-- [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')] -->


<!-- The filter() function is used to select elements from an iterable that meet a specific condition. The filter() function accepts a function and an iterable for its arguments. -->

<!-- passing in an is_long_word function into the filter() function to check if the current word count is greater than 4. All words that have a character count greater than 4 are added into a new list and assigned to the long_words variable. -->
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']


List()
map(function, iterable)
filter(function, iterable)

Key difference
| Function   | What it does                                      |
| ---------- | ------------------------------------------------- |
| `map()`    | **changes every element**                         |
| `filter()` | **removes elements that don’t match a condition** |

numbers = [1,2,3,4]

# map → change values
list(map(lambda x: x*2, numbers))
# [2,4,6,8]

# filter → keep some values
list(filter(lambda x: x%2==0, numbers))
# [2,4]


numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50

numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60


numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60


<!-- Alternative way to code the sum function with start argument -->
iterable = [5, 10, 15, 20]
start = 10

total = start
for n in iterable:
    total += n
    print("n =", n, "| total =", total)

print("final total =", total)


Lambda Function - Anonymous Function

- Lambda is only used for simple, short arithmetic or single-expression calculations.

Why do anonymous functions exist?
To avoid creating a separate named function when:
- A function is only used once 
— writing a full def feels unnecessary
- You want to avoid defining a temporary helper function
- Some functions like map(), filter(), and sorted() expect another function as input

Don't use Labmda when 
- the function is long
- the logic is complex
- the function is reused
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]