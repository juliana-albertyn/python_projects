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
    capacity (int) : the maximum number of elements allowed.
    head (int) : the index of the front element.
    tail (int) : the index where the next element will be inserted.
    length (int) : the number of elements.
    """

    def __init__(self, capacity: int) -> None:
        """Initialise an instance of Queue."""
        self._queue_items: list[Any] = [None] * capacity
        self._capacity = capacity
        self._head = 0
        self._tail = 0
        self._length = 0

    def __len__(self) -> int:
        """Returns the number of items currently in the list."""
        return self._length

    def enqueue(self, element: Any) -> None:
        """Add an element at the tail."""
        if len(self) == self._capacity:
            raise OverflowError("Queue is full")
        self._queue_items[self._tail] = element
        self._tail = (self._tail + 1) % self._capacity
        self._length += 1

    def dequeue(self) -> Any:
        """Remove the element at the head."""
        if self._length == 0:
            raise ValueError("Queue is empty")
        item = self._queue_items[self._head]
        self._queue_items[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._length -= 1
        return item

    def peek(self) -> Any:
        """Return the element at the head without removing it."""
        if self._length == 0:
            raise ValueError("Queue is empty")
        return self._queue_items[self._head]

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False if it contains elements."""
        return self._length == 0

    def is_full(self) -> bool:
        """Returns True if the list is filled to capacity, else returns False."""
        return self._length == self._capacity


# create and check empty
q = Queue(5)
print(f"Empty?: {q.is_empty()}")
# enqueue to capacity
try:
    for item in range(101, 106):
        q.enqueue(item)
        print(
            f"Enqueue: {item} Count: {len(q)} Head: {q._head} Tail: {q._tail} Queue: {q._queue_items}"
        )
except ValueError as e:
    print(e)
except RuntimeError as e:
    print(e)
print(f"Full?: {q.is_full()}")
# trying to go over capacity
try:
    for item in range(106, 108):
        q.enqueue(item)
        print(
            f"Enqueue: {item} Count: {len(q)} Head: {q._head} Tail: {q._tail} Queue: {q._queue_items}"
        )
except ValueError as e:
    print(e)
except RuntimeError as e:
    print(e)
except OverflowError as e:
    print(e)

try:
    # dequeue 3
    for i in range(0, 3):
        print(
            f"Dequeue: {q.dequeue()} Count: {len(q)} Head: {q._head} Tail: {q._tail} Queue: {q._queue_items}"
        )
    # enqueue 2
    for item in range(201, 203):
        q.enqueue(item)
        print(
            f"Enqueue: {item} Count: {len(q)} Head: {q._head} Tail: {q._tail} Queue: {q._queue_items}"
        )
    print(f"Full?: {q.is_full()}")
    print(f"Empty?: {q.is_empty()}")

except ValueError as e:
    print(e)
except RuntimeError as e:
    print(e)
