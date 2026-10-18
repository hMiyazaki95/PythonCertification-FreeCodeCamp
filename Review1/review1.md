Which description of Python is most accurate?
A markup language used mainly for web page structure

A low-level, compiled, statically typed language

A high-level, interpreted, dynamically typed language

Correct
A language that can only be used for data science

Spot on. Python is high-level, runs through an interpreter, and works out variable types at runtime. It's used for web development, automation, data science, AI, scripting and more.


Which variable name follows Python's recommended naming convention (PEP 8)?
user_age

Correct
userAge

USER-AGE

UserAge

Nicely done. Python variables and functions use snake_case: lowercase words separated by underscores. PascalCase is for class names, and hyphens aren't allowed at all.


Which of these is NOT a valid variable name?
_count

2nd_place

Correct
total_score

place2

Have another look. The correct answer is 2nd_place.Variable names can't start with a digit. They can start with a letter or underscore and contain letters, digits and underscores.


What does this print? print("a", "b", "c", sep="-")
a-b-c-

abc-

a-b-c

Correct
a b c

You got it. The sep argument replaces the default space placed between arguments. It doesn't add anything at the end; that's what end controls.


What is the result of type(3.0)?
<class 'str'>

<class 'float'>

Correct
<class 'int'>

<class 'number'>

Right. Any number written with a decimal point is a float, even if the decimal part is zero.


What does isinstance(True, int) return?
False

True

Correct
TypeError

None

That's a tricky one. The correct answer is True.bool is a subclass of int in Python (True behaves like 1, False like 0), so isinstance returns True. This is a key difference from type(True) == int, which is False.

isinstance(True, int) # argument 1 is instance of the data type in argument 2


What happens here? word = "hello" word[0] = "J"
Nothing happens

A TypeError is raised

Correct
word becomes "Jhello"

word becomes "Jello"

Remember immutability. The correct answer is A TypeError is raised.Strings are immutable: you can't change their characters in place. To get "Jello" you build a new string, e.g. "J" + word[1:].

Given name = "Ada" and age = 36, which line prints Ada is 36?
print("name is age")

print(f"{name} is {age}")

Correct
print("{name} is {age}")

print(name + " is " + age)

Perfect. An f-string interpolates the values in braces. Option c raises a TypeError because you can't concatenate a str with an int, and d lacks the f prefix so it prints the braces literally.

What is "Python"[1:4]?
"Pyt"

"ytho"

"Pyth"

"yth"

Correct
Watch the stop index. The correct answer is "yth".Slicing includes the start index and excludes the stop index: indices 1, 2 and 3 are y, t, h.

What is "Python"[::-1]?
"nohtyP"

Correct
An error

"n"

"P"

Not quite. The correct answer is "nohtyP".A step of -1 walks the string backwards, which is the classic way to reverse a string.

What does "red,green,blue".split(",") return?
"red green blue"

['red,green,blue']

('red', 'green', 'blue')

['red', 'green', 'blue']

Correct
Correct. split() breaks a string at the separator and returns a list of strings. Its partner join() does the reverse: ",".join(list).

What does print(7 // 2, 7 % 2) output?
4 1

3.5 1

3 1

Correct
3 0.5

Great. // is floor division (rounds down to a whole number) and % gives the remainder. 7 divided by 2 is 3 remainder 1.

What does 0.1 + 0.2 == 0.3 evaluate to?
TypeError

False

Correct
True

Incorrect
0.3

Floats are sneaky. The correct answer is False.Floats are stored in binary and can't represent 0.1 or 0.2 exactly, so the sum is 0.30000000000000004. Use round() or math.isclose() to compare floats.