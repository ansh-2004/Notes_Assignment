# List in Python 

# List is a collection of items which are ordered and changeable/mutable. Lists are written in square brackets []

# List can contain items of different data types


# difference between tuple and list is that tuple is immutable whereas list is mutable
# tuples are written in round brackets () but lists are written in square brackets []

l1 = [1,'a',True]
print(type(l1)) # Output :- <class 'list'>
print(l1) # Output :- [1, 'a', True]


# Extracting individual elements from a list
li=[1,"a",2,"b",3,"c"]
print(li[0]) # Output :- 1
print(li[2:5]) # Output :- [2, 'b', 3] where 5 not included
print(li[-1]) # Output :- c


# Modifying a list 

#changing the element at index 0
print(li) # Output :- [100, 'a', 2, 'b', 3, 'c']         
li[0] = 100
print(li) # Output :- [100, 'a', 2, 'b', 3, 'c']         


# ---

# Popping the last element from a list
print(li) # Output :- [100, 'a', 2, 'b', 3, 'c']
li.pop()
print(li) # Output :- [100, 'a', 2, 'b', 3]


# Popping the element at index 1
li.pop(1)
print(li) # Output :- [100, 2, 'b', 3]

# ---
# Appending a new element at last of the list
print(li) # Output :- [100, 2, 'b', 3]
li.append("new element")
print(li) # Output :- [100, 2, 'b', 3, 'new element']

# ---
# Inserting a new element at index 1
print(li) # Output :- [100, 2, 'b', 3, 'new element']
li.insert(1,"inserted element")
print(li) # Output :- [100, 'inserted element', 2, 'b', 3, 'new element']


# ---

# Removing an element from the list
print(li) # Output :- [100, 'inserted element', 2, 'b', 3, 'new element']
li.remove(2)
print(li) # Output :- [100, 'inserted element', 'b', 3, 'new element']

#---

# Reversing elements of a list 
print("original list",li) # Output :- [100, 'inserted element', 'b', 3, 'new element']
li.reverse()
print("reversed list ",li) # Output :- ['new element', 3, 'b', 'inserted element', 100]

# ---
# Sorting List 
li = ["mango","banana","guava","apple"]
print("original list",li) # Output :- ['mango', 'banana', 'guava', 'apple']
li.sort()
print("sorted list ",li) # Output :- ['apple', 'banana', 'guava', 'mango']

# sort() is a built-in function in python which sorts the elements of a list in ascending order

# Sorting list in descending order
li.sort(reverse=True)
print("sorted list in descending order ",li) # Output :- ['mango', 'guava', 'banana', 'apple']


# ---
# Concatenating Lists
list1 = [1,2,3]
list2 = ['a','b','c']
print(list1 + list2)  # Output :- [1, 2, 3, 'a', 'b', 'c']

# Here + operator is used to concatenate two lists

# ---
# Repeating elements 
list3 = [1,'a',True]
print(list3 * 3) # Output :- [1, 'a', True, 1, 'a', True, 1, 'a', True]

# Here * operator is used to repeat the elements of a list

# ---
# Length of a list
print(len(list3)) # Output :- 3
