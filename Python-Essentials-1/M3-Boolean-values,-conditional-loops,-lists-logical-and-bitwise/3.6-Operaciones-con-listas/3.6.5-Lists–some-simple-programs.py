"""
3.6.5 Lists – some simple programs
Now we want to show you some simple programs utilizing lists.

The first of them tries to find the greater value in the list. Look at the code in the editor.

play_arrow
sync
download
light_mode
dark_mode
Console 
terminal
sync
The concept is rather simple ‒ we temporarily assume that the first element is the largest one, and check the hypothesis against all the remaining elements in the list.

The code outputs 17 (as expected).

The code may be rewritten to make use of the newly introduced form of the for loop:


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)
 
The program above performs one unnecessary comparison, when the first element is compared with itself, but this isn't a problem at all.

The code outputs 17, too (nothing unusual).

If you need to save computer power, you can use a slice:


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)
 
The question is: which of these two actions consumes more computer resources ‒ just one comparison, or slicing almost all of a list's elements?

Now let's find the location of a given element inside a list:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Element found at index", i)
else:
    print("absent")
 
Note:

the target value is stored in the to_find variable;
the current status of the search is stored in the found variable (True/False)
when found becomes True, the for loop is exited.
Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.

The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.

The question is: how many numbers have you hit?

This program will give you the answer:


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)
 
Note:

the drawn list stores all the drawn numbers;
the bets list stores your bets;
the hits variable counts your hits.
The program output is: 4.
"""