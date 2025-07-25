"""
4.2.4 Mixing positional and keyword arguments
You can mix both styles if you want ‒ there is only one unbreakable rule: you have to put positional arguments before keyword arguments.

If you think for a moment, you'll certainly guess why.

To show you how it works, we'll use the following simple three-parameter function:


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
 
Its purpose is to evaluate and present the sum of all its arguments.

The function, when invoked in the following way:


adding(1, 2, 3)
 
will output:

Output
1 + 2 + 3 = 6
It was ‒ as you may suspect ‒ a pure example of positional argument passing.

Of course, you can replace such an invocation with a purely keyword variant, like this:


adding(c = 1, a = 2, b = 3)
 
Our program will output a line like this:

Output
2 + 3 + 1 = 6
Note the order of the values.

Let's try to mix both styles now.

Look at the function invocation below:


adding(3, c = 1, b = 2)
 
Let's analyze it:

the argument (3) for the a parameter is passed using the positional way;
the arguments for c and b are specified as keyword ones.
This is what you'll see in the console:

Output
3 + 2 + 1 = 6
Be careful, and beware of mistakes. If you try to pass more than one value to one argument, all you'll get is a runtime error.

Look at the invocation below - it seems that we've tried to set a twice:


adding(3, a = 1, b = 2)
 
Python's response:

Output
TypeError: adding() got multiple values for argument 'a'
Look at the snipet below. A code like this is fully correct, but it doesn't make much sense:


adding(4, 3, c = 2)
 
Everything is right, but leaving in just one keyword argument looks a bit weird ‒ what do you think?
"""