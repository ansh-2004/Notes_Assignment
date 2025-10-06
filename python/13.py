# Multi-Level Inheritance :- In multi-level inheritance , we have Parent , child , grand-child relationship 

#               Parent
#                 |
#                 |
#                 |
#                 V
#               Child
#                 |
#                 |
#                 |
#                 V 
#            Grand-Child
 

# Parent Class 

class Parent():
    def assign_name(self,name):
        self.name = name 
    
    def show_name(self):
        return self.name

# child class 

class Child(Parent):
    def assign_age(self, age):
       self.age = age 
    
    def show_age(self):
        return self.age 
    
# grand-child class 

class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender = gender 

    def show_gender(self):
        return self.gender
    

gc = GrandChild()

gc.assign_name("ansh")
gc.assign_age(20)
gc.assign_gender("Male")

print(gc.show_name()) # output: ansh
print(gc.show_age())  # output: 20
print(gc.show_gender()) # output: Male



# Method Overriding
# You can override methods from parent classes in child or grandchild classes to change their behavior.

class Parent():
    def show_info(self):
        return "Parent Info"

class Child(Parent):
    def show_info(self):  # Overrides Parent's method
        return "Child Info"


c = Child()

print(c.show_info())  # output: Child Info




#---

# Constructors in Multi-Level Inheritance
# Use super() to call constructors of parent classes properly:


class Parent():
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class GrandChild(Child):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender
# This ensures all attributes are initialized correctly.