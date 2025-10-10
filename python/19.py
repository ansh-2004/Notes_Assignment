# Stack 

# - Linear data structure 
# - It follows Last In First Out (LIFO) order. 
# - Insertion and removal of the element has done at one end. 
# - Push is used for inserting an element in a stack . 
# - Pop is used to removal an element in a stack 


# ---
# Functions associated with Stack 

# push(x) - It is used to insert the element 'x' at the end of a stack . 
# pop() - It is used to remove the topmost/last element of a stack . 
# size() - gives the size/length of a stack . 
# top() - give reference of last element present in stack . 
# empty() - returns true for an empty stack . 


# ---

# Implementation of stack 

# Several ways to implement stack in python 

# - list 
# - collections.deque
# - queue.LifoQueue

# 1. Implementation using list 
# - List in python can be used as stack 
#     - append() - It is used to insert the element 
#     - pop() - It is used to remove the last element 

# Logic - 

# stack = []
# stack.append("abc")
# print(stack) # output: ['abc']
# print(type(stack)) # output : <class 'list'>
# print(stack.pop()) # output: abc
# print(stack) # output: []                      


# stack = []
# stack.append("Welcome")
# stack.append("to")
# stack.append("great learning")
# print(stack,end= " ")  # output: ['Welcome', 'to', 'great learning'] 

# print(stack.pop()) # output : great learning
# print(stack.pop()) # output : to

# print(stack) # output: ['Welcome']


#----

# 2. Implementation using deque (Double ended queue)

# - Stacks in python are created by the collection module which provides deque class. 
# - append and pop operations are faster in deque as compare to list beacause time complexity of deque is O(1) whereas time complexity of list is O(n)

# logic - 

# from collections import deque 
# stack = deque()
# print(stack) # output: deque([])
# print(type(stack)) # output: <class 'collections.deque'>
# stack.append("abc")
# print(stack) # output: deque(['abc'])
# print(stack.pop()) # output: abc


# from collections import deque 
# stack = deque()

# stack.append("x")
# print(stack) # output: deque(['x'])
# stack.append("y")
# stack.append("z")
# print(stack) # output : deque(['x', 'y', 'z'])

# print(stack.pop()) # output :- z
# print(stack) # output:- deque(['x', 'y'])

#---

# 3. Implementation using queue

# - Queue module contains the LIFO queue.
# - It is having some additional functions and works same as stack. 
# - put functions is used to insert the data in queue. 
# - get function is used to remove the element. 


# Functions available in queue module-

# get() - It is used to remove the element from the queue. 
# maxsize() - used to put the maximum number of items allowed in queue.
# empty() - It returns true, when queue is empty else false. 
# full() - When queue is full return True. 
# put(x) - It is used to insert x in queue. 
# qsize() - gives the size of a queue. 

# Logic 
# from queue import LifoQueue
# stack = LifoQueue()
# stack.put(2)
# stack.get() 


from queue import LifoQueue
stack = LifoQueue()

print(stack) # output : <queue.LifoQueue object at 0x0000021270C59940> # Prints the object reference, not the contents.

stack.put(2)
stack.put(3)
stack.put("hlo")

print(stack) # output: <queue.LifoQueue object at 0x0000021270C59940> # Prints the object reference, not the contents.
print(type(stack)) # output : <class 'queue.LifoQueue'> 
print(stack.qsize()) # output : 3


# giving maxsize to this 
stack = LifoQueue(maxsize=3)
print(stack.full()) # output: False
stack.put(2)
stack.put(3)
stack.put("hlo")

print(stack.full())  # output: True
# stack.put("element")  # terminal get struck /frozen because
stack.put("element",timeout=2)  # now 2 seconds after struck we get error 

# ```
# Traceback (most recent call last):
#   File "C:\Users\ansh.gupta\Documents\Work\Notes_Assignment\python\19.py", line 135, in <module>
#     stack.put("element",timeout=2)  
#     ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\ansh.gupta\AppData\Local\Programs\Python\Python313\Lib\queue.py", line 169, in put
#     raise Full
# queue.Full
# ```


# By default, put() is a blocking call. If the queue is full, it will wait indefinitely until space becomes available.Since maxsize=3 and you've already added 3 items (2, 3, "hlo"), the queue is full.So stack.put("element") just waits forever, causing your terminal to appear frozen.

# to fix this :
# 2. Use put() with a Timeout
# You can specify how long to wait before giving up.

# stack.put("element", timeout=2)  # Waits 2 seconds, then raises Full

# Or 
# 1. Use put_nowait() Instead
# This method raises an exception immediately if the queue is full.

# python
# from queue import LifoQueue, Full

# stack = LifoQueue(maxsize=3)
# stack.put(2)
# stack.put(3)
# stack.put("hlo")

# try:
#     stack.put_nowait("element")
# except Full:
#     print("Stack is full! Cannot add more items.")

                                                                                             