# Python Strings :- Strings are a sequence of characters enclosed within single quotes or double quotes or triple quotes 
# 'hello world' , "hello world" , '''hello world''' , """hello world"""

# triple quotes are used for multi line strings
str1 = '''
I am 
going to 
France tomorrow
'''

print(str1)
# Output :-
# I am
# going to
# France tomorrow
print(type(str1)) # Output :- <class 'str'>

# in jupyter notebook we get output like 
# '\nI am \ngoing to \nFrance tomorrow\n'


# We can also use escape sequences in strings
str2 = 'I am \'going\' to France tomorrow' # Here we have used \' to escape the single quote
print(str2) # Output :- I am 'going' to France tomorrow

char1 = 'A' # Here A is a character
print(type(char1)) # Output :- <class 'str'>
# In python there is no char data type , a single character is also treated as a string of length 1

# We can also use double quotes inside single quotes and vice versa
str3 = "I am 'going' to France tomorrow"
print(str3) # Output :- I am 'going' to France tomorrow

str4 = 'I am "going" to France tomorrow'
print(str4) # Output :- I am "going" to France tomorrow


# --- 

# Extracting individual characters from a string 

my_string = "My name is John"
print(my_string[0]) # Output :- M

print(my_string[-1]) # Output :- n



# Finding length of string 
print(len(my_string)) # Output :- 15

# len() is a built-in function in python which returns the length of a string

# Converting string to lower case 
print(my_string.lower()) # Output :- my name is john
# lower() is a built-in function in python which converts a string to lower case

# Converting string to upper case
print(my_string.upper()) # Output :- MY NAME IS JOHN
# upper() is a built-in function in python which converts a string to upper case

# Replacing a substring in a string
print(my_string.replace('y','a')) # Output :- Ma name is John
print(my_string.replace('John','Sam')) # Output :- My name is Sam
print(my_string) # Output :- My name is John
# replace() is a built-in function in python which replaces a substring in a string


# Number of occurrences of a substring in a string
new_string = "hello hello world"
print(new_string.count('hello')) # Output :- 1

# count() is a built-in function in python which returns the number of occurrences of a substring in a string


# Finding index of a substring in a string

s1 = 'This is sparta!!!!'
print(s1.find('sparta')) # Output :- 8 

# find() is a built-in function in python which returns the index of a substring in a string

# If the substring is not found , it returns -1
print(s1.find('hello')) # Output :- -1
# If the substring is found multiple times , it returns the index of the first occurrence
s2 = 'hello hello world'
print(s2.find('hello')) # Output :- 0


# ---

# Splitting a string into a list of substrings
fruit = 'I like apples, mangoes , bananas'
print(fruit.split(',')) # Output :- ['I like apples', ' mangoes ', ' bananas']