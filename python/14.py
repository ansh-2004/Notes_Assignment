# Hybrid Inheritance :- It is a combination of two or more types of inheritance (like single , multiple, multilevel,hierarchical ) in one program. It allows you to model complex relationships between classes. 


#              Base
#               /\
#              /  \
#             /    \
#          classA  classB
#            \      /
#             \    /
#             Derived
# 

# This combines multiple inheritance (Derived inherits from ClassA and ClassB) and hierarchical inheritance (ClassA and ClassB inherit from Base).

# Base class
class Animal:
    def speak(self):
        return "Animal sound"

# Intermediate classes
class Mammal(Animal):
    def give_birth(self):
        return "Gives birth to young ones"

class Bird(Animal):
    def lay_eggs(self):
        return "Lays eggs"

# Hybrid class
class Platypus(Mammal, Bird):
    def unique_trait(self):
        return "Can swim and lay eggs"


p = Platypus()
print(p.speak())         # From Animal
print(p.give_birth())    # From Mammal
print(p.lay_eggs())      # From Bird
print(p.unique_trait())  # From Platypus

# output:
# Animal sound
# Gives birth to young ones
# Lays eggs
# Can swim and lay eggs


print(Platypus.__mro__) # (<class '__main__.Platypus'>, <class '__main__.Mammal'>, <class '__main__.Bird'>, <class '__main__.Animal'>, <class 'object'>)


#---

# Using super() in hybrid inheritance 
# super() helps call methods from parent classes in a clean and predictable way.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(A):
    def show(self):
        super().show()
        print("C")

class D(B, C):
    def show(self):
        super().show()
        print("D")

d = D()
d.show()


# output:
# A
# C
# B
# D


# Step-by-Step Execution
# When you call d.show(), here's what happens:

# 1. D.show() is called
# super().show() inside D refers to the next class in the Method Resolution Order (MRO), which is B.

# 2. B.show() is executed
# Inside B.show(), super().show() refers to the next class in the MRO after B, which is C.

# 3. C.show() is executed
# Inside C.show(), super().show() refers to the next class in the MRO after C, which is A.

# 4. A.show() is executed
# This prints "A".

# 5. Backtrack and continue
# After A.show(), control returns to C.show(), which prints "C".

# Then back to B.show(), which prints "B".

# Finally back to D.show(), which prints "D".


# super() doesn't always mean "parent class"—it means "next in MRO".

# This structure avoids the diamond problem by ensuring each method is called only once in a predictable order.