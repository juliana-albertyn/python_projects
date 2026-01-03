"""
Module: queue-with-fixed-size-array
Purpose: Implement a circular queue
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-02"

from typing import Any
import gettext
import language_constants as lc

#lang = gettext.translation("messages", localedir="locales", languages=["af_ZA"])
lang = gettext.translation("messages", localedir="locales", languages=["en_ZA"])
lang.install()
_ = lang.gettext


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
        """Returns the number of items currently in the queue."""
        return self._length

    def __str__(self) -> str:
        """Returns a string representation of the queue for debugging purposes."""
        return f"{_(lc.COUNT)}: {len(q)} {_(lc.HEAD)}: {q._head} {_(lc.TAIL)}: {q._tail} {_(lc.QUEUE)}: {q._queue_items}"

    def enqueue(self, element: Any) -> None:
        """Add an element at the tail."""
        if len(self) == self._capacity:
            raise OverflowError(_(lc.ERROR_OVERFLOW))
        self._queue_items[self._tail] = element
        self._tail = (self._tail + 1) % self._capacity
        self._length += 1

    def dequeue(self) -> Any:
        """Remove the element at the head."""
        if self._length == 0:
            raise ValueError(_(lc.ERROR_UNDERFLOW))
        item = self._queue_items[self._head]
        self._queue_items[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._length -= 1
        return item

    def peek(self) -> Any:
        """Return the element at the head without removing it."""
        if self._length == 0:
            raise ValueError(_(lc.QUEUE_IS_EMPTY))
        return self._queue_items[self._head]

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False if it contains elements."""
        return self._length == 0

    def is_full(self) -> bool:
        """Returns True if the list is filled to capacity, else returns False."""
        return self._length == self._capacity


# create and check empty
q = Queue(5)
print(f"{_(lc.EMPTY_QUERY)}: {q.is_empty()}")
# enqueue to capacity
try:
    for item in range(101, 106):
        q.enqueue(item)
        print(f"{_(lc.QUEUE_ENQUEUE)}: {item} {q}")
except ValueError as e:
    print(e)
print(f"{_(lc.FULL_QUERY)}: {q.is_full()}")
# trying to go over capacity
try:
    for item in range(106, 108):
        q.enqueue(item)
        print(f"{_(lc.QUEUE_ENQUEUE)}: {item} {q}")
except ValueError as e:
    print(e)
except OverflowError as e:
    print(e)

try:
    # dequeue 3
    for i in range(0, 3):
        print(f"{_(lc.QUEUE_DEQUEUE)}: {q.dequeue()} {q}")
    # enqueue 2
    for item in range(201, 203):
        q.enqueue(item)
        print(f"{_(lc.QUEUE_ENQUEUE)}: {item} {q}")
    print(f"{_(lc.FULL_QUERY)}: {q.is_full()}")
    print(f"{_(lc.EMPTY_QUERY)}: {q.is_empty()}")

except ValueError as e:
    print(e)
