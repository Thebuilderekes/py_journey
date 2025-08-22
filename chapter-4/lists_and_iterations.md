## Rules of Lists
- You cannot assign a value to an item in a list that does not exist compared to some other programming languages that allow this kind of behavior

- you can use + to add 2 list together
``
names = ['ana', 'john']
movies = ['matrix', 'hostel']
add_list = names + movies //prints ['ana', 'john', 'matrix', 'hostel']
``
- list.append(item) to add item to a list 
- list.extend(another_list) to add list to another list 
- list.insert(index, another_list) to add list to another list at index 
- list.sort() to sort a list of numbers or letter sin ascending order. It can also take arguments like reverse, etc.  An alternative would be to use sorted(list) especially when you want sort the list and store it as the value of another variable without changing the original list
- list.count(item) to count he number of occurrences of the item
- list.pop() to remove the last item in a list
-list.remove(0)

## Iterations
for loop is a preferred way of looping over a list compared to a while loop. A while loop requires a condition to be met in order to run the loop while a for loop doesn't.

- range() is very useful when dealing with iterations.
- if you type((range(5))) you get an object of type range #prints <class 'range'>
- Strings are also iterable just like range



