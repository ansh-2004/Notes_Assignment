# Data-Structures in Python :- Tuple , List, Dictionary , Set 


# Tuple 

# Tuple is an ordered collection of elements enclosed within (). Tuples are immutable i.e we cannot change the elements of a tuple once it is created. Tuples can contain elements of different data types
# Tuple is faster than list because of its immutability


tup1 = (1,"sparta",True)
print(type(tup1)) # Output :- <class 'tuple'>
print(tup1) # Output :- (1, 'sparta', True)

# Extracting individual elements from a tuple
tup1 = (1,"a",True,2,"b",False)
print(tup1[2]) # Output :- True

print(tup1[-1]  ) # Output :- False

print(tup1[1:4]) # Output :- ('a', True, 2) where 4 not included

# You cannot modify a tuple becuase it is immutable
# tup1[0] = "hello" # TypeError: 'tuple' object does not support item assignment

#---
# Finding Length of a tuple 
print(len(tup1)) # Output :- 6

#---
# Concatenating Tuples
tup1 = (1,2,3)
tup2 = (4,5,6)
print(tup1 + tup2) # Output :- (1, 2, 3, 4, 5, 6)

#---
# Repeating Tuple Elements 
tup1 = ("sparta",300)
print(tup1 * 3) # Output :- ('sparta', 300, 'sparta', 300, 'sparta', 300)
print(tup1 * 0) # Output :- ()

#---
# Repeating and concatenating 
tup2 = (4,5,6)
print(tup1 * 3 + tup2) # Output :- ('sparta', 300, 'sparta', 300, 'sparta', 300, 4, 5, 6)


#---
# Tuple Packing and Unpacking
# Tuple Packing
tup1 = 1, "sparta", True # Parenthesis are optional
print(tup1) # Output :- (1, 'sparta', True)
print(type(tup1)) # Output :- <class 'tuple'>
# Here we have packed the values 1, "sparta", True into a tuple
# Tuple Unpacking
a, b, c = tup1
print(a) # Output :- 1
print(b) # Output :- sparta
print(c) # Output :- True
# Here we have unpacked the tuple tup1 into individual variables a, b, c
# Number of variables should be equal to number of elements in the tuple otherwise we will get ValueError
# a, b = tup1 # ValueError: too many values to unpack (expected 2)
# a, b, c, d = tup1 # ValueError: not enough values to unpack (expected 4, got 3)
# We can use * to unpack the remaining elements of the tuple into a list
a, *b = tup1
print(a) # Output :- 1
print(b) # Output :- ['sparta', True]
# Here we have unpacked the first element of the tuple tup1 into variable a and the remaining elements into list b
# Similarly we can unpack the last element of the tuple into a variable and the remaining elements into a list
*a, b = tup1
print(a) # Output :- [1, 'sparta']
print(b) # Output :- True
# Here we have unpacked the last element of the tuple tup1 into variable b and the remaining elements into list a
# We can also unpack the elements of a tuple into individual variables and a list
a, *b, c = tup1
print(a) # Output :- 1
print(b) # Output :- ['sparta']
print(c) # Output :- True
# Here we have unpacked the first element of the tuple tup1 into variable a, the last element into variable c and the remaining elements into list b


#---

# Tuple Functions 

# Minimum Value 
tup1 = (1,2,3,4,5,5,5)
print(min(tup1)) # Output :- 1

# Maximum Value
print(max(tup1)) # Output :- 5

# Sum of all elements
print(sum(tup1)) # Output :- 25

# Length of tuple
print(len(tup1)) # Output :- 7
# Here min() , max() , sum() , len() are built-in functions in python which can be used with tuples

print(tup1.count(5)) # Output :- 3
# Here count() is a built-in function in python which returns the number of occurrences of an element in a tuple


