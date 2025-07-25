"""
3.6.2 Powerful slices
Fortunately, the solution is at your fingertips ‒ it's called a slice.

A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.

It actually copies the list's contents, not the list's name.

This is exactly what you need. Take a look at the snippet below:
"""
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

"""
Its output is [1].

This inconspicuous part of the code described as [:] is able to produce a brand new list.

One of the most general forms of the slice looks as follows:

my_list[start:end]
As you can see, it resembles indexing, but the colon inside makes a big difference.

A slice of this form makes a new (target) list, taking elements from the source list ‒ the elements of the indices from start to end - 1.

Note: not to end but to end - 1. An element with an index equal to end is the first element which does not take part in the slicing.

Using negative values for both start and end is possible (just like in indexing).

Take a look at the snippet:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
 
The new_list list will have end - start (3 - 1 = 2) elements ‒ the ones with indices equal to 1 and 2 (but not 3).

The snippet's output is: [8, 6]

Run the code in the editor to see how Python copies the entire list, and some fragment of a list. Feel free to experiment!
"""
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
