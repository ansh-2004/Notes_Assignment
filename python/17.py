# Exception Handling 

# Try and Except 

# The code written inside the try block executes if the code is error free. 
# If the code is not error free then the except block gets executed and results an exception. 
# A try statement can have more than one except statement. 

# try:
    # Statement 
# except :
    # Exception 


# a = input("Enter a number 1 : ")
# b = input("Enter the number 2 : ")

# try:
#     c = int(a) + b 
#     print(c)
# except Exception as e:
#     print(e)


# output:
# unsupported operand type(s) for +: 'int' and 'str'        , it does not come as error , simple print statement is executed
# because int can't be added to string . 


# we can simple write it as 

# a = input("Enter a number 1 : ")
# b = input("Enter the number 2 : ")

# try:
#     c = int(a) + b 
#     print(c)
# except :
#     print("error in your try block")

# output :
# error in your try block


# ----

# Try with else clause 

# - Else clause is used with the try clause when you want to execute the set of instructions in the absence of exceptions in your code. 
# syntax 
# try:
#     print(" ")
# except :
#     print(" ")
# else :
#     print(" ")


# a = int(input("Enter the number 1 :"))

# try:
#     if a % 2 == 0:
#         print(f"{a} is an even number")
#         # print(f"{b} is an even number")
#     else :
#         print(f"{a} is an odd number")
# except Exception as e:
#     print(e)
# else:
#     print("Else clause got executed ")

# output :
# Enter the number 1 :4
# 4 is an even number
# Else clause got executed 

# In this output we see else block got executed because there was no error in the try block 

# if we make  an error in try block like print b instead of a 
#output:
# Enter the number 1 : 8
# name 'b' is not defined

# now here we see we get exception b not defined and our else block did not get executed because there was an error in try block 


# --------

# Finally Keyword 

# Finally is a keyword which surely executes after the execution of the try and except block of statement. 

# try:
#     print(" ")
# except :
#     print(" ")
# else : # Exceptional
#     print(" ")
# finally :
#     print(" ")


# a = int(input("Enter the num 1 : "))
# b = int(input("Enter the num 2 : "))

# try:
#     if a > b:
#         print(f"{a} is greater than {b}")
#     else :
#         print(f"{b} is greater than {a}")
# except Exception as e:
#     print(e)
# finally:
#     print("Finally keyword used ")


# output :
# Enter the num 1 : 10
# Enter the num 2 : 52
# 52 is greater than 10
# Finally keyword used 

# no error in try block but finally block executed 


# a = int(input("Enter the num 1 : "))
# b = int(input("Enter the num 2 : "))

# try:
#     if c > b:
#         print(f"{a} is greater than {b}")
#     else :
#         print(f"{b} is greater than {a}")
# except Exception as e:
#     print(e)
# finally:
#     print("Finally keyword used ")

# output:
# Enter the num 1 : 2
# Enter the num 2 : 5
# name 'c' is not defined
# Finally keyword used

# error in our try block but still finally block executed 


a = int(input("Enter the num 1 : "))
b = int(input("Enter the num 2 : "))

# try:
#     if c > b:
#         print(f"{a} is greater than {b}")
#     else :
#         print(f"{b} is greater than {a}")
# finally:
#     print("Finally keyword used ")

# output :
# Enter the num 1 : 4
# Enter the num 2 : 6
# Finally keyword used 
# Traceback (most recent call last):
#   File "C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\python\17.py", line 152, in <module>
#     if c > b:
#        ^
# NameError: name 'c' is not defined

# in this we use try with finally but no except block , in this case finally block gets executed but we get error in our try block and program terminates abruptly



# -------------

# . Raising Exceptions Manually
# Use raise to trigger exceptions intentionally:

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    

# ---------------------

# Exception Chaining
# Use raise ... from ... to preserve original exceptions:

try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Conversion failed") from e


# Sometimes, you catch one exception but want to raise a new one that gives more context. Instead of hiding the original error, you can chain it using raise ... from ....

# 🧠 Why Use It
# To preserve the original error for debugging

# To wrap low-level errors in high-level context

# To make error logs more informative

# 🧪 Example Explained

try:
    int("abc")  # This raises ValueError
except ValueError as e:
    raise RuntimeError("Conversion failed") from e

# int("abc") fails because "abc" is not a number.

# We catch the ValueError and raise a new RuntimeError.

# The from e part links the new error to the original one.

# 🔍 Output Traceback
# The traceback will show:

# RuntimeError: Conversion failed
# → caused by ValueError: invalid literal for int() with base 10: 'abc'
# This is super helpful when debugging complex systems where one error leads to another.

# ------------------
# Using except with Multiple Exceptions
# You can group exceptions using a tuple:

# try:
#     # risky code
# except (TypeError, ValueError) as e:
#     print(f"Handled error: {e}")


# -------------------------------

# 1. Catching Specific Exceptions
# Instead of using a generic except, catch specific exceptions to handle different error types more precisely:


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")