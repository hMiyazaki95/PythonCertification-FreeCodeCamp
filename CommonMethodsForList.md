append()
pop()
sort()

append() - This is used to add an item to the end of the list. 

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

extend() - you can add multiple elements from one list to another. 

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

insert() - This method accepts two arguments: the index where you wish to insert the new item and the item you want to insert.

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

remove() 
- The remove() method takes the value of the element to remove as an argument
- This method will only remove the first occurrence of an item. Not all of them:


numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]

pop() - Used to remove an element at a specific index in the list.

sort() -  This method is used to sort the elements in place. Here is an example of sorting a random list of numbers in place:

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67] # assending order

reverse() - This method, will reverse a list of elements in place like this:

numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]
numbers[::-1]

What is the difference between List and Strings?
- Lists are mutable and Strings are immutable
  
index() -  This is used to find the first index where an element can be found in a list
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1

If the element cannot be found, then Python throws a ValueError:

programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('JavaScript')

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'JavaScript' is not in list
"""


Questions

Which of the following examples will correctly insert the number 2.5 at index 2 in the numbers list?


numbers = [1, 2, 3, 4, 5]
numbers.insertInto(2.5, 2)

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
Correct!


numbers = [1, 2, 3, 4, 5]
numbers.insertInto(2, 2.5)

numbers = [1, 2, 3, 4, 5]
numbers.insert(2.5, 2)

Which of the following methods will reverse a list of elements in place?


reverse()
Correct!


reversing()

reversedList()

reversingList()

Which of the following is NOT a list method?


pop()

clear()

splice()
Correct!


append()
