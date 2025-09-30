# Set in python 

# Set is an unordered and unindexed collection of elements enclosed within {}, Duplicates are not allowed in Set 
# unordered means whatever sequence you insert an element is a set that particular order is not maintained
# unindexed means we cannot access elements of a set using index

s1 = {1,"a",True,2,"b",False}
print(type(s1)) # Output :- <class 'set'>
print(s1) # Output :- {False, 1, 2, 'a', 'b'} (order may vary)
# Here, True is not shown because 1 was already added — and Python treats them as the same key because 1 and True are considered equal.So when you add both 1 and True to a set, only one of them is kept


# Set Operations 

# Adding an element in a set 
s1 = {1,"a",True,2,"b",False}
s1.add("new element")
print(s1) # Output :- {False, 1, 2, 'a', 'new element', 'b'} (order may vary)

# add() method is used to add an element in a set

#---
# Removing an element from a set
s1.remove("b")
print(s1) # Output :- {False, 1, 2, 'a', 'new element'} (order may vary)

# remove() method is used to remove an element from a set
# If the element is not present in the set then it will raise KeyError
# s1.remove("not present") # KeyError: 'not present'
# s1.discard("not present") # No Error
# discard() method is used to remove an element from a set
# If the element is not present in the set then it will not raise any error


# print(s1) # Output :- {False, 1, 2, 'a', 'new element'} (order may vary)
# s1.discard(True) 
# print(s1) # Output :- {1, 2, 'a', 'new element'} (order may vary)

# note:- to remove an integer or boolean element , we need to write without quotes because with quotes it understand it as string so it will not remove . in both remove or discard method 
# so type sensitive applies in all list , set , dictionary


#---

# Popping an element from a set
s1 = {1,"a",True,2,"b",False}
popped_element = s1.pop()
print("popped element is ",popped_element) # Output :- popped element is  False (element may vary)
print(s1) # Output :- {1, 2, 'a', 'b'} (order may vary)
# pop() method is used to pop an element from a set
# It removes and returns an arbitrary element from the set  
# If the set is empty then it will raise KeyError
# s1.clear()
# print(s1) # Output :- set()
# popped_element = s1.pop() # KeyError: 'pop from an empty set'
# print("popped element is ",popped_element) # Output :- popped element is  (element may vary)
# print(s1) # Output :- set()


# ---
# Updating multiple elements in a set
s1 = {1,"a",True,2,"b",False}
s1.update([10,20,30])
s1.update({"key":"value"}) # only key will be added not value 
print(s1) # Output :- {False, 1, 2, 10, 20, 30, 'a', 'b'} (order may vary)
# update() method is used to update multiple elements in a set
# It can take a list , tuple , set or string as an argument
# If we pass a string as an argument then it will add each character of the string as an element in the set
s1.update("hello")
print(s1) # Output :- {False, 1, 2, 10, 20, 30, 'a', 'b', 'e', 'h', 'l', 'o'} (order may vary)

# Here, 'l' is shown only once because duplicates are not allowed in set

# The .update() method in a set adds elements from an iterable (like a list, tuple, or dictionary) to the set.

#---




# Set Functions 

# Union of two sets 
s1 = {1,2,3}
s2 = {"a","b","c"}
s3 = s1.union(s2) 
print(s3) # output :- {1, 2, 3, 'c', 'a', 'b'}
print(s1) # Output :- {1, 2, 3}
# union() method is used to find the union of two sets
# It returns a new set which is the union of two sets

# s1 remains unchanged
# We can also use | operator to find the union of two sets
s4 = s1 | s2
print(s4) # output :- {1, 2, 3, 'c', 'a', 'b'}
# Here | operator is used to find the union of two sets
# s1 and s2 remains unchanged
#---

# Intersection of two sets
s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}
s3 = s1.intersection(s2)
print(s3) # Output :- {5}
print(s1) # Output :- {1, 2, 3, 4, 5}
# intersection() method is used to find the intersection of two sets
# It returns a new set which is the intersection of two sets

# s1 remains unchanged
# We can also use & operator to find the intersection of two sets
s4 = s1 & s2
print(s4) # Output :- {5}
# Here & operator is used to find the intersection of two sets
# s1 and s2 remains unchanged
#---

