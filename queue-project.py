"""
Implementation a Queue using a List
"""

from typing import Any
from collections import deque


class Queue:
    """
    A queue class using a list to store elements
    """

    def __init__(self) -> None:
        """
        Initialises an instance of the queue class

        Attributes:
        queue_items (list[Any]) : contains the queue items
        """
        self.queue_items = [Any]

    def enqueue(self, element: Any) -> None:
        """Add an element to the back of the list"""
        self.queue_items.append(element)  # O(1)

    def dequeue(self) -> Any:
        """Remove an element from the front of the list and returns it"""
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items.pop(0)  # O(n)

    def is_empty(self) -> bool:
        """Returns True is the queue is empty, else returns False"""
        return len(self.queue_items) == 0  # O(1)

    def peek(self) -> Any:
        """Returns the first item in the list, without removing it"""
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items[0]  # O(1)


class ImprovedQueue:
    """
    A queue class using a deque to store elements
    """

    def __init__(self) -> None:
        """Initialise an instance of the queue class"""
        self.queue_items = deque()  # --> improvement

    def enqueue(self, element : Any) -> None:
        """Add an element to the back of the list"""
        self.queue_items.append(element)  # O(1)

    def dequeue(self) -> Any:
        """Remove an element from the front of the list and returns it"""
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items.popleft()  # O(1) --> improvement

    def is_empty(self) -> bool:
        """Returns True is the queue is empty, else returns False"""
        return len(self.queue_items) == 0  # O(1)

    def peek(self) -> Any:
        """Returns the first item in the list, without removing it"""
        if len(self.queue_items) == 0:
            raise ValueError("Queue is empty")
        return self.queue_items[0]  # O(1)


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
