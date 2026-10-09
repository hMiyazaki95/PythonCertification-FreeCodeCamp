# Step 1: Set up your code

# Create a file called main.py with the following content:

# def divide(a, b):
#     result = a / b
#     return result

# print(divide(10, 2))
# print(divide(15, 3))

# Step 2: Set a breakpoint
# Click in the gutter (left margin) next to line 2 (result = a / b) to set a breakpoint
# A red dot will appear, indicating the breakpoint is set

# Step 3: Start debugging
# Press F5 or go to Run > Start Debugging
# Select "Python File" when prompted
# The debugger will pause execution at your breakpoint

# Step 4: Inspect variables
# Hover over variables to see their current values
# Use the Variables panel on the left to see all local variables
# Use the Debug Console at the bottom to evaluate expressions

# Step 5: Step through code
# Use the debug toolbar to:
# Continue (F5): Resume execution until the next breakpoint
# Step Over (F10): Execute the current line and move to the next
# Step Into (F11): Enter into function calls
# Step Out (Shift + F11): Exit the current function


# import pdb

def divide(a, b):
    # pdb.set_trace()
    result = a / b # set the break point with red dot
    return result

print(divide(10, 2))
print(divide(15, 3))

# Error_Handling/main.py(38)divide()
# -> result = a / b # set the break point with red dot
# (Pdb) help

# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt      
# alias  clear      disable  ignore    longlist  r        source   until    
# args   commands   display  interact  n         restart  step     up       
# b      condition  down     j         next      return   tbreak   w        
# break  cont       enable   jump      p         retval   u        whatis   
# bt     continue   exit     l         pp        run      unalias  where    

# Miscellaneous help topics:
# ==========================
# exec  pdb

# (Pdb) type
# <class 'type'>
# (Pdb) debug
# ENTERING RECURSIVE DEBUGGER
# > <string>(0)<module>()
# ((Pdb)) 
