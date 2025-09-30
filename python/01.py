# Variables in Python :- Data/Values can be stored in temporty storage spaces called variables
# This variable will have a particular address associated with it and since this variable is a temporty storage space , the values which are stored inside it can be changed again and again

var1 = "John"
print(var1)   # Output :- John

# This var1 is called variable and it is storing the value "John" inside it

# We can change the value of var1 again and again as it is temporary storage space
var1 = "sam"
print(var1)   # Output :- sam

var1 = "Matt"
print(var1)   # Output :- Matt

# Every variable is associated with a data type 

# 10500 - int 
# 3.14,15.97 - float 
# True,False - Boolean 
# "Sam", 'John' - String

num1 = 10 
print(type(num1)) # Output :- <class 'int'>

decimate = 3.14
print(type(decimate)) # Output :- <class 'float'>

log1 = True 
print(type(log1)) # Output :- <class 'bool'>

char1 = "Arjun"
print(type(char1)) # Output :- <class 'str'>

char2 = 'A'
print(type(char2)) # Output :- <class 'str'>

# Another data type is **Complex type** . It is a data type where you have a real part and an imaginary part
3 + 5j # Here 3 is the real part and 5j is the imaginary part
print(type(3 + 5j)) # Output :- <class 'complex'>b

# ------------

# Operators in python :- Operators help us to perform simple operations on this data. 
# We have Arithmetic opeartors , Relational Operators , Logical Operators 

# Arithmetic Operators :- + , - , * , /  
num1 = 10 
num2 = 20 

print(num1+ num2) # Output :- 30


print(num1 - num2) # Output :- -10

print(num1 * num2) # Output :- 200

print(num1 / num2) # Output :- 0.5

print(num1 ** num2) # Output :- 100000000000000000000

print(num2 // num1) # Output :- 2

print(num1 % num2) # Output :- 0


# Relational Operators :- > , < , >= , <= , == , !=

# We can also print numbers like 
print(num1,num2) # Output :- 10 20
# num2 = 10
print(num1 > num2) # Output :- False
print(num1 < num2) # Output :- True
print(num1 >= num2) # Output :- False
print(num1 <= num2) # Output :- True
print(num1 == num2) # Output :- False
print(num1 != num2) # Output :- True


# Logical Operators :- and(&) , or(|) , not(!)

log1 = True 
log2 = False 

print(log1 and log2) # Output :- False
print(log1 or log2) # Output :- True
print(not log1) # Output :- False

print(log1 & log2) # Output :- False
print(log1 | log2) # Output :- True

