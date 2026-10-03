available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

# if you give a parameter the exact same name as a global 
# variable (like available_eggs), the function will use its 
# own local parameter available_eggs instead of the global one.
def use_eggs(available_eggs, eggs_to_use):
    #pass
    # make sure eggs that will be used does not exceed the available eggs
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs

    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use # this one doesn't update the value

# parameter 1 value from the global variable of available_eggs
# parameter 2 is number of eggs you want to use
use_eggs(available_eggs, 1)
print(available_eggs)

# check_kitchen_stock()

# this function checks whether an egg is available and updates its local egg count
def make_fried_egg(available_eggs):
    has_enough_eggs = available_eggs >= 1

    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print('Made a fried egg. Yummy!')
    else:
        print('Could not make a fried egg. Not enough eggs!')
    
    return available_eggs
# call the make_fried_egg function, passing available_eggs as the argument, and assign the result back to the global available_eggs variable.
available_eggs = make_fried_egg(available_eggs)
# this will show updated value for the eggs (0)
check_kitchen_stock()


### Final Output ###

# python3 kitchen_inventory_tracker.py  
# 1 egg(s) used out of 1 available.
# 1
# 1 egg(s) used out of 1 available.
# Made a fried egg. Yummy!
# The kitchen has 5 total items:
# - 0 eggs
# - 2 flour
# - 3 sugar