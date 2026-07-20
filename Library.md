# how to import library
<!-- 
import module_name
module_name.function_name()
-->

# this import all the functions in the math library
import math 
math.sqrt(36) # square root of 36 
# outout 6.0


# What if you want the specific functions or classes but not everything in the library

from module_name import name1, name2

# If you want to assign aliases to these names

from module_name import name1 as alias1, name2 as alias2

# example if you only need the radians, sine and cosine functions

from math import radians, sin, cos

# you can find the libary below
# https://docs.python.org/3/library/index.html


# example how to use math libary to find cos, sin, and redians from spefic degree

from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978
