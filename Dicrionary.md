
# dictionary
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# pass list of tuppledictionary as an argument of dict()
# dict() turn tuples into dictionary form
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

###### dictionary[key]

# 'Margherita Pizza'
# if the key ['name'] doesn't exist in the dicrionary "pizza", it will create the new key-value pair 
pizza['name'] 

# changes the value of the key 'name'
# now the value of the key is Margherita
pizza['name'] = 'Margherita'

#### dictionary.get('key', default (it could be list))
#### this case key value is a list 
pizza.get('toppings', []) # ['mozzarella', 'basil']

### .keys() will return dict_keys(['name', 'price', 'calories_per_slice'])
pizza.keys()
# below is dict_keys view object
# dict_keys(['name', 'price', 'calories_per_slice']) 


pizza.values()
# below is dict_values view object
# dict_values(['Margherita Pizza', 8.9, 250])

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250
}

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])


pizza.items()
# below is a view object with all the key-value pairs
# this will return both values and key # dict_items([('name', 'Margherita Pizza'), ('price', 8.9), 

pizza.clear()
# below is to remove all the key value pair from the dictionary
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)]) 
# contents of the dictionary, not the dictionary object itself.



pizza.pop() # this method removes the key-value pair with the key that you specify as the first argument and returns its value
# it will pop the price as a key and 10 as a value from the dictionary
pizza.pop('price', 10)
# if the key is not exist, it will return the KeyError
pizza.pop('total_price') 


popitem() # this will removes the last inserted item

# Checks each key in the given dictionary.
# - If the key exists, its value is updated (replaced) with the new value.
# - If the key does not exist, the key and its value are added to the dictionary.
update() # pizza.update({ 'price': 15, 'total_time': 25 })


# keys() # dict_keys view object
# values() # view object with all the key-value pairs
# items() # both key and value 

# clear() # remove all the key value pairs
# pop() # remove all 

# update() 
pizza = {
    "name": "Margherita Pizza",
    "price": 8.9
}
keys = pizza.keys()
values = pizza.value()
items = pizza.items()
prints(keys) # this prints dict_keys(['name', 'price', 'calories_per_slice'])
prints(values) # this will print dict_values(['Margherita Pizza', 8.9, 250])
print(items) # dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])
print(type(values)) # this verify its type.

clear_key_value_pair = pizza.clear()
pop_key_value_pair = pizza.pop()
print(clear_key_value_pair)
print(pop_key_value_pair) # it will print the what key and values that it removed. 


pizza.update({ 'price': 15, 'total_time': 25 })
# dictionary will be like below
{
    'name': 'Margherita Pizza', 
    'price': 15, 
    'calories_per_slice': 250, 
    'toppings': ['mozzarella', 'basil'], 
    'total_time': 25
}


What Are Some Common Techniques to Loop Over a Dictionary?

print("Start small. Ship something.")

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}


for price in products.values(): 
    print(price)
# output
<!-- #990
600
250
70 -->


for product in products.keys(): # returns all the keys. In this case product
    print(product)
# you can also do below
# for product in products:
#     print(product)

# this will returns the key value pair
for product in products.items():
    print(product)
# output

<!-- 0 Laptop
1 Smartphone
2 Tablet
3 Headphones -->

# defining product loop variable
# defining price loops
# use the items() to return key value pair
# items() takes two parameter key and values 

for product, price in products.items():
    print(product, price)

# make 20% discount

products = products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8) # create the new list with product in the list

print(products) # this will print 

# {
# 'Laptop': 792, 
# 'Smartphone': 480, 
# 'Tablet': 200, 
# 'Headphones': 56
# }

# enumerate the the keys with enumerate()
# enumerate() assignes integier to each key-value pair 
# start with 0
for product in enumerate(products):
    print(product)

<!-- (0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones') -->

# this is you commmonly see in the forloop
for index, product in enumerate(products):
    print(index, product)

# this will return  the index that are paired with the values

<!-- (0, 990)
(1, 600)
(2, 250)
(3, 70) -->


# Iterates through the dictionary values.
# enumerate() assigns an integer counter (starting at 0 by default) to each
# value returned by products.values(), creating (index, value) tuples.
# enumerate(products.values()) returns an iterator of (index, value) tuples.
# During each iteration, each tuple is unpacked into the variables
# 'index' and 'price' before the print() statement is executed.
for index, price in enumerate(products.values()):
    print(index, price)
<!-- 
0 990
1 600
2 250
3 70 
-->





# Iterates through the dictionary's key-value pairs.
# products.items() returns (key, value) tuples.
# enumerate() wraps each (key, value) tuple in another tuple by adding an
# integer counter, resulting in (index, (key, value)) tuples.
# During each iteration, the outer tuple is unpacked into the variables
# 'index' and 'product', where 'product' contains the (key, value) tuple.
for index, product in enumerate(products.items()):
    print(index, product)
<!-- 
0 ('Laptop', 990)
1 ('Smartphone', 600)
2 ('Tablet', 250)
3 ('Headphones', 70) 
-->


# The second argument 1 inside the enumerate() specifies the starting value of the counter, so enumerate() starts counting from 1 instead of its default value of 0.
for index, product in enumerate(products.items(), 1):
    print(index, product)


## ######### Name Conflict  ############ ##

# suppose you write own function like below
def sin():
    print("Hello")
# then you import math libary
import math

# Python library function will overwrite your functions.
# Python think that you will use function from the standard library instead of your function
# this causes namespace collisions, and make it harder to know where certain names are coming from.

# Is it good practice to avoid the from name import *

###### Special Build-in variable in Python
# Below means "Only run this code when this file is executed directly."
if __name__ == "__main__": 

##### When do you use this? #####
# when you write the utility file:
# whe you quickly test your file by run it directly like below. 
# you have a math_tools.py below
# math_tools.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))

# Then main.py (or any file) imports it
import math_tools

result = math_tools.add(10, 20)

print(result)

# python will ignore the print(add(2, 3)) in the first code and execute the print(result) and then output 30 because you have this if __name__ == "__main__":

# get(): get method retrieves the value associated with a key. It's similar to the bracket notation, but it lets you set a default value, preventing errors if the key doesn't exist.








Dictionaries
| Method or term   | Easy description                                          | How it works                                              |
| ---------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| Dictionary       | Stores information as key and value pairs                 | Example: `{'name': 'Pizza', 'price': 8.9}`                |
| Key              | The name used to find a value                             | `'price'` is a key                                        |
| Value            | The information connected to a key                        | `8.9` is the value                                        |
| `dict()`         | Creates a dictionary                                      | Can convert key and value tuples into a dictionary        |
| Bracket notation | Gets a value using its key                                | `pizza['price']` returns `8.9`                            |
| `get()`          | Gets a value safely                                       | `pizza.get('price', 0)` returns `0` if the key is missing |
| `keys()`         | Shows all dictionary keys                                 | `pizza.keys()` returns a view of the keys                 |
| `values()`       | Shows all dictionary values                               | `pizza.values()` returns a view of the values             |
| `items()`        | returns view object with keys and values together         | Each pair is returned as a tuple                          |
| View object      | A live view of dictionary information                     | It changes when the original dictionary changes           |
| `clear()`        | Removes everything                                        | The dictionary becomes empty                              |
| `pop()`          | Removes a key and returns its value                       | A default value can prevent a `KeyError`                  |
| `popitem()`      | Removes the most recently added pair                      | It returns the removed key and value                      |
| `update()`       | Adds or updates information                               | Existing values are replaced and new keys are added       |
| `KeyError`       | An error caused by a missing key                          | Happens when you request a key that does not exist        |

Looping through dictionaries
| Method or term                         | Easy description                      | How it works                                |
| -------------------------------------- | ------------------------------------- | ------------------------------------------- |
| `for key in dictionary`                | Loops through keys                    | Each key is placed in the loop variable     |
| `for value in dictionary.values()`     | Loops through values                  | Each value is placed in the loop variable   |
| `for key, value in dictionary.items()` | Loops through keys and values         | The tuple is unpacked into two variables    |
| Tuple unpacking                        | Separates tuple values into variables | `product, price` receives the key and value |
| `enumerate()`                          | Adds a counter to a loop              | Returns an index and the current item       |
| `enumerate(data, 1)`                   | Starts counting from 1                | Without `1`, counting starts from 0         |

Sets
| Method or term | Easy description                  | How it works                                 |
| -------------- | --------------------------------- | -------------------------------------------- |
| Set            | Stores unique values              | Duplicate values are automatically removed   |
| Unordered      | Items have no guaranteed position | You cannot access a set with an index        |
| Mutable        | The set can be changed            | You can add or remove items                  |
| Immutable item | An item that cannot be changed    | Sets can contain strings, numbers and tuples |
| `{1, 2, 3}`    | Creates a set with values         | Curly brackets contain the set items         |
| `set()`        | Creates an empty set              | `{}` creates an empty dictionary, not a set  |
| `add()`        | Adds one value                    | Duplicate values are not added again         |
| `remove()`     | Removes a value                   | Raises `KeyError` if the value is missing    |
| `discard()`    | Safely removes a value            | Does nothing if the value is missing         |
| `clear()`      | Removes every value               | The set becomes empty                        |
| `in`           | Checks whether a value exists     | `5 in my_set` returns `True` or `False`      |

Set comparisons and operations
| Method or operator       | Easy description                              | How it works                        |
| ------------------------ | --------------------------------------------- | ----------------------------------- |
| `issubset()`             | Checks if all values exist in another set     | Useful for checking required skills |
| `issuperset()`           | Checks if a set contains another complete set | Useful for checking permissions     |
| `isdisjoint()`           | Checks if two sets share no values            | Returns `True` when nothing matches |
| `\|` Union               | Combines both sets                            | Includes every unique value         |
| `&` Intersection         | Finds shared values                           | Useful for finding matched skills   |
| `-` Difference           | Finds values missing from the second set      | Useful for finding missing skills   |
| `^` Symmetric difference | Finds values that are not shared              | Excludes values found in both sets  |

Python libraries and imports
| Method or term          | Easy description                       | How it works                                         |
| ----------------------- | -------------------------------------- | ---------------------------------------------------- |
| Python standard library | Reusable code included with Python     | Includes modules such as `math`, `re` and `datetime` |
| Module                  | A Python file containing reusable code | It can contain functions, classes and variables      |
| `import math`           | Imports an entire module               | Use `math.sqrt(36)` to call its function             |
| Dot notation            | Accesses something inside a module     | `math.sqrt` means the `sqrt` function from `math`    |
| `import math as m`      | Imports a module using a shorter name  | Use `m.sqrt(36)`                                     |
| Alias                   | A different name for an imported item  | Created with the `as` keyword                        |
| `from math import sqrt` | Imports one specific function          | You can call `sqrt(36)` directly                     |
| `from math import *`    | Imports everything directly            | Discouraged because names can conflict               |
| Namespace collision     | Two items have the same name           | Python may use or replace the wrong name             |

Running a Python file
| Method or term               | Easy description                     | How it works                                          |
| ---------------------------- | ------------------------------------ | ----------------------------------------------------- |
| `__name__`                   | A special variable created by Python | Its value depends on how the file is used             |
| `"__main__"`                 | Means the file was run directly      | Python assigns this value to `__name__`               |
| Imported module              | A file loaded by another Python file | Its `__name__` becomes the module’s name              |
| `if __name__ == "__main__":` | Controls when main code runs         | The code runs only when the file is executed directly |
