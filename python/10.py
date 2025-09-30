# Python Object Oriented Programming

# classes :- it is a template/blue-print for real world entities . Example Mobile Phone
# There are two things associated with classes :- Properties/Attributes and Behavior/Methods
# Properties/Attributes like color , cost , battery life 
# Behavior/Methods like Make calls , watch videos , play games

# class is a user defined data type similar to predefined data types like int ,float, bool , str  


# Objects:- They are specific instances of a class 
# eg. for a mobile phone class ,objects can be Apple , Motorola, Samsung


class Phone:
    def make_call(self): # with self parameter, you will able to invoke attributes which are present in this class 
        print("Making phone call")
    def play_games(self):
        print("Playing game")


p1 = Phone() # instantiaing the p1 object

p1.make_call() # invoking methods through object 

p1.play_games() # invoking methods through object 

# output:
# Making pone call
# Playing game

#---

class Phone:

    def set_color(self,color):
        self.color = color

    def set_cost(self,cost):
        self.cost = cost

    def show_color(self):
        return self.color 
    
    def show_cost(self):
        return self.cost 
    
    def make_call(self): 
        print("Making pone call")

    def play_games(self):
        print("Playing game")
    

p1 = Phone()
p1.set_color("blue")
p1.set_cost("999")

# print(p1.show_color())  # output: blue
# print(p1.show_cost())   # output: 999


# code works even though you didn't explicitly define attributes like color or cost inside the class:

# In Python, you can dynamically add attributes to an object at runtime using the self keyword inside methods.
# def set_color(self, color):
#     self.color = color

# When you call p1.set_color("blue"), Python creates a new attribute color on the p1 object and sets its value to "blue".

# Similarly, self.cost = cost creates the cost attribute when set_cost() is called.

# These attributes don’t need to be declared in advance like in some other languages (e.g., Java or C++).


# Object vs Class Attributes
# You're creating instance attributes (specific to p1) dynamically.
# If you wanted to define them upfront, you'd typically use the __init__ method:
# class Phone:
#     def __init__(self, color, cost):
#         self.color = color
#         self.cost = cost
# This ensures every object has those attributes from the moment it's created.


# about __init__ method:

#  The `__init__` method in Python is a **special method** used to initialize objects when a class is instantiated. Think of it as the **constructor** of the class—it sets up the object with its initial state.

# ---

# ### 🧱 What Is `__init__`?

# - It's automatically called **when you create an object** from a class.
# - It allows you to **pass parameters** and assign them to the object's attributes.
# - The double underscores (`__`) indicate it's a **special method** in Python.

# ---

# ### 📦 Example: Using `__init__` in a Class

# ```python
# class Phone:
#     def __init__(self, color, cost):
#         self.color = color
#         self.cost = cost

#     def show_color(self):
#         return self.color

#     def show_cost(self):
#         return self.cost
# ```

# Now when you create a `Phone` object:

# ```python
# p1 = Phone("blue", 999)
# print(p1.show_color())  # Output: blue
# print(p1.show_cost())   # Output: 999
# ```

# ---

# ### 🔍 How It Works

# - `p1 = Phone("blue", 999)` calls `__init__` with `"blue"` and `999`.
# - Inside `__init__`, `self.color = color` and `self.cost = cost` store those values in the object.
# - `self` refers to the **current instance** of the class.

# ---

# ### ✅ Benefits of Using `__init__`

# - Makes object creation **clean and consistent**
# - Avoids needing separate `set_` methods
# - Ensures all required attributes are set at creation

# ---


# -----

# self vs __init__

# ---

# ### 🧠 `self`: Refers to the Current Object

# - `self` is **not a keyword**, but a **convention**.
# - It refers to the **instance** of the class you're working with.
# - You use `self` to access or set attributes and methods **inside the class**.

# #### Example:
# ```python
# def set_color(self, color):
#     self.color = color  # 'self.color' is an attribute of the object
# ```

# Here, `self.color` means “the `color` attribute of this particular object.”

# ---

# ### 🧱 `__init__`: Initializes the Object

# - `__init__` is a **special method** that runs **automatically** when you create an object.
# - It’s used to **set up initial values** (attributes) for that object.
# - You still use `self` inside `__init__` to assign values to the object.

# #### Example:
# ```python
# class Phone:
#     def __init__(self, color, cost):
#         self.color = color
#         self.cost = cost
# ```

# Now when you do:
# ```python
# p1 = Phone("blue", 999)
# ```

# Python automatically calls `__init__`, and sets `p1.color = "blue"` and `p1.cost = 999`.

# ---

# ### 🔍 So What's the Difference?

# | Concept     | Role | When It's Used | Example |
# |-------------|------|----------------|---------|
# | `self`      | Refers to the object itself | Inside any method | `self.color = color` |
# | `__init__`  | Initializes the object | Automatically during object creation | `def __init__(...)` |

# ---

# ### 🧪 Why You Could Set Values Without `__init__`

# You used methods like `set_color()` to assign values manually:
# ```python
# p1.set_color("blue")
# ```

# This works because Python lets you **add attributes dynamically** to objects. But using `__init__` is cleaner and ensures all attributes are set **at creation time**, which is especially useful in larger programs.

# ---


# Creating a class with constructor 

class Employee:
    
    def __init__(self,name,age,salary,gender):  # init method acts as the constructor 
        self.name = name
        self.age = age 
        self.salary = salary 
        self.gender = gender 
    
    def employee_details(self):
        print("Name of employee is",self.name)
        print("Age of employee is ",self.age)
        print("Salary of employee is ",self.salary)
        print("Gender of employee is ",self.gender)


# employe1 = Employee("ansh",20,25000,"male")
# employe1.employee_details()

# print("-----------------------")
# employe2 = Employee("gupta",22,25000,"male")
# employe2.employee_details()

# output:
# Name of employee is ansh
# Age of employee is  20
# Salary of employee is  25000
# Gender of employee is  male
# -----------------------
# Name of employee is gupta
# Age of employee is  22
# Salary of employee is  25000
# Gender of employee is  male













