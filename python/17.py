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
try:
    print(" ")
except :
    print(" ")
else :
    print(" ")
