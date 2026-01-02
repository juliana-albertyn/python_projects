"""
Module: doubly-linked-list-queue
Purpose: Implements a queue using a doubly linked list
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-02"

from typing import Any, Optional


class Node:
    """
    This class contains an element, and pointers to the next and
    previous elements in the queue.

    Attributes:
    element(Any): the data stored in the node.
    next(Optional[Node]): a pointer to the next node.
    prev(Optional[Node]): a pointer to the previous node.
    """

    def __init__(self, element: Any) -> None:
        """Creates an instance of the Node class."""
        self.element = element
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None


class Queue:
    """
    A doubly linked list of elements.

    Attributes
    head (Optional[Node]): the first node in the queue.
    tail (Optional[Node]): the last node in the queue.
    length (int): the number of nodes in the queue.
    """

    def __init__(self) -> None:
        """Creates an instance of the Queue class."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length = 0

    def __len__(self) -> int:
        """Returns the number of items in the queue."""
        return self.length

    def enqueue(self, element: Any) -> None:
        """Adds an element to the end of the queue."""
        node = Node(element)
        if len(self) == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return
        if self.tail is None:
            raise RuntimeError("Tail should never be None here")
        prev_tail = self.tail
        self.tail = node
        self.tail.prev = prev_tail
        prev_tail.next = node
        self.length += 1

    def dequeue(self) -> Any:
        """Removes and returns the first element in the queue."""
        if len(self) == 0:
            raise ValueError("Queue is empty")
        if self.head is None:
            raise RuntimeError("Head should never be None here")
        prev_head = self.head
        self.head = prev_head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return prev_head.element

    def peek(self) -> Any:
        """Returns the first element in queue without removing it."""
        if len(self) == 0:
            raise ValueError("Queue is empty")
        if self.head is None:
            raise RuntimeError("Head should never be None here")
        return self.head.element

    def is_empty(self) -> bool:
        """Returns True is the queue is empty, else returns False."""
        return len(self) == 0


try:
    print("-- create queue class --")
    q = Queue()
    print(f"Empty? {q.is_empty()}")

    print("-- enqueue items --")
    for item in range(1, 21):
        q.enqueue(item)
    print(f"Length: {len(q)}")

    print("-- dequeue items --")
    for item in range(1, 11):
        print(q.dequeue())
    print(f"Length: {len(q)}")

    print("-- enqueue more items --")
    for item in range(21, 26):
        q.enqueue(item)
    print(f"Length: {len(q)}")

    print(f"Peek: {q.peek()}")

    print(f"Dequeue: {q.dequeue()}")

    print(f"Peek: {q.peek()}")

    print("-- dequeue past the end of the queue --")
    for item in range(1, 21):
        print(q.dequeue())

except ValueError as e:
    print(e)
except RuntimeError as e:
    print(e)
