What Are Lambda Functions and How Do They Work?
Throughout the previous lessons, you have been used to defining functions by using the def keyword like this:

def square(num):
    return num ** 2

print(square(4)) # 16
But when it comes to working with high order functions like map() and filter(), you can use an anonymous inline function. This is where lambda functions come in.

Here's what the square() function looks like when refactored into a lambda function:

lambda num: num ** 2
As mentioned earlier, lambda functions are anonymous, so this function no longer has the name square associated with it. Lambda functions are great when you need to use them in higher order functions like this:

numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
In this example, we have a list of numbers and want to create a new list of even numbers. So we pass in a lambda function as one of the arguments to the filter() function to get a new list containing the numbers 2 and 4.

When working with lambda functions it is important to be aware of best practices. For example, it is not a good practice to assign a lambda function to a variable like this:

numbers = [1, 2, 3, 4, 5]

square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
This defeats the purpose of using anonymous functions. In this case, you should use a regular function, like this:

numbers = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers) # [1, 4, 9, 16, 25]
Also, you should avoid creating lambda functions that are difficult to read or unnecessarily complicated, like this:

result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)  # 14
While this function runs fine and produces the correct result of 14, it is not easy to read or look at. In this case, it would be better to create a separate function with an if/else statement, and then call that function:

def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # 14
Both regular functions and lambda functions have their use cases in Python programs. If you are dealing with a single inline expressions, then you might consider using a lambda function. Otherwise, using a regular function would be the way to go.

Questions

Which of the following is the best use case for a lambda function?


Defining a function with multiple lines and conditional logic.

Creating a reusable function across multiple modules.

Writing a small function for use inside a map() or filter() call.
Correct!


Creating a function with a descriptive name for clarity.

Why is it generally considered bad practice to assign a lambda function to a variable?


It results in syntax errors.

It defeats the purpose of using an anonymous function.
Correct!


Lambda functions are slower than regular functions.

Python does not allow this in most versions.

What is the primary disadvantage of using a complex lambda function like the one shown below?

result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)

It makes the code more readable.

It could lead to unexpected behavior due to ambiguity.

It is harder to understand and maintain.
Correct!


It requires too many resources to execute.