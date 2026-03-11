# Daily Review Questions — Python Concepts

Review one section per day, or shuffle through all of them. For each question, answer out loud or write it down before checking the answer.

---

## 1. Variables & Data Types

**Definition**
- What is a variable in Python?
- What does it mean that Python is dynamically typed?
- Name the 5 common data types in Python.

**Syntax**
- How do you declare a variable named `age` with value `25`?
- What naming convention does Python use for variables?

**Output — What does this print?**
```python
x = 10
y = "10"
print(type(x))
print(type(y))
```

**When / Why**
- When would you use an `int` vs a `float`?
- Why is it important to know the type of a variable?

---

## 2. Strings

**Definition**
- What is a string in Python?
- What does "immutable" mean for strings?

**Syntax**
- How do you create a multi-line string?
- How do you use an f-string? Write an example with a variable `name`.

**Output — What does this print?**
```python
s = "Hello World"
print(s[0])
print(s[-1])
print(s[1:5])
print(s[::-1])
print(s.lower())
print(s.upper())
print(s.replace("World", "Python"))
print(s.split())
print(len(s))
```

**When / Why**
- When would you use `.strip()`?
- When would you use `.split()`?
- Why can't you change a character in a string directly like `s[0] = "h"`?

**String Methods — Fill in the blank**
- `"hello".______()` → `"HELLO"`
- `"  hi  ".______()` → `"hi"`
- `"hello world".______(separator)` → `['hello', 'world']`
- `['a', 'b'].______('-')` → `"a-b"` ← fix the syntax
- `"hello".______(2)` → `"llo"` ← what kind of operation is this?
- `"hello world".______('o')` → `2`
- `"hello".______(prefix)` → `True/False`

---

## 3. String Slicing

**Definition**
- What is string slicing?
- What is the syntax for slicing?

**Output — What does this print?**
```python
s = "Hello World"
print(s[2:])
print(s[:4])
print(s[0:11:2])
print(s[::-1])
print(s[::1])
```

**When / Why**
- When would you use `[::-1]`?
- When would you omit the start or stop index?
- Does slicing modify the original string? Why or why not?

---

## 4. Numbers & Math Operations

**Syntax — What is the operator for each?**
- Addition
- Subtraction
- Multiplication
- Division (returns float)
- Floor Division (returns int)
- Modulo (remainder)
- Exponent

**Output — What does this print?**
```python
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 4)
print(type(10 / 2))
print(type(10 // 2))
```

**When / Why**
- When would you use `%` (modulo)?
- When would you use `//` vs `/`?
- What are augmented assignment operators? Give 3 examples.

---

## 5. Booleans & Conditionals

**Definition**
- What are the only two values a boolean can have?
- What is a falsy value? List all falsy values in Python.
- What is a truthy value? Give 3 examples.

**Output — What does this print?**
```python
print(bool(0))
print(bool(""))
print(bool(None))
print(bool("False"))
print(bool([]))
print(bool(1))
print(not True)
print(not 0)
```

**Logical Operators**
- What does `and` return when the first operand is falsy?
- What does `or` return when the first operand is truthy?
- What does `not` always return?

**Output — What does this print?**
```python
print(True and 25)
print(False and 25)
print(0 or "hello")
print("hi" or "bye")
print(not "")
print(not "hello")
```

**Conditionals — What is printed?**
```python
age = 15
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")
```

**When / Why**
- When would you use `elif` vs multiple `if` statements?
- When would you use `and` vs nested `if` statements?
- Why use `not` in a conditional?

---

## 6. Functions & Scope

**Definition**
- What is a function?
- What is the difference between a parameter and an argument?
- What does `return` do?
- What does a function return if you don't write `return`?

**Syntax**
- Write a function `add(a, b)` that returns the sum.
- How do you call a function?
- What keyword defines a function?

**Output — What does this print?**
```python
def greet(name):
    print(f"Hello, {name}")

def add(a, b):
    return a + b

result = greet("Alice")
print(result)
print(add(3, 4))
```

**Scope**
- What is a local variable?
- What is a global variable?
- Can a function access a variable defined outside it? What about the reverse?

**When / Why**
- Why use functions instead of writing all code in one place?
- When would you use `return` vs `print` inside a function?

---

## 7. Lists

**Definition**
- What is a list?
- Is a list mutable or immutable?
- What indexing does a list use?

**Syntax**
- How do you create an empty list?
- How do you access the last element without knowing the length?
- How do you update the first element of a list?
- How do you delete an element at index 2?
- How do you check if `"Python"` is in a list?

**Output — What does this print?**
```python
cities = ['LA', 'London', 'Tokyo']
print(cities[0])
print(cities[-1])
print(cities[1:])
print(len(cities))
cities[0] = 'NYC'
print(cities)
del cities[1]
print(cities)
print('Tokyo' in cities)
```

**List Unpacking**
- What does unpacking do?
- What does `*rest` do in unpacking?

**Output — What does this print?**
```python
data = ['Alice', 25, 'Engineer']
name, *rest = data
print(name)
print(rest)
```

**When / Why**
- When would you use a list instead of a string?
- When would negative indexing be useful?

---

## 8. Common List Methods

**Fill in the blank — What method does each?**
- Add an element to the end: `list._______(item)`
- Remove and return the last element: `list._______()`
- Remove and return element at index: `list._______(index)`
- Insert at a specific index: `list._______(index, item)`
- Return the index of an element: `list._______(item)`
- Count occurrences of an element: `list._______(item)`
- Sort the list in place: `list._______()`
- Reverse the list in place: `list._______()`
- Add all items from another list: `list._______(other_list)`
- Remove first occurrence of value: `list._______(value)`
- Return a sorted copy (without modifying): `_______(list)`

**Output — What does this print?**
```python
nums = [3, 1, 4, 1, 5]
nums.append(9)
print(nums)
nums.sort()
print(nums)
print(nums.count(1))
print(nums.index(4))
nums.pop()
print(nums)
```

---

## 9. Tuples

**Definition**
- What is a tuple?
- What is the key difference between a list and a tuple?
- Can you change an element in a tuple?

**Syntax**
- How do you create a tuple with 3 elements?
- How do you create a tuple with only 1 element? (tricky!)

**Output — What does this print?**
```python
t = (10, 20, 30)
print(t[0])
print(t[-1])
print(len(t))
print(t.count(10))
print(t.index(20))
```

**When / Why**
- When would you use a tuple instead of a list?
- Why are tuples useful as dictionary keys but lists are not?

---

## 10. Loops

**Definition**
- What is a `for` loop used for?
- What is a `while` loop used for?
- What does `break` do?
- What does `continue` do?

**Output — What does this print?**
```python
for i in range(5):
    print(i)
```

```python
for i in range(2, 10, 2):
    print(i)
```

```python
for i in range(40, 0, -10):
    print(i)
```

```python
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    if name == 'Bob':
        break
    print(name)
```

```python
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    if name == 'Bob':
        continue
    print(name)
```

**Range**
- What are the 3 arguments of `range()`?
- What does `range(5)` produce?
- Is the stop value inclusive or exclusive?
- How do you create a list from a range?

**When / Why**
- When would you use `while` instead of `for`?
- When would you use `break`?
- When would you use `continue`?

---

## 11. `enumerate()` & `zip()`

**Definition**
- What does `enumerate()` do?
- What does `zip()` do?
- What type does `enumerate()` return?

**Output — What does this print?**
```python
langs = ['Python', 'Java', 'Rust']
for index, lang in enumerate(langs):
    print(index, lang)
```

```python
langs = ['Python', 'Java', 'Rust']
for index, lang in enumerate(langs, 1):
    print(index, lang)
```

```python
names = ['Alice', 'Bob']
ids = [101, 102]
for name, id in zip(names, ids):
    print(name, id)
```

**When / Why**
- When would you use `enumerate()` instead of a manual index counter?
- When would you use `zip()`?
- What happens if the two lists passed to `zip()` have different lengths?

---

## 12. List Comprehensions

**Definition**
- What is a list comprehension?
- What is the basic syntax?

**Rewrite with list comprehension**
```python
# Rewrite this:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
```

**Output — What does this print?**
```python
evens = [n for n in range(10) if n % 2 == 0]
print(evens)
```

```python
nums = [1, 2, 3, 4, 5]
result = [(n, 'Even') if n % 2 == 0 else (n, 'Odd') for n in nums]
print(result)
```

**When / Why**
- When is a list comprehension better than a `for` loop?
- When might a regular `for` loop be better than a list comprehension?

---

## 13. `map()`, `filter()`, `sum()`

**Definition**
- What does `map()` do?
- What does `filter()` do?
- What is the key difference between `map()` and `filter()`?
- What does `sum()` do?

**Syntax**
- What two arguments does `map()` take?
- What two arguments does `filter()` take?
- What is the optional second argument to `sum()`?

**Output — What does this print?**
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
```

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

```python
print(sum([5, 10, 15]))
print(sum([5, 10, 15], 10))
```

**When / Why**
- When would you use `map()` over a list comprehension?
- When would you use `filter()` over a list comprehension?
- When would you use `sum()` vs a `for` loop with a counter?

---

## 14. Lambda Functions

**Definition**
- What is a lambda function?
- What is another name for a lambda function, and why?
- What kind of calculations is lambda only used for?

**Syntax**
- What is the syntax for a lambda function?
- How is a lambda different from a `def` function?
- Can a lambda have multiple lines? Why or why not?

**Rewrite using lambda**
```python
# Rewrite this as a lambda:
def double(x):
    return x * 2
```

**Output — What does this print?**
```python
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)
```

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
```

```python
add = lambda a, b: a + b
print(add(3, 4))
```

**When / Why**
- When should you use a lambda instead of a `def`?
- When should you NOT use a lambda? (3 cases)
- Why does `map()` / `filter()` / `sorted()` work well with lambda?

**Don't use lambda when:**
- The function is ______
- The logic is ______
- The function is ______

---

## 16. Output Challenge — Read & Predict

Before running, write down what each block prints:

```python
# Block 1
words = ['cat', 'elephant', 'dog', 'rhinoceros']
long = [w for w in words if len(w) > 4]
print(long)
```

```python
# Block 2
nums = [10, 20, 30]
a, *b = nums
print(a)
print(b)
```

```python
# Block 3
s = "racecar"
print(s == s[::-1])
```

```python
# Block 4
pairs = list(zip([1, 2, 3], ['a', 'b', 'c']))
print(pairs)
```

```python
# Block 5
total = sum([x for x in range(1, 6)])
print(total)
```

---

## 17. Coding Interview Questions

Practice by writing the solution on paper or in a blank file first. Then run it to verify.

---

### Strings

**Q1.** Write a function that reverses a string without using `[::-1]`.
```python
def reverse_string(s):
    # your code here

print(reverse_string("hello"))   # "olleh"
print(reverse_string("Python"))  # "nohtyP"
```

**Q2.** Write a function that checks if a string is a palindrome. Ignore spaces and casing.
```python
def is_palindrome(s):
    # your code here

print(is_palindrome("racecar"))          # True
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))            # False
```

**Q3.** Write a function that counts how many vowels are in a string.
```python
def count_vowels(s):
    # your code here

print(count_vowels("hello"))   # 2
print(count_vowels("Python"))  # 1
print(count_vowels("aeiou"))   # 5
```

**Q4.** Write a function that returns the most repeated character in a string.
```python
def most_repeated(s):
    # your code here

print(most_repeated("aabbccc"))  # "c"
print(most_repeated("hello"))    # "l"
```

**Q5.** Write a function that checks if two strings are anagrams of each other.
```python
def is_anagram(s1, s2):
    # your code here

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```

**Q6.** Write a function that capitalizes the first letter of every word in a sentence without using `.title()`.
```python
def capitalize_words(s):
    # your code here

print(capitalize_words("hello world"))       # "Hello World"
print(capitalize_words("i love python"))     # "I Love Python"
```

**Q7.** Write a function that removes all spaces from a string.
```python
def remove_spaces(s):
    # your code here

print(remove_spaces("hello world"))   # "helloworld"
print(remove_spaces("a b c d"))       # "abcd"
```

**Q8.** Write a function that returns `True` if a string contains only digits.
```python
def is_all_digits(s):
    # your code here

print(is_all_digits("12345"))   # True
print(is_all_digits("123a5"))   # False
```

**Q9.** Write a function that counts how many times a word appears in a sentence.
```python
def count_word(sentence, word):
    # your code here

print(count_word("the cat sat on the mat", "the"))  # 2
print(count_word("hello hello hello", "hello"))      # 3
```

**Q10.** Write a function that reverses only the words in a sentence, not the letters.
```python
def reverse_words(s):
    # your code here

print(reverse_words("Hello World"))        # "World Hello"
print(reverse_words("I love Python"))      # "Python love I"
```

---

### Numbers & Math

**Q11.** Write a function that returns `True` if a number is even, `False` if odd.
```python
def is_even(n):
    # your code here

print(is_even(4))   # True
print(is_even(7))   # False
```

**Q12.** Write a function that returns the sum of all digits in a number.
```python
def digit_sum(n):
    # your code here

print(digit_sum(123))   # 6
print(digit_sum(9999))  # 36
```

**Q13.** Write a function that returns `True` if a number is a palindrome (reads the same forward and backward).
```python
def is_palindrome_num(n):
    # your code here

print(is_palindrome_num(121))   # True
print(is_palindrome_num(123))   # False
print(is_palindrome_num(1221))  # True
```

**Q14.** Write a function that returns all multiples of `n` up to `limit`.
```python
def multiples_of(n, limit):
    # your code here

print(multiples_of(3, 20))  # [3, 6, 9, 12, 15, 18]
print(multiples_of(5, 30))  # [5, 10, 15, 20, 25, 30]
```

**Q15.** FizzBuzz — Write a function that prints numbers 1 to n. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", for both print "FizzBuzz".
```python
def fizzbuzz(n):
    # your code here

fizzbuzz(15)
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
```

**Q16.** Write a function that returns the factorial of a number using a loop.
```python
def factorial(n):
    # your code here

print(factorial(5))  # 120
print(factorial(3))  # 6
```

---

### Lists

**Q17.** Write a function that returns the largest number in a list without using `max()`.
```python
def find_max(nums):
    # your code here

print(find_max([3, 1, 4, 1, 5, 9, 2]))  # 9
print(find_max([10, 20, 5, 30]))         # 30
```

**Q18.** Write a function that returns the second largest number in a list.
```python
def second_largest(nums):
    # your code here

print(second_largest([3, 1, 4, 1, 5, 9]))  # 5
print(second_largest([10, 20, 5, 30]))      # 20
```

**Q19.** Write a function that removes all duplicates from a list and returns the unique values.
```python
def remove_duplicates(lst):
    # your code here

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates(["a", "b", "a", "c"]))    # ["a", "b", "c"]
```

**Q20.** Write a function that flattens a nested list (one level deep).
```python
def flatten(lst):
    # your code here

print(flatten([[1, 2], [3, 4], [5]]))  # [1, 2, 3, 4, 5]
```

**Q21.** Write a function that returns `True` if a list is sorted in ascending order.
```python
def is_sorted(lst):
    # your code here

print(is_sorted([1, 2, 3, 4, 5]))   # True
print(is_sorted([1, 3, 2, 4, 5]))   # False
```

**Q22.** Write a function that rotates a list to the right by `k` positions.
```python
def rotate_right(lst, k):
    # your code here

print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(rotate_right([1, 2, 3], 1))         # [3, 1, 2]
```

**Q23.** Write a function that returns the intersection (common elements) of two lists.
```python
def intersection(lst1, lst2):
    # your code here

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
print(intersection(["a", "b"], ["b", "c"]))        # ["b"]
```

**Q24.** Write a function that returns the sum of all even numbers in a list.
```python
def sum_evens(lst):
    # your code here

print(sum_evens([1, 2, 3, 4, 5, 6]))  # 12
print(sum_evens([10, 15, 20, 25]))     # 30
```

**Q25.** Write a function that counts how many times a value appears in a list without using `.count()`.
```python
def count_occurrences(lst, value):
    # your code here

print(count_occurrences([1, 2, 2, 3, 2], 2))       # 3
print(count_occurrences(["a", "b", "a"], "a"))      # 2
```

**Q26.** Write a function that returns a new list with each element squared.
```python
def square_all(lst):
    # your code here

print(square_all([1, 2, 3, 4]))  # [1, 4, 9, 16]
print(square_all([5, 10]))       # [25, 100]
```

**Q27.** Write a function that moves all zeros in a list to the end while keeping the order of other elements.
```python
def move_zeros(lst):
    # your code here

print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeros([0, 0, 1]))         # [1, 0, 0]
```

**Q28.** Write a function that returns the running sum of a list. Each element is the sum of all elements up to that index.
```python
def running_sum(lst):
    # your code here

print(running_sum([1, 2, 3, 4]))  # [1, 3, 6, 10]
print(running_sum([1, 1, 1, 1]))  # [1, 2, 3, 4]
```

---

### Loops & Range

**Q29.** Write a function that prints a multiplication table for a given number `n` (1 to 10).
```python
def times_table(n):
    # your code here

times_table(3)
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30
```

**Q30.** Write a function that returns the count of consecutive 1s in a list.
```python
def max_consecutive_ones(lst):
    # your code here

print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))  # 3
print(max_consecutive_ones([1, 0, 1, 1, 0, 1]))  # 2
```

**Q31.** Write a function using a `while` loop that returns the number of digits in an integer.
```python
def count_digits(n):
    # your code here

print(count_digits(12345))  # 5
print(count_digits(9))      # 1
```

**Q32.** Write a function that prints a number pattern like this for `n=4`:
```
1
1 2
1 2 3
1 2 3 4
```
```python
def number_pattern(n):
    # your code here
```

---

### enumerate() & zip()

**Q33.** Write a function that takes a list and returns a new list of strings like `"0: apple"`, `"1: banana"`, etc.
```python
def index_labels(lst):
    # your code here

print(index_labels(["apple", "banana", "cherry"]))
# ["0: apple", "1: banana", "2: cherry"]
```

**Q34.** Write a function that takes two lists (names and scores) and returns the name of the person with the highest score.
```python
def top_scorer(names, scores):
    # your code here

print(top_scorer(["Alice", "Bob", "Charlie"], [85, 92, 78]))  # "Bob"
```

**Q35.** Write a function that takes two lists and returns a list of tuples pairing each element.
```python
def pair_lists(lst1, lst2):
    # your code here

print(pair_lists([1, 2, 3], ["a", "b", "c"]))
# [(1, "a"), (2, "b"), (3, "c")]
```

**Q36.** Write a function that finds the index of the first element in a list that is greater than a given value.
```python
def first_greater(lst, value):
    # your code here

print(first_greater([1, 3, 5, 7], 4))   # 2  (index of 5)
print(first_greater([10, 20, 30], 25))  # 2  (index of 30)
```

---

### List Comprehensions

**Q37.** Rewrite this using a list comprehension:
```python
# Original
result = []
for n in range(1, 11):
    if n % 2 != 0:
        result.append(n * n)
# Expected: [1, 9, 25, 49, 81]
```

**Q38.** Write a list comprehension that extracts only the words longer than 4 characters from a list.
```python
words = ["hi", "hello", "cat", "elephant", "sun", "python"]
# Expected: ["hello", "elephant", "python"]
```

**Q39.** Write a list comprehension that converts all strings in a list to uppercase.
```python
fruits = ["apple", "banana", "cherry"]
# Expected: ["APPLE", "BANANA", "CHERRY"]
```

**Q40.** Write a list comprehension that returns `True`/`False` for each number — `True` if even, `False` if odd.
```python
nums = [1, 2, 3, 4, 5]
# Expected: [False, True, False, True, False]
```

---

### map(), filter(), lambda

**Q41.** Use `map()` and a lambda to convert a list of temperatures from Celsius to Fahrenheit. Formula: `(c * 9/5) + 32`
```python
celsius = [0, 20, 37, 100]
# Expected: [32.0, 68.0, 98.6, 212.0]
```

**Q42.** Use `filter()` and a lambda to return only strings that start with the letter "a".
```python
words = ["apple", "banana", "avocado", "cherry", "apricot"]
# Expected: ["apple", "avocado", "apricot"]
```

**Q43.** Use `map()` and a lambda to return the length of each word in a list.
```python
words = ["cat", "elephant", "hi", "python"]
# Expected: [3, 8, 2, 6]
```

**Q44.** Use `filter()` and a lambda to return only negative numbers from a list.
```python
nums = [3, -1, -4, 1, 5, -9, 2]
# Expected: [-1, -4, -9]
```

**Q45.** Use `sorted()` with a lambda to sort a list of tuples by the second element.
```python
pairs = [(1, 3), (3, 1), (2, 2)]
# Expected: [(3, 1), (2, 2), (1, 3)]
```

---

### Mixed — Harder Challenges

**Q46.** Write a function that takes a list of numbers and returns a dictionary grouping them as even or odd.
```python
def group_even_odd(lst):
    # your code here

print(group_even_odd([1, 2, 3, 4, 5, 6]))
# {"even": [2, 4, 6], "odd": [1, 3, 5]}
```

**Q47.** Write a function that takes a sentence and returns the longest word.
```python
def longest_word(sentence):
    # your code here

print(longest_word("I love programming in Python"))  # "programming"
```

**Q48.** Write a function that checks if all elements in a list are unique (no duplicates).
```python
def all_unique(lst):
    # your code here

print(all_unique([1, 2, 3, 4]))      # True
print(all_unique([1, 2, 2, 4]))      # False
```

**Q49.** Write a function that takes a list of names and returns only the names that appear more than once.
```python
def find_duplicates(lst):
    # your code here

print(find_duplicates(["Alice", "Bob", "Alice", "Charlie", "Bob"]))
# ["Alice", "Bob"]
```

**Q50.** Write a function that takes two lists and returns a list of elements that are in one list but not the other.
```python
def difference(lst1, lst2):
    # your code here

print(difference([1, 2, 3, 4], [3, 4, 5, 6]))  # [1, 2, 5, 6]
```

---

## 18. Answer Key Hints

Use these only after you attempt each question.

| Q | Hint |
|---|---|
| Q1 | Loop through the string, build a new string in reverse |
| Q2 | Clean the string with a loop + `isalnum()` + `lower()`, then compare to `[::-1]` |
| Q3 | Loop through characters, check if each is `in "aeiou"` |
| Q4 | Loop with a counter per character using a variable to track the max |
| Q5 | Sort both strings and compare, or count each character |
| Q6 | `split()` the sentence, use a loop + `[0].upper() + [1:]` on each word, then `join()` |
| Q7 | `replace(" ", "")` or list comprehension filtering spaces |
| Q8 | Loop and check each char with `isdigit()` |
| Q9 | `split()` the sentence, loop and count matches |
| Q10 | `split()` then reverse the list then `join()` |
| Q11 | Use `%` operator |
| Q12 | Convert `n` to string, loop through digits, sum them |
| Q13 | Convert to string, compare to `[::-1]` |
| Q14 | `range()` with step or loop with `%` |
| Q15 | Check `% 15` first, then `% 3`, then `% 5` |
| Q16 | Start with `result = 1`, multiply in a loop using `range(1, n+1)` |
| Q17 | Start with `max_val = lst[0]`, loop and compare |
| Q18 | Sort the list, return `[-2]` or loop tracking top two values |
| Q19 | Loop and append only if not already in result list |
| Q20 | Nested loop or list comprehension with inner `for` |
| Q21 | Loop through pairs using `range(len-1)`, check if each is `<=` next |
| Q22 | Slice: `lst[-k:] + lst[:-k]` |
| Q23 | Loop through one list, check `in` the other |
| Q24 | List comprehension with `% 2 == 0`, then `sum()` |
| Q25 | Loop and increment a counter when value matches |
| Q26 | List comprehension: `[x ** 2 for x in lst]` |
| Q27 | List comprehension: non-zeros first, then count and append zeros |
| Q28 | Loop with a running total, append to result each iteration |
| Q29 | `for i in range(1, 11)` with f-string |
| Q30 | Loop with `current` and `max_count` counters, reset on 0 |
| Q31 | `while n > 0: n //= 10, count += 1` |
| Q32 | Nested loop: outer for rows, inner `range(1, i+1)` |
| Q33 | `enumerate()` + f-string in list comprehension |
| Q34 | `zip(names, scores)`, loop and track max score |
| Q35 | `list(zip(lst1, lst2))` |
| Q36 | `enumerate()`, return index when condition is met |
| Q37 | `[n*n for n in range(1,11) if n % 2 != 0]` |
| Q38 | `[w for w in words if len(w) > 4]` |
| Q39 | `[w.upper() for w in fruits]` |
| Q40 | `[n % 2 == 0 for n in nums]` |
| Q41 | `list(map(lambda c: (c * 9/5) + 32, celsius))` |
| Q42 | `list(filter(lambda w: w.startswith("a"), words))` |
| Q43 | `list(map(lambda w: len(w), words))` |
| Q44 | `list(filter(lambda x: x < 0, nums))` |
| Q45 | `sorted(pairs, key=lambda x: x[1])` |
| Q46 | Start with `{"even": [], "odd": []}`, loop and append |
| Q47 | `split()` then loop tracking longest, or `max()` with `len` as key |
| Q48 | Loop and check `in` a seen list, or compare `len(lst)` to `len` of unique version |
| Q49 | Count occurrences, return those with count > 1 |
| Q50 | Two list comprehensions: elements in lst1 not in lst2, plus elements in lst2 not in lst1 |

---

## 15. LeetCode Concept Connections

| Concept | LeetCode Problem it helps solve |
|---|---|
| `[::-1]` reverse string | 125. Valid Palindrome, 344. Reverse String |
| `isalnum()` | 125. Valid Palindrome |
| `for` loop + counter | 485. Max Consecutive Ones |
| `enumerate()` | 1. Two Sum, 217. Contains Duplicate |
| `%` modulo | 412. FizzBuzz |
| `sum()` | 1480. Running Sum of 1d Array |
| list comprehension | 283. Move Zeroes |
| `in` keyword | 217. Contains Duplicate |
| `range()` | 66. Plus One |
| `split()` / string methods | 13. Roman to Integer |
