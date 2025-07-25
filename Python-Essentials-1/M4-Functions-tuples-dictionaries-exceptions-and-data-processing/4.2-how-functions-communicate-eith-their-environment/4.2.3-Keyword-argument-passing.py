"""
4.2.3 Keyword argument passing
Python offers another convention for passing arguments, where the meaning of the argument is dictated by its name, not by its position ‒ it's called keyword argument passing.

Take a look at the snippet:


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
 
The concept is clear ‒ the values passed to the parameters are preceded by the target parameters' names, followed by the = sign.

The position doesn't matter here ‒ each argument's value knows its destination on the basis of the name used.

You should be able to predict the output. Run the code to check if you're right.

Of course, you mustn't use a non-existent parameter name.

The following snippet will cause a runtime error:


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(surname="Skywalker", first_name="Luke")
 
This is what Python will tell you:

Output
TypeError: introduction() got an unexpected keyword argument 'surname'
Try it out yourself.
"""