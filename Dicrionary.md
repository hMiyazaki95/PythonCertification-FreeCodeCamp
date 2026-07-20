
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

