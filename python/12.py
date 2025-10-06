# Types of Inheritance :-

# Single Inheritance
# Multiple Inheritance
# Multi-level Inheritance
# Hybrid Inheritance
# Hierarchical Inheritance?

# Single Inheritance :- we done in previous file 11.py


# Multiple Inheritance:- In multiple Inheritance , the child inherits from more than 1 parent class 

# parent 1              parent 2
#        \              /  
#         \            /
#          \          /
#           \        /
#            \      /
#             \    /
#              \  /
#               VV
#             child


# Parent class One 

class Parent1():
    def assign_string_one(self,str1):
        self.str1 = str1
    
    def show_string_one(self):
        return self.str1
    
# Parent class Two 

class Parent2():
    def assign_string_two(self,str2):
        self.str2 = str2 
    
    def show_string_two(self):
        return self.str2 
    
# Child class 

class Derived(Parent1,Parent2):
    def assign_string_three(self,str3):
        self.str3 = str3 
    
    def show_string_three(self):
        return self.str3
    
c = Derived()
c.assign_string_one("string 1")
c.assign_string_two("string 2")
c.assign_string_three("string 3")

print(c.show_string_one())  # output : string 1
print(c.show_string_two()) # output : string 2
print(c.show_string_three()) # output :string 3 




#-----

# Method Resolution Order (MRO )
# When multiple parent class define methods with the same name , Python uses MRO to decide which method to call 

class A :
    def greet(self):
        print("Hello from A")

class B :
    def greet(self):
        print("Hello from B")

class C(A,B) :
    pass

c = C()
c.greet()   # output: Hello from A

print(C.__mro__) # shows method resolution order 

#output:
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

# MRO Rule:
# Python uses C3 linearization to determine the order. You can inspect it using ClassName.__mro__.



#---

# Constructor Chaining with super()
# If both parent classes have __init__ methods, you should use super() carefully to ensure all initializations happen.

class Parent1:
    def __init__(self):
        print("Parent1 constructor")

class Parent2:
    def __init__(self):
        print("Parent2 constructor")

class Derived(Parent1, Parent2):
    def __init__(self):
        super().__init__()  # Only calls Parent1's constructor due to MRO

d = Derived()  # Parent1 constructor


# To call both constructors, you can explicitly invoke them:

class Derived(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

e = Derived()

# output:
# Parent1 constructor
# Parent2 constructor


# Or use cooperative super() if both parents also use super():
class Parent1:
    def __init__(self):
        super().__init__()
        print("Parent1 constructor")

class Parent2:
    def __init__(self):
        super().__init__()
        print("Parent2 constructor")

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("Child constructor")


# This works because super() follows MRO and calls each constructor in order.

# In multiple inheritance, cooperative super() allows each class in the hierarchy to call the next class's method in the MRO chain — not just its immediate parent. This ensures that all constructors (or methods) in the chain get called, once and in order


# Key Rule: Use super() in All Classes
# For cooperative inheritance to work:

# Every class must use super() — even if it’s not the direct parent

# Avoid hardcoding parent class names like Parent1.__init__(self) unless necessary


# Diamond Problem in Inheritance
# This occurs when two parent classes inherit from the same base class, and the child inherits from both. Python handles this using MRO.

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Output: Hello from B (MRO: D → B → C → A)
