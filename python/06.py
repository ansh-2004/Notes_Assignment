# Dictionary in Python 

# Dictionary is an unordered collection of key-value pairs enclosed with {}
# Dictionary is mutable i.e we can change the elements of a dictionary once it is created
# Keys in a dictionary are unique and immutable whereas values can be of any data type and can be duplicate

fruit = {"Mango" : 10 , "Apple" : 20, "Litchi" : 30, "Strawberry" : 40}
print(type(fruit)) # Output :- <class 'dict'>
print(fruit) # Output :- {'Mango': 10, 'Apple': 20, 'Litchi': 30, 'Strawberry': 40}

fruit = {1 : 10 , 2 : 20, 3 : 30, 4 : 40}
print(fruit)  # Output :- {1: 10, 2: 20, 3: 30, 4: 40}

#---

# Extracting Keys and values 

fruit = {"Apple" : 10 , "Orange" : 20, "Banana" : 30, "Guava" : 40}
print(fruit.keys()) # Output :- dict_keys(['Apple', 'Orange', 'Banana', 'Guava']) 
# keys() method returns a list of keys in the dictionary
print(fruit.values()) # Output :- dict_values([10, 20, 30, 40])
# values() method returns a list of values in the dictionary
print(fruit.items()) # Output :- dict_items([('Apple', 10), ('Orange', 20), ('Banana', 30), ('Guava', 40)])
# items() method returns a list of tuples where each tuple is a key-value pair

#---
# Accessing values using keys
print(fruit["Apple"]) # Output :- 10
print(fruit.get("Banana")) # Output :- 30
# get() method is used to access values using keys
# If the key is not present in the dictionary then it will return None
print(fruit.get("Pineapple")) # Output :- None
# print(fruit["Pineapple"]) # KeyError: 'Pineapple'
# If we try to access a key which is not present in the dictionary using [] then it will raise KeyError
#---

# Modifying a Dictionary 

# Adding a new element 
print(fruit) # Output :- {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}
fruit["Pineapple"] = 50
print(fruit) # Output :- {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40, 'Pineapple': 50}

# changing an existing element 
print(fruit) # Output :- {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40, 'Pineapple': 50}
fruit["Apple"] = 100
print(fruit) # Output :- {'Apple': 100, 'Orange': 20, 'Banana': 30, 'Guava': 40, 'Pineapple': 50}

#---
# Dictionary Functions 

# Update one dictionary's elements with another  or concatenate two dictionaries
fruit1 = {"Apple" : 10 , "Orange": 20}
fruit2 = {"Banana" : 30 , "Guava" : 40}

print("Before updating fruit1",fruit1) # Output :- Before updating fruit1 {'Apple': 10, 'Orange': 20}
fruit1.update(fruit2)
print("After updating fruit1",fruit1) # Output :- After updating fruit1 {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}
# update() method is used to update one dictionary's elements with another dictionary

#---
# Popping an element 
fruit = {"Apple" : 10,"Orange":20, "Banana" : 30, "Guava" : 40}
print("Before popping",fruit) # Output :- Before popping {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}
fruit.pop("Banana")
print("After popping",fruit) # Output :- After popping {'Apple': 10, 'Orange': 20, 'Guava': 40}

# pop() method is used to pop an element from the dictionary using its key

# If the key is not present in the dictionary then it will raise KeyError
# fruit.pop("Pineapple") # KeyError: 'Pineapple'
# To avoid KeyError we can use pop() method with default value
# print(fruit.pop("Pineapple", "Not Found")) # Here "Not Found" is the default value
# print("After popping with default value",fruit) # Output :- After popping with default value {'Apple': 10, 'Orange': 20, 'Guava': 40}
# Here if the key is not present in the dictionary then it will return the default value instead of raising KeyError
# If the key is present in the dictionary then it will pop the element and return its value
# print(fruit.pop("Apple", "Not Found")) # Output :- 10
# print(fruit) # Output :- {'Orange': 20, 'Guava': 40}
# Here it will pop the element with key "Apple" and return its value 10
#---


# Clearing a dictionary
fruit = {"Apple" : 10,"Orange":20, "Banana" : 30, "Guava" : 40}
print("Before clearing",fruit) # Output :- Before clearing {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}
fruit.clear()
print("After clearing",fruit) # Output :- After clearing {}
# clear() method is used to clear all the elements of a dictionary
#---

# Length of a dictionary
fruit = {"Apple" : 10,"Orange":20, "Banana" : 30, "Guava" : 40}
print(len(fruit)) # Output :- 4
# len() method is used to find the length of a dictionary i.e the number of key-value pairs in the dictionary


#---
# Deleting a dictionary
fruit = {"Apple" : 10,"Orange":20, "Banana" : 30, "Guava" : 40}
print(fruit) # Output :- {'Apple': 10, 'Orange': 20, 'Banana': 30, 'Guava': 40}
del fruit
# print(fruit) # NameError: name 'fruit' is not defined
# del keyword is used to delete a dictionary    



#---'
# Membership operator in dictionary
fruit = {"Apple" : 10,"Orange":20, "Banana" : 30, "Guava" : 40}
print("Apple" in fruit) # Output :- True        
print("Pineapple" in fruit) # Output :- False
# in operator is used to check if a key is present in the dictionary or not

print("Pineapple" not in fruit) # Output :- True
print("Apple" not in fruit) # Output :- False
# not in operator is used to check if a key is not present in the dictionary or not

# Here in and not in operators check for keys only not for values
print(10 in fruit) # Output :- False
print(10 not in fruit) # Output :- True
#---


# note :- in dictionary keys are immutable, unique and can be string , numbers or tuples (if the tuple itself contains only immutable elements). You cannot use lists or other dictionaries as keys 
my_dict = {1: "one", "name": "Alice", (2, 3): "tuple"}
print(my_dict) # Output :- {1: 'one', 'name': 'Alice', (2, 3): 'tuple'}

# my_dict = {[1, 2]: "list"}  # ❌ This will raise a TypeError unhashable type: 'list'
 
