# 1.1.4 Namespace

"""
1.1.4 Namespace
To continue, you need to become familiar with an important term: namespace. Don't worry, we won't go into great detail - this explanation is going to be as short as possible.

A namespace is a space (understood in a non-physical context) in which some names exist and the names don't conflict with each other (i.e., there are not two different objects of the same name). We can say that each social group is a namespace - the group tends to name each of its members in a unique way (e.g., parents won't give their children the same first names).


This uniqueness may be achieved in many ways, e.g., by using nicknames along with the first names (it will work inside a small group like a class in a school) or by assigning special identifiers to all members of the group (the US Social Security Number is a good example of such practice).

Inside a certain namespace, each name must remain unique. This may mean that some names may disappear when any other entity of an already known name enters the namespace. We'll show you how it works and how to control it, but first, let's return to imports.

If the module of a specified name exists and is accessible (a module is in fact a Python source file), Python imports its contents, i.e., all the names defined in the module become known, but they don't enter your code's namespace.

This means that you can have your own entities named sin or pi and they won't be affected by the import in any way.


At this point, you may be wondering how to access the pi coming from the math module.

To do this, you have to qualify the pi with the name of its original module.
"""

# 1.1.5 Importing a module: continued

"""
This first example won't be very advanced - we just want to print the value of sin(½π).

Look at the code in the editor. This is how we test it.
"""

import math
print(math.sin(math.pi/2))

"""
The code outputs the expected value: 1.0.

Look at the snippet below, this is the way in which you qualify the names of pi and sin with the name of its originating module:


math.pi
math.sin
It's simple, you put:

the name of the module (e.g., math)
a dot (i.e., .)
the name of the entity (e.g., pi)
Such a form clearly indicates the namespace in which the name exists.

Note: using this qualification is compulsory if a module has been imported by the import module instruction. 
It doesn't matter if any of the names from your code and from the module's namespace are in conflict or not.

Note: removing any of the two qualifications will make the code erroneous. There is no other way to enter math's namespace if you did the following:


import math
Now we're going to show you how the two namespaces (yours and the module's one) can coexist.

Take a look at the example in the editor window.

We've defined our own pi and sin here.
"""

import math


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

"""
Run the program. The code should produce the following output:

Output
0.99999999
1.0
As you can see, the entities don't affect each other.

In the second method, the import's syntax precisely points out which module's entity (or entities) are acceptable in the code:


from math import pi
The instruction consists of the following elements:

the from keyword;
the name of the module to be (selectively) imported;
the import keyword;
the name or list of names of the entity/entities which are being imported into the namespace.
The instruction has this effect:

the listed entities (and only those ones) are imported from the indicated module;
the names of the imported entities are accessible without qualification.
Note: no other entities are imported. Moreover, you cannot import additional entities using a qualification - a line like this one:


print(math.e)
will cause an error (e is Euler's number: 2.71828...)

Let's rewrite the previous script to incorporate the new technique.

Here it is:
"""

from math import sin, pi

print(sin(pi/2))

"""
The output should be the same as previously, as in fact we've used the same entities as before: 1.0. Copy the code, paste it in the editor, and run the program.

Does the code look simpler? Maybe, but the look is not the only effect of this kind of import. Let's show you that.

Look at the code in the editor. Analyze it carefully:

line 1: carry out the selective import;
line 3: make use of the imported entities and get the expected result (1.0)
lines 5 through 12: redefine the meaning of pi and sin - in effect, they supersede the original (imported) definitions within the code's namespace;
line 15: get 0.99999999, which confirms our conclusions.
"""

from math import sin, pi

print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

"""
Let's do another test. Look at the code below:
"""

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))

"""
Here, we've reversed the sequence of the code's operations:

lines 1 through 8: define our own pi and sin;
line 11: make use of them (0.99999999 appears on the screen)
line 13: carry out the import - the imported symbols supersede their previous definitions within the namespace;
line 15: get 1.0 as a result.
"""

# 1.1.6 Importing a module: *

"""
In the third method, the import's syntax is a more aggressive form of the previously presented one:


from module import *
 
As you can see, the name of an entity (or the list of entities' names) is replaced with a single asterisk (*).

Such an instruction imports all entities from the indicated module.

Is it convenient? Yes, it is, as it relieves you of the duty of enumerating all the names you need.

Is it unsafe? Yes, it is - unless you know all the names provided by the module, you may not be able to avoid name conflicts. Treat this as a temporary solution, and try not to use it in regular code.
"""