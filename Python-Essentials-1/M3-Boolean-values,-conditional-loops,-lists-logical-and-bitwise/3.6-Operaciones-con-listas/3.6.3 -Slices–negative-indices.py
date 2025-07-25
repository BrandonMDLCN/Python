"""
3.6.3 Slices – negative indices
Look at the snippet below:

my_list[start:end]
 
To repeat:

start is the index of the first element included in the slice;
end is the index of the first element not included in the slice.
This is how negative indices work with the slice:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
 
The snippet's output is:

Output
[8, 6, 4]
If the start specifies an element lying further than the one described by the end (from the list's beginning), the slice will be empty:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
 
The snippet's output is:

Output
[]
If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.

In other words, the slice of this form:

my_list[:end]
 
is a more compact equivalent of:

my_list[0:end]
 
Look at the snippet below:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
 
This is why its output is: [10, 8, 6].

Similarly, if you omit the end in your slice, it is assumed that you want the slice to end at the element with the index len(my_list).

In other words, the slice of this form:

my_list[start:]
 
is a more compact equivalent of:

my_list[start:len(my_list)]
 
Look at the following snippet:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
 
Its output is therefore: [4, 2].

As we've said before, omitting both start and end makes a copy of the whole list:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
 
The snippet's output is: [10, 8, 6, 4, 2].

More about the del instruction
The previously described del instruction is able to delete more than just a list's elements at once ‒ it can delete slices too:


my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
 
Note: in this case, the slice doesn't produce any new list!

The snippet's output is: [10, 4, 2].

Deleting all the elements at once is possible too:


my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
 
The list becomes empty, and the output is: [].

Removing the slice from the code changes its meaning dramatically.

Take a look:


my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
 
The del instruction will delete the list itself, not its content.

The print() function invocation from the last line of the code will then cause a runtime error.
"""