"""
Module: queue-with-fixed-size-array
Purpose: Implement a circular queue
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-02"

from typing import Any

class Queue:
    """
    A circular queue.

    Attributes
    queue_items (list[Any]) : the list containing the elements.
    capacity (int) : the maximnum number of elements allowed.
    head (int) : the index of the front element.
    tail (int) : the index where the next element will be inserted.
    length (int) : the number of elements.
    """
    def __init__(self):
        """ Initialise an instance of Queue. """
        self.queue_items : list[Any] = []
        self.capacity = 0
        self.head = 0
        self.tail = 0
        self.length = 0

    def __len__(self) -> int:
        """ Returns the number of items currently in the list. """
        return self.length

    def enqueue(self, element: Any) -> None:
        """ Add an element at the tail. """
        if len(self) == self.capacity:
            raise OverflowError("Queue is full")
        self.queue_items.append(element)
        self.tail = (self.tail + 1) % self.capacity
        self.length += 1

    def dequeue(self) -> Any:
        """ Remove the element at the head. """
        item = None 
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        if self.queue_items[self.head] is not None:
            item = self.queue_items[self.head]
            self.queue_items.pop(self.head)
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return item

    def peek(self) -> Any:
        """ Return the element at the head without removng it. """
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items[self.head]

    def is_empty(self) -> bool:
        """ Returns True if the list is empty, False if it contains elements. """
        return self.length == 0

    def is_full(self) -> bool:
        """ Returns True if the list is filled to capacity, else returns False. """
        return self.length == self.capacity

    
q = Queue()
q.capacity = 5
print(f"Empty?: {q.is_empty()}")    
for item in range(101, 106):
    q.enqueue(item)
print(f"Count: {len(q)} Head index: {q.head} Tail index: {q.tail}")    
print(f"Full?: {q.is_full()}")    
print(f"Dequeue: {q.dequeue()}")
print(f"Count: {len(q)} Head index: {q.head} Tail index: {q.tail}")    
print(f"Dequeue: {q.dequeue()}")
print(f"Count: {len(q)} Head index: {q.head} Tail index: {q.tail}")    
print(f"Enqueue: {q.enqueue(201)}")
print(f"Count: {len(q)} Head index: {q.head} Tail index: {q.tail}")    
print(f"Enqueue: {q.enqueue(202)}")
print(f"Count: {len(q)} Head index: {q.head} Tail index: {q.tail}")    
