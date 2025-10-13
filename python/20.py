# Queue
# - Linear Data Structure
# - Follows FIFO : First In First Out 
# - Insertion can take place from the rear end. 
# - Deletion can take place from the front end. 
# - Eg. queue at ticket counters , bus station 
# - 4 major operations:
#    - enqueue(ele) - used to insert element at top 
#    - dequeue() - removes the top element from queue 
#    - peekfirst() - to get the first element of queue 
#    - peeklast() - to get the last element of queue 
# - All opeations works in constant time i.e, O(1)

# Applications of queue:- 
# - Scheduling 
# - Maintaining Playlist 
# - Interrupt handling 


# Queue Implementation 

# class Queue:
    # def __init__(self):
        # self.queue = []
    # def enqueue(self,item):
        # self.queue.append(item)
    # def dequeue(self):
        # if len(self.queue) < 1:
            # return None
        # return self.queue.pop(0)
    # def peekfirst(self):
    #     return self.queue[0] if self.queue else None

    # def peeklast(self):
    #     return self.queue[-1] if self.queue else None
    # def display(self):
        # print(self.queue)
    # def size(self):
        # return len(self.queue)
    

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)

# q.display() # output:- [1, 2, 3, 4, 5]
# q.dequeue()
# print("After removing an element")
# q.display() # output:- [2, 3, 4, 5]
# q.dequeue()
# q.display() # output:- [3, 4, 5]


# Circular Queue:- A circular queue is a fixed-size queue where the last position wraps around to the first -- forming a circle. It is useful for memory-efficient designs. Avoids shifting element like in a regular queue. 


class MyCircularQueue():
    def __init__(self,k):
        self.k = k 
        self.queue = [None] * k 
        self.head = self.tail = -1
    
    def enqueue(self,data):
        if((self.tail + 1) % self.k == self.head):
            print("The circular queue is full \n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0 
            self.queue[self.tail] = data 
        else:
            self.tail = (self.tail + 1) % self.k 
            self.queue[self.tail] = data 
    
    def dequeue(self):
        if(self.head == -1):
            print("The circular queue is empty now \n")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1 
            self.tail = -1 
            return temp 
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k 
            return temp 
    
    def printQueue(self):
        if(self.head == -1):
            print("No element in the circular queue is found")
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i],end = " ")
            print()
        else:
            for i in range(self.head,self.k):
                print(self.queue[i],end = " ")
            for i in range(0,self.tail + 1):
                print(self.queue[i], end = " ")
            print()


obj = MyCircularQueue(5)

obj.enqueue(12)
obj.enqueue(22)
obj.enqueue(31)
obj.enqueue(44)
obj.enqueue(57)
print("Initial queue values")
obj.printQueue()  # output: 12 22 31 44 57 

obj.dequeue()
print("After removing an element from the queue")
obj.printQueue() # output: 22 31 44 57 

obj.dequeue()
obj.printQueue() # output: 31 44 57


# Advantages 
# - Maintains data in FIFO manner 
# - Insertion from beginning and deletion from end takes O(1) time 

# Disadvantages 
# - Manipulation is restricted front and rear. 
# - Not much flexible. 


# Difference with regular queue 
# - In a regular queue, after several dequeue() operations, the front of the list becomes empty. But python lists don't automatically reuse that space - they just grow longer. Circular queues reuse that space. In a circular queue, we use modulo arithmetic to wrap around. so when we reach the end of the list, we go back to the beginning. 

# ```python
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue()
# enqueue(4)
# enqueue(5)
# enqueue(6)
# ```

# Let’s assume the circular queue has a **fixed size of 5**. We’ll track:

# - `head`: where we remove from
# - `tail`: where we insert
# - `queue`: the actual list

# ---

### 🔹 Initial State
# ```
# queue = [None, None, None, None, None]
# head = -1
# tail = -1
# ```

# ---

### 🔹 enqueue(1)
# - Queue is empty → set `head = 0`, `tail = 0`
# - Insert at index 0

# ```
# queue = [1, None, None, None, None]
# head = 0
# tail = 0
# ```

# ---

### 🔹 enqueue(2)
# - Move `tail = (0 + 1) % 5 = 1`
# - Insert at index 1

# ```
# queue = [1, 2, None, None, None]
# head = 0
# tail = 1
# ```

# ---

### 🔹 enqueue(3)
# - Move `tail = (1 + 1) % 5 = 2`
# - Insert at index 2

# ```
# queue = [1, 2, 3, None, None]
# head = 0
# tail = 2
# ```

# ---

### 🔹 dequeue()
# - Remove from `head = 0`
# - Move `head = (0 + 1) % 5 = 1`

# ```
# queue = [None, 2, 3, None, None]
# head = 1
# tail = 2
# ```

# ---

### 🔹 enqueue(4)
# - Move `tail = (2 + 1) % 5 = 3`
# - Insert at index 3

# ```
# queue = [None, 2, 3, 4, None]
# head = 1
# tail = 3
# ```

# ---

### 🔹 enqueue(5)
# - Move `tail = (3 + 1) % 5 = 4`
# - Insert at index 4

# ```
# queue = [None, 2, 3, 4, 5]
# head = 1
# tail = 4
# ```

# ---

### 🔹 enqueue(6)
# - Move `tail = (4 + 1) % 5 = 0`
# - Index 0 is empty, so we can insert!

# ```
# queue = [6, 2, 3, 4, 5]
# head = 1
# tail = 0
# ```

# ✅ Final queue: `[6, 2, 3, 4, 5]` (but remember: logical order starts from `head = 1`)

# So the actual order is: `2 → 3 → 4 → 5 → 6`

# ---

