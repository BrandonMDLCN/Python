# 1.2.1 Working with standard modules

# Before we start going through some standard Python modules, we want to introduce the dir() function to you. 
# It has nothing to do with the dir command you know from Windows and Unix consoles, as dir() doesn't show the contents of a disk directory/folder, 
# but there is no denying that it does something really similar - it is able to reveal all the names provided through a particular module.

# There is one condition: the module has to have been previously imported as a whole (i.e., using the import module instruction - from module is not enough).

# The function returns an alphabetically sorted list containing all entities' names available in the module identified by a name passed to the function as an argument:


# dir(module)
  
# Note: if the module's name has been aliased, you must use the alias, not the original name.

# Using the function inside a regular script doesn't make much sense, but it is still possible.

# For example, you can run the following code to print the names of all entities within the math module:


import math
  
for name in dir(math):
  print(name, end="\t")
  
# The example code should produce the following output:

""" 
__doc__ __loader__ __name__ __package__ __spec__ acos acosh asin asinh atan atan2
atan2 atanh ceil copysign cos cosh degrees e erf erfc exp expm1 fabs factorial floor
fmod frexp fsum gamma hypot isfinite isinf isnan ldexp lgamma log log10 log1p
log2 modf pi pow radians sin sinh sqrt tan tanh trunc
 """

# Have you noticed these strange names beginning with __ at the top of the list? 
# We'll tell you more about them when we talk about the issues related to writing your own modules.

# Some of the names might bring back memories from math lessons, and you probably won't have any problems guessing their meanings.

# Using the dir() function inside a code may not seem very useful - usually you want to know a particular module's contents before you write and run the code.

# Fortunately, you can execute the function directly in the Python console (IDLE), without needing to write and run a separate script.

# This is how it can be done:


# import math
# dir(math)