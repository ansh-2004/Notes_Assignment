# Hierarchical Inheritance :- Hierarchical inheritance occurs when multiple child classes inherit from a single parent class. Each child class gets access to the parent’s methods and attributes but can also define its own.

#         Parent
#        /     \
#   Child1    Child2


# Parent class
class Animal:
    def speak(self):
        return "Animal makes a sound"

# Child classes
class Dog(Animal):
    def speak(self):
        return "Dog says Woof!"

class Cat(Animal):
    def speak(self):
        return "Cat says Meow!"


d = Dog()
c = Cat()

print(d.speak())  # Output: Dog says Woof!
print(c.speak())  # Output: Cat says Meow!

# Each child class (Dog, Cat) inherits from Animal and overrides the speak() method.


# Advanced Concepts
# 1. Shared Methods from Parent
# You can define common methods in the parent and use them in all children:

# python
# class Animal:
#     def eat(self):
#         return "Eating food"

# class Dog(Animal):
#     def bark(self):
#         return "Woof!"

# class Cat(Animal):
#     def meow(self):
#         return "Meow!"
# python
# dog = Dog()
# cat = Cat()

# print(dog.eat())  # Shared method
# print(cat.eat())  # Shared method
# 2. Adding Unique Behavior
# Each child can have its own unique methods while still inheriting shared ones:

# python
# class Bird(Animal):
#     def fly(self):
#         return "Flying high"
# 3. Constructor Inheritance
# You can use super() to call the parent’s constructor:

# python
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed