# Flow Control statements in pyhton 

# Decision Making statements 

# If statement 
a=10
b=20
# if b > a:
#     print("b is greater than a")  # output :- b is greater than a

# if a > b:
#     print("a is greater than b ") # output :- no any output as condition is false 


#---

# if a > b:
#     print("a is greater than b")
# else:
#     print("b is greater than a ")  # output:- b is greater than a 
    

#---

# elif 

# a = 10
# b = 20
# c = 30

# if (a>b) & (a>c) :
#     print("a is the greatest")
# elif (b>a) & (b > c):
#     print("b is greatest")
# else:
#     print("c is the greatest")       # output: c is the greatest


#---
# Tuple with if 
# tup1 = ("a","b","c",5)
# if 5 in tup1:
#     print("5 is present in tup1")


#---
# list with if 
# li=["a","b","c"]
# if li[0] == 'a':
#     li[0] = 100
# print(li)


#---

# Dictionary with if 
d1 = {"k1":10,"k2":20,"k3":30}
if d1["k1"] == 10:
    d1["k1"] = d1["k1"] + 100

print(d1)