# Python Tokens :- Smallest meaningful component in a program 
# Combining all python tokens we get a python code 
# Python tokens are :- Keywords , Identifiers , Literals , Operators , Punctuators


# Keywords :- Keywords are reserved words in python which have special meaning to the compiler
# Some keywords are :- False,True, None , if , else , elif , for , while , break , continue , return , import , from , as , pass , def , class , try , except , finally , with , lambda , nonlocal , global , assert , yield , raise , del , in , is , not , or , and


# def = 10  # SyntaxError: invalid syntax 


# ---

# Identifiers :- Identifiers are the name given to variables , functions , classes , modules , objects etc.
# Rules for writing identifiers :-
# 1. No special Character expect _ (underscore) is allowed
# 2. Identifiers are case sensitive 
# 3. First letter cannot be digit 


# j%t = 10 # SyntaxError: invalid syntax


# ---
# Literals :- Literals are the data which is given in a variable or constant. Literals are constants in python 
# Whatever values you are storing inside a variable is called literal

# n1 = 10 # Here 10 is a literal

# ---
# Punctuators :- Punctuators are the special symbols which have a special meaning in python
# Some punctuators are :- ( ) , : . [ ] { } ; @ = 
# Some examples of punctuators
# ( ) :- Parenthesis
def func1():  # Here ( ) is a punctuator
    pass
# : :- Colon
if True:  # Here : is a punctuator
    pass
# . :- Dot
str1 = "Hello World"
print(str1.upper())  # Here . is a punctuator
# [ ] :- Square Brackets
list1 = [1, 2, 3, 4, 5]  # Here [ ] is a punctuator
# { } :- Curly Braces
dict1 = {"name": "John", "age": 30}  # Here { } is a punctuator
# , :- Comma
tuple1 = (1, 2, 3, 4, 5)  # Here , is a punctuator
# ; :- Semicolon
a = 10; b = 20  # Here ; is a punctuator
# @ :- At the rate
class MyClass:  # Here @ is a punctuator
    @classmethod
    def func2(cls):
        pass
# = :- Equal to
x = 10  # Here = is a punctuator
# ---
