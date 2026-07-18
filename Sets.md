# Sets can only contains immutable data types (can access through the indices but can't be modified) like numbers, strings, and tuples
# Sets supports Mathematical set operations, including union, intersection, difference and symmetric difference


| Data Type      | Mutable? |   Has Indices?   | Can Iterate? |
| -------------- | :------: | :--------------: | :----------: |
| `list`         |   ✅ Yes  |       ✅ Yes      |     ✅ Yes    |
| `tuple`        |   ❌ No   |       ✅ Yes      |     ✅ Yes    |
| `str` (string) |   ❌ No   |       ✅ Yes      |     ✅ Yes    |
| `dict`         |   ✅ Yes  | ❌ No (uses keys) |     ✅ Yes    |
| `set`          |   ✅ Yes  |       ❌ No       |     ✅ Yes    |
| `int`          |   ❌ No   |       ❌ No       |     ❌ No     | 
| `float`        |   ❌ No   |       ❌ No       |     ❌ No     |
| `bool`         |   ❌ No   |       ❌ No       |     ❌ No     |
# Integer is single value and it doesn't have anything inside it to index.
# list, tuple, and str always has indices but tuple and str are immutable

# how to create the set
# sets use curly braces {}
my_set = {1, 2, 3, 4, 5, (10, 20), "string", 3.14, False} 

# define empty set


set() # empty set
{} # curly braces automatically creates the dictionary for you in python

# TO ADD an element
# .add() will add an element to set depending on the argument
# add() adds a hashable (typically immutable) object to an unordered set. The element is not appended to the "end" of the set because sets have no defined order.
my_set = {1, 2, 3, 4, 5} 
my_set.add((10, 20)) # add the tuple in the set
my_set.add("string") 
print(my_set) 
# output 
# the string is added before the tuple because Sets are usually unordered 
# {1, 2, 3, 4, 5, 'string', (10, 20)}

# To REMOVE an element
my_set.remove(4) # will raise a KeyError if the element is not found,
my_set.discard(4) # will not

# TO CLEAR the sets
# .clear() will remove all the existing elements from the set
my_set.clear()

# common mathematical set operations Methods
# if the my_set if subset of your_set, my set has to contain all the element that your_set has same in the other way around.
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

# case 1
my_set = {1, 2, 3}
your_set = {1, 2, 3, 4, 5}

print(my_set.issubset(your_set)) # true

# case 2
my_set = {1, 2, 6}
your_set = {1, 2, 3, 4, 5}

print(my_set.issubset(your_set)) # false

my_set | your_set # {1, 2, 3, 4, 5, 6}
my_set & your_set # {2, 3, 4}
my_set - your_set # {1, 5}
my_set ^ your_set # {1, 5, 6}

# corresponding compound assignment operator
|= &= -= ^=

# finds the difference between the sets and updates the first set with that result:
my_set -= your_set
# my_set will be updated to {1, 5}
print(my_set)
# check if an element is in a set or not with the in operator
print(5 in my_set)


Questions

Which of the following is a core characteristic of Python sets?


Elements are ordered and accessed by index.

Elements are stored as key-value pairs.

Elements are unique and unordered.
Correct!


Elements can be of any data type, including lists and dictionaries.

What operator is used to check if an element is present in a set?


==

in
Correct!


get()

find()

Which set operation returns a new set with the elements that are present in either one of the two sets, but not in both of them?


Union

Intersection

Difference

Symmetric Difference
Correct!

