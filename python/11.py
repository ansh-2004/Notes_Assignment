# Inheritance in python 
# With inheritance one class can derive the properties of another class . eg. A man inheriting features from his father 


# parent class / base class  
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost 
    def show_details(self):
        print("I am a vehicle")
        print("Mileage of vehicle is", self.mileage)
        print("cost of vehicle is ",self.cost)
    

v1 = Vehicle(500,500)
v1.show_details()

print("mileage of v1 is ",v1.mileage)  

# output:
# I am a vehicle
# Mileage of vehicle is 500
# cost of vehicle is  500
# mileage of v1 is  500

# child class 

class Car(Vehicle):  # to create child class , we have parenthesis and inside that we pass parent class
    def show_car(self):
        print("I am a car ")


c1 = Car(200,200)  # Although i don't have constructor in child class but i am passing it the value . this is because car class is inheriting the vehicle class, so this will automatically have all two methods of vehcle class , the init method and show_details method  

c1.show_details()

# output:
# I am a vehicle
# Mileage of vehicle is 200
# cost of vehicle is  200


c1.show_car() # output:- I am a car                  


# ----


# so we saw python will automatically use the constructor from the parent class if we don't define the constructor in child class 
# But also we can override the constructor in child class using super() keyword

# Over-riding init method 

class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):       # Over-riding init method
        super().__init__(mileage,cost)      
        self.tyres = tyres
        self.hp = hp 
    
    def show_car_details(self):
        print("I am a car ")
        print("Number of tyres are",self.tyres)
        print("value of horse power is ",self.hp)


# invoking show_details() method from parent class 
c1 = Car(20,12000,4,300)
c1.show_details()

# output:
# I am a vehicle
# Mileage of vehicle is 20
# cost of vehicle is  12000


c1.show_car_details()

# output:
# I am a car 
# Number of tyres are 4
# value of horse power is  300


#---
# These built-in functions help verify relationships between objects and classes.
print(isinstance(c1, Car))  # True
# this is because of polymorphism, where you can treat objects of different subclasses as instances of a common superclass.
print(issubclass(Car, Vehicle))  # True



#---

# Access Modifiers (Encapsulation )
# Python uses naming conventions to simulate private and protected members 

class Vehicle:
    def __init__(self, mileage, cost):
        self._mileage = mileage       # Protected
        self.__cost = cost            # Private

# Protected Members
# Prefix with a single underscore: _variable

# Meant to be used within the class and its subclasses

# Not enforced by Python, but it's a soft convention
class Vehicle:
    def __init__(self, mileage):
        self._mileage = mileage  # Protected

class Car(Vehicle):
    def show_mileage(self):
        print("Mileage:", self._mileage)  # Accessible


obj = Car(45)
print("mileage of obj is ",obj._mileage)   # mileage of obj is  45

# can access becasue 
# In Python, a single underscore prefix (like _mileage) is a convention, not a strict rule. It signals to other developers:

# “This is meant for internal use. Please don’t touch it unless you know what you're doing.”

# But Python does not enforce access restrictions for protected members. So yes, you can access _mileage directly from outside the class:
# This is allowed, but it's considered bad practice unless you have a good reason.




# Private Members

# Prefix with double underscore: __variable

# Python performs name mangling to make it harder to access from outside the class
class Vehicle:
    def __init__(self, cost):
        self.__cost = cost  # Private

    def show_cost(self):
        print("Cost:", self.__cost)

v = Vehicle(10000)
v.show_cost()          # ✅ Works
# print(v.__cost)        # ❌ Error: AttributeError
print(v._Vehicle__cost)  # ✅ Works (name mangling)

# What is Name Mangling?
# Name mangling is Python's way of making private variables harder to access from outside the class. It’s not true privacy (like in Java or C++), but a protective mechanism.

# When you define a variable with two leading underscores (e.g., __cost), Python internally changes its name to include the class name. This prevents accidental access or modification.

class Vehicle:
    def __init__(self, cost):
        self.__cost = cost  # Private variable

    def show_cost(self):
        print("Cost:", self.__cost)

v = Vehicle(10000)
v.show_cost()           # ✅ Works fine

# print(v.__cost)         # ❌ AttributeError: 'Vehicle' object has no attribute '__cost'

# What actually happens:
# Python renames __cost to _Vehicle__cost internally.

# So you can still access it like this:

# python
print(v._Vehicle__cost)  # ✅ Works: prints 10000