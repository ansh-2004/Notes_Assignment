# Data Structures and Algorithms 
# Arrays 
# Stack 
# Queue 
# Linked List 
# Linear Search 
# Binary Search 
# Insertion sort
# Quick Sort 
# Merge Sort 

# --------------------

# Array 

# - Linear Data Structure 
# - Contiguous memory locations 
# - Access elements randlomly 
# - Homogeneous elements i.e, similar elements 

# Applications 
# - Storing information - linear fashion 
# - Suitable for applications that require frequent searching . 

# 1-Dimensional Array 
# - 1D can be related to a row. 
# - Elements are stored one after another. 
# - Only one subscript or index is used. 


# 2-Dimensional Array 
# - 2D can be related to a table or matrix. 
# - Elements are stored one after another i.e one 1D array inside other. 
# - Two subscripts or indices are used, one row and one column. 
# - Dimensions depends upon the number of subscripts used. 


# Array Implementation 
# A program implementing the following points :-
# - Create a one-dimensional integer array and insert numbers to the maximum size provided until the end of the array. Access the numbers inserted and then display the same as output. 
# - Create a two-dimensional integer array and insert numbers to the maximum size provided unitl the end of the array. Access the numbers inserted and then display the same as output. 
# - Implement search , sort and delete operations on array of integers. 

# print("How many element to store inside the array",end="")
# num=input()
# arr = []

# print("\nEnter",num,"Elements",end="")
# num = int(num)

# for i in range(num):
#     element = input()
#     arr.append(element)
# print("\nThe array elements are")
# for i in range(num):
#     print(arr[i],end="")  # 1 2 3 45

# print(arr)  # ['1 2 3 ', '4', '5']
# print(type(arr))  # <class 'list'>



# ---

# r_num = int(input("Input number of rows"))  # 4
# c_num = int(input("Input number of columns")) # 3
# twod_arr = [[] for row in range(r_num)] 
# print(twod_arr)  # [[], [], [], []]
# twod_arr = [[0 for col in range(c_num)] for row in range(r_num)]
# print(twod_arr) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for row in range(r_num):
#     for col in range(c_num):
#         twod_arr[row][col] = row * col

# print(twod_arr)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6]]

# print(type(twod_arr)) # <class 'list'>



#--- deleting operation 

# print(end="Enter the size of Arrays:")
# tot = int(input())
# arr = []
# print(end="Enter " + str(tot) + " Elements:")

# for i in range(tot):
#     arr.append(input())


# print(end="\nEnter the value to delete:")
# val = input()

# if val in arr:
#     arr.remove(val)
#     print("\nThe new array is :")
#     for i in range(tot - 1):
#         print(end=arr[i] + " ")
# else:
#     print("\n Element doesn't exist in the list")


# ```
# output:
# Enter the size of Arrays:10
# Enter 10 Elements:10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# Enter the value to delete:5

# The new array is :
# 10 9 8 7 6 4 3 2 1

# ```



# --- Sorting opeartion 
# arr = [10,22,38,27,11];
# temp = 0;

# # Displaying elements of original array 
# print("Elements of original array:");
# for i in range(0,len(arr)):
#     print(arr[i],end=" ");

# #Sort the array in ascending order 
# for i in range(0,len(arr)):
#     for j in range(i + 1,len(arr)):
#         if(arr[i]> arr[j]):
#             temp = arr[i];
#             arr[i] = arr[j];
#             arr[j] = temp;

# print();
# #Displaying elements of the array after sorting 
# print("Elements of array sorted in ascending order:");
# for i in range(0,len(arr)):
#     print(arr[i],end=" ");



# - Searching operation 

# import array 
# arr = array.array('i',[1,2,3,1,2,5])
# print(type(arr)) # output: <class 'array.array'>
# print(arr) # output: array('i', [1, 2, 3, 1, 2, 5])
# print("The new created array is :",end="")
# for i in range(0,6):
#     print(arr[i],end=" ")  # output: The new created array is :1 2 3 1 2 5 
# print("\r")
# print("The index of 1st occurrence of 2 is :",end="")
# print(arr.index(2)) # output: 1
# print("The index of 1st occurrence of 1 is :",end="")
# print(arr.index(1)) # output: 0


#---

# Array Module 

# The `array` module provides an `array()` object that stores elements of the **same data type** in a compact form. It's more efficient than Python lists for numerical data.

### Importing the Module
# ```python
# import array
# ```

 
## Creating an Array

# arr = array.array('i', [1, 2, 3, 4])


# - `'i'` is the **type code** for signed integers.
# - Other type codes:
#   | Type Code | C Type             | Python Type       |
#   |-----------|--------------------|-------------------|
#   | `'b'`     | signed char        | int               |
#   | `'B'`     | unsigned char      | int               |
#   | `'u'`     | Unicode character  | str (deprecated)  |
#   | `'h'`     | signed short       | int               |
#   | `'H'`     | unsigned short     | int               |
#   | `'i'`     | signed int         | int               |
#   | `'I'`     | unsigned int       | int               |
#   | `'f'`     | float              | float             |
#   | `'d'`     | double             | float             |

## Common Methods

### 1. `append(x)`
# Adds an element to the end.

# arr.append(5)


### 2. `insert(i, x)`
# Inserts `x` at index `i`.

# arr.insert(2, 10)


### 3. `pop([i])`
# Removes and returns the item at index `i`. If `i` is omitted, removes the last item.

# arr.pop(1)


### 4. `remove(x)`
# Removes the first occurrence of `x`.

# arr.remove(3)


### 5. `index(x)`
# Returns the index of the first occurrence of `x`.

# arr.index(2)


### 6. `reverse()`
# Reverses the array in place.

# arr.reverse()


### 7. `buffer_info()`
# Returns a tuple with memory address and number of elements.

# arr.buffer_info()


### 8. `typecode`
# Returns the type code of the array.

# arr.typecode



## Iterating Over an Array


# for item in arr:
#     print(item)


## Converting Between Array and List


# list_version = arr.tolist()
# new_arr = array.array('i', list_version)


 
## Array vs List

# | Feature         | `array` Module         | `list`               |
# |-----------------|------------------------|----------------------|
# | Type restriction| Same type only         | Mixed types allowed  |
# | Memory usage    | More efficient         | Less efficient       |
# | Speed           | Faster for numerics    | Slower               |
# | Flexibility     | Less flexible          | More flexible        |


# If you're working with **large numeric datasets**, the `array` module is a great lightweight alternative to NumPy. 

# ----

# Advantages 
# - Random access elements 
# - Easy sorting and iteration 
# - Replacement fo multiple variables 

# Disadvantages 
# - Size is fixed 
# - Difficult to insert and delete 
# - If capacity is more and occupancy less, most of the array gets wasted. 
# - Needs contiguous memory 

