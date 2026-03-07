
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







