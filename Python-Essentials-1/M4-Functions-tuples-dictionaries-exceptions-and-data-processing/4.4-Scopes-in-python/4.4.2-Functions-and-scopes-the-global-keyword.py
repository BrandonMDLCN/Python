"""
4.4.2 Functions and scopes: the global keyword
Hopefully, you should now have arrived at the following question: does this mean that a function is not able to modify a variable defined outside it? This would create a lot of discomfort.

Fortunately, the answer is no.

There's a special Python method which can extend a variable's scope in a way which includes the function's body (even if you want not only to read the values, but also to modify them).

Such an effect is caused by a keyword named global:


global name
global name1, name2, ...
 
Using this keyword inside a function with the name (or names separated with commas) of a variable (or variables), forces Python to refrain from creating a new variable inside the function ‒ the one accessible from outside will be used instead.

In other words, this name becomes global (it has global scope, and it doesn't matter whether it's the subject of read or assign).

Look at the code in the editor.


def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


We've added global to the function.

The code now outputs:

Output
Do I know that variable? 2
2
This should be sufficient evidence to show that the global keyword does what it promises.
"""