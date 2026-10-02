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
    return available_eggs - eggs_to_use

# parameter 1 value from the global variable of available_eggs
# parameter 2 is number of eggs you want to use
use_eggs(available_eggs, 1)

# check_kitchen_stock()

