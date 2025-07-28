# 1.1.7 The as keyword

"""
If you use the import module variant and you don't like a particular module's name (e.g., it's the same as one of your already defined entities, so qualification becomes troublesome) 
you can give it any name you like - this is called aliasing.

Aliasing causes the module to be identified under a different name than the original. This may shorten the qualified names, too.

Creating an alias is done together with importing the module, and demands the following form of the import instruction:


import module as alias
 
The "module" identifies the original module's name while the "alias" is the name you wish to use instead of the original.

Note: as is a keyword.
"""

# 1.1.8 Aliasing

"""
If you need to change the word math, you can introduce your own name, just like in the example:


import math as m
    
print(m.sin(m.pi/2))
 
Note: after successful execution of an aliased import, the original module name becomes inaccessible and must not be used.

In turn, when you use the from module import name variant and you need to change the entity's name, you make an alias for the entity. This will cause the name to be replaced by the alias you choose.

This is how it can be done:


from module import name as alias
 
As previously, the original (unaliased) name becomes inaccessible.

The phrase name as alias can be repeated - use commas to separate the multiplied phrases, like this:


from module import n as a, m as b, o as c
  
The example may look a bit weird, but it works:


from math import pi as PI, sin as sine
  
print(sine(PI/2))
  
Now you're familiar with the basics of using modules. Let us show you some modules and some of their useful entities.
"""