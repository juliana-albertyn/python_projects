"""
Co-Pilot prompt
Project 1 (Beginner Level): **Implement a Queue using a List**
Concepts reinforced: arrays/lists, abstract data type (queue), FIFO behavior, Big‑O reasoning.

1. Create a `Queue` class with the following methods:
   - `enqueue(element)` → adds an element to the back of the queue.
   - `dequeue()` → removes and returns the front element.
   - `is_empty()` → returns `True` if the queue is empty.
   - `peek()` → returns the front element without removing it.
2. Internally, use a Python list to store the elements.
3. Demonstrate the queue by enqueuing a few items, dequeuing them, and printing results.
4. Add a short comment in your code explaining the **time complexity** of each operation (`O(1)` or `O(n)` depending on how you implement it).
#"""

from collections import deque

class Queue:
    def __init__(self):
        self.queue_items = []

    def enqueue(self, element):
        self.queue_items.append(element) # O(1)

    def dequeue(self):
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items.pop(0) # O(n)

    def is_empty(self):
        return len(self.queue_items) == 0 # O(1)

    def peek(self):
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items[0] # O(1) 
    
class ImprovedQueue:
    def __init__(self):
        self.queue_items = deque() # --> improvement

    def enqueue(self, element):
        self.queue_items.append(element) # O(1)

    def dequeue(self):
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items.popleft() # O(1) --> improvement

    def is_empty(self):
        return len(self.queue_items) == 0 # O(1)

    def peek(self):
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items[0] # O(1)


q = Queue()
try:
    print(q.is_empty())
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("carrot")
    print(q.is_empty())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
except ValueError as e:
    print(e)

q = ImprovedQueue()
try:
    print(q.is_empty())
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("carrot")
    print(q.is_empty())
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
except ValueError as e:
    print(e)    