"""
Module: queue-using-two-stacks
Purpose: Implement a Queue using two Stack objects
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-02"

from typing import Any


class Stack:
    """Stack class to store elements of queue."""

    def __init__(self) -> None:
        """
        Initialise an instance of a Stack.

        Attributes
        elements (list[Any]) : stores the elements in the stack.
        """
        self._elements: list[Any] = []

    def __len__(self) -> int:
        """Returns the number of elements in the stack."""
        return len(self._elements)

    def __str__(self) -> str:
        """Returns a string representation of a stack."""
        return str(self._elements)

    def push(self, element: Any) -> None:
        """Add a new element to the top of the stack."""
        self._elements.append(element)

    def pop(self) -> Any:
        """Remove and return the top element in the stack."""
        return self._elements.pop()

    def peek(self) -> Any:
        """Return the top element of the stack without removing it."""
        return self._elements[-1]

    def is_empty(self) -> bool:
        """Returns True is the stack is empty, else returns False."""
        return len(self._elements) == 0


class Queue:
    def __init__(self) -> None:
        """
        Initialise an instance of Queue.

        Attributes
        stack_in (Stack) - for enqueue operations
        stack_out (Stack) - for dequeue operations
        """
        self.stack_in = Stack()
        self.stack_out = Stack()

    def __len__(self) -> int:
        """Returns the total number of elements across both stacks."""
        return len(self.stack_in) + len(self.stack_out)

    def enqueue(self, element: Any) -> None:
        """Push an element onto stack_in."""
        self.stack_in.push(element)

    def dequeue(self) -> Any:
        """Pop an element from stack_out."""
        if self.is_empty():
            raise ValueError("Queue is empty")
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def is_empty(self):
        """Returns True if both stacks are empty, else returns False"""
        return self.stack_in.is_empty() and self.stack_out.is_empty()


try:
    print("-- create queue class --")
    q = Queue()
    print(f"Empty? {q.is_empty()}")

    print("-- enqueue items --")
    for item in range(1, 21):
        q.enqueue(item)

    print(f"Length: {len(q)}")
    print(f"Stack in: {q.stack_in}")
    print(f"Stack out: {q.stack_out}")

    print("-- dequeue items --")
    for item in range(1, 11):
        print(q.dequeue())
    print(f"Length: {len(q)}")
    print(f"Stack in: {q.stack_in}")
    print(f"Stack out: {q.stack_out}")

    print("-- enqueue more items --")
    for item in range(1, 5):
        q.enqueue(item)
    print(f"Length: {len(q)}")
    print(f"Stack in: {q.stack_in}")
    print(f"Stack out: {q.stack_out}")

    print(f"Peek: {q.peek()}")

    print(f"Dequeue: {q.dequeue()}")

    print(f"Peek: {q.peek()}")

    print("-- dequeue past the end of the queue --")
    for item in range(1, 21):
        q.dequeue()

except ValueError as e:
    print(e)
