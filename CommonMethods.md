count() - This method is used to determine how many times an item appears in a tuple

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2

if the string is not in the tupple it will returns 0

index()

sorted() 
- this will always create a new list of the sorted values.
- can be used on any iterable including tuples

Key - If you need to customize the sorting behavior for an iterable, you can use the optional reverse and key arguments. 

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']