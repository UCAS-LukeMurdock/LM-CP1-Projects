#Luke Murdock, Debugging

# The function is supposed to print the second element of the list, but it causes an IndexError. Find the bug.

#my_list = [1, 2]

#print(my_list[1])

def add_to_list(item, my_list=[]):

     my_list.append(item)

     return my_list

print(add_to_list("apple", ["banana, orange, grape"]))