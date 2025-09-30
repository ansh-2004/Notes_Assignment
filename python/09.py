# Looping statements

# Looping statements are used to repeat a task multiple times 

# simple for loop
fruits = ["apple","mango","banana"]

# for i in fruits:
#     print(i)                  

# output:- 
# apple
# mango
# banana



# ---
#nested for loop
color = ["blue","green","yellow"]
item = ["book","ball","chair"]

# for i in color:
#     for j in item:
#         # print("i is",i + " j is",j)
#         print(f"i is {i} and j is {j}") # embed variables inside strings. The f before the string tells Python to treat it as a formatted string literal.

# output:-
# i is blue j is book
# i is blue j is ball
# i is blue j is chair
# i is green j is book
# i is green j is ball
# i is green j is chair
# i is yellow j is book
# i is yellow j is ball
# i is yellow j is chair


# ---


# Range method 


#  In Python, `range` is a built-in function used to generate a sequence of numbers — often used in loops.

# ---

# ### 🔢 Basic Syntax

# ```python
# range(stop)
# range(start, stop)
# range(start, stop, step)
# ```

# - `start`: the number to begin from (default is 0)
# - `stop`: the number to stop **before**
# - `step`: how much to increment each time (default is 1)

# ---

# ### ✅ Examples

# #### 1. `range(5)`
# ```python
# for i in range(5):
#     print(i)
# ```
# **Output:**
# ```
# 0
# 1
# 2
# 3
# 4
# ```

# #### 2. `range(2, 6)`
# ```python
# for i in range(2, 6):
#     print(i)
# ```
# **Output:**
# ```
# 2
# 3
# 4
# 5
# ```

# #### 3. `range(1, 10, 2)`
# ```python
# for i in range(1, 10, 2):
#     print(i)
# ```
# **Output:**
# ```
# 1
# 3
# 5
# 7
# 9
# ```

# ---

# ### 🔁 Use Cases

# - Looping a fixed number of times
# - Generating sequences
# - Indexing through lists
# - Creating number patterns

# ---

# ### 🧠 Bonus Tip

# You can convert a range to a list:
# ```python
# list(range(5))  # Output: [0, 1, 2, 3, 4]
# ```


# You're absolutely right to question this — and the answer is: **you can print a `range` object directly**, but it won't show the actual numbers. Instead, it shows something like:

# ```python
# range(1, 5, 2)
# ```

# This is just a **representation** of the range object — not the values inside it.

# ---

# ### ✅ How to see the actual numbers

# To view the contents of a range, you need to **convert it to a list**:

# ```python
# print(list(range(1, 5, 2)))
# ```

# **Output:**
# ```
# [1, 3]
# ```

# ---

# ### 🔍 Why this happens

# - `range()` returns a **lazy iterable** — it doesn't generate all values upfront.
# - This is memory-efficient, especially for large ranges.
# - But to see the actual values, you need to iterate over it or convert it to a list.

# ---

# ### 🧪 Bonus: You can also loop through it

# ```python
# for i in range(1, 5, 2):
#     print(i)
# ```

# **Output:**
# ```
# 1
# 3
# ```

#---

# While loop 

i = 1
# while i<=10:
#     print(i)
#     i=i+1
  
# output:-
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# printin 2-table with while loop 

i = 1 
n = 2

# while i <= 10:
#     print(n," * ",i, "=", n * i)
#     i=i+1

# output:-
# 2  *   1 =   2
# 2  *   2 =   4
# 2  *   3 =   6
# 2  *   4 =   8
# 2  *   5 =  10
# 2  *   6 =  12
# 2  *   7 =  14
# 2  *   8 =  16
# 2  *   9 =  18
# 2  *  10 =  20



# ---

# while with list 
li = [1,2,3,4,5]
i = 0
while i < len(li):
    li[i] = li[i] + 100
    i = i + 1

print(li) # Output: [101, 102, 103, 104, 105]
 

# ---

# some advanced concepts 

# You've done a fantastic job covering the **core concepts** of flow control in Python — decision-making (`if`, `elif`, `else`) and looping (`for`, `while`). Now let’s take it a step further and explore some **advanced and useful extensions** to these topics that will make your Python skills even sharper:

# ---

# ## 🔁 Advanced Looping Techniques

# ### 1️⃣ `break`, `continue`, and `pass`

# - **`break`**: exits the loop entirely
# - **`continue`**: skips the current iteration and moves to the next
# - **`pass`**: does nothing (placeholder)

# ```python
# for i in range(5):
#     if i == 3:
#         break
#     print(i)  # Output: 0, 1, 2

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)  # Output: 0, 1, 2, 4

# for i in range(5):
#     if i == 3:
#         pass
#     print(i)  # Output: 0, 1, 2, 3, 4
# ```

# ---

# ### 2️⃣ `else` with loops

# Python allows an `else` block after a loop — it runs **only if the loop completes normally** (i.e., not interrupted by `break`).

# ```python
# for i in range(5):
#     if i == 10:
#         break
# else:
#     print("Loop completed without break")  # ✅ This will print
# ```

# ---

# ### 3️⃣ `enumerate()` for index tracking

# Instead of manually tracking index with `i`, use `enumerate()`:
# instead of this code to track index
# fruits = ["apple", "banana", "cherry"]
# for i in range(len(fruits)):
#     print(f"{i}: {fruits[i]}")

# we use this code 

# ```python
# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")
# ```

#enumerate(fruits) returns an iterator that produces pairs: (index, item)

# You can unpack these pairs directly in the for loop: for index, fruit in ...



# You can also specify a starting index:


# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}: {fruit}")

# output
# 1: apple
# 2: banana
# 3: cherry


# ---

# ### 4️⃣ `zip()` for parallel iteration

# Loop through multiple lists together:

# ```python
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 95]

# for name, score in zip(names, scores):
#     print(f"{name} scored {score}")
# ```

# ---

# ### 5️⃣ List Comprehensions (Loop + Expression)

# A compact way to create lists:

# ```python
# squares = [x**2 for x in range(5)]
# print(squares)  # Output: [0, 1, 4, 9, 16]
# ```

# You can even add conditions:

# ```python
# evens = [x for x in range(10) if x % 2 == 0]
# ```

# ---

# ## 🧠 Decision-Making Enhancements

# ### 6️⃣ Ternary Operator (One-line `if-else`)

# ```python
# a = 10
# b = 20
# max_val = a if a > b else b
# print(max_val)  # Output: 20
# ```

# ---

# ### 7️⃣ Logical Operators: `and`, `or`, `not`

# ```python
# x = 5
# if x > 0 and x < 10:
#     print("x is between 1 and 9")
# ```

# ---

# ### 8️⃣ Membership and Identity Operators

# - `in`, `not in` → check membership
# - `is`, `is not` → check identity (same memory location)

# ```python
# a = [1, 2, 3]
# b = a
# print(a is b)  # True
# print(2 in a)  # True
# ```
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)     # True → b is just another name for a
# print(a is c)     # False → a and c have same content but are different objects
# print(a == c)     # True → values are equal, but not identity

# ---

# ## 🧪 Bonus: Looping with `range()` in reverse

# ```python
# for i in range(10, 0, -1):
#     print(i)
# ```

# ---
