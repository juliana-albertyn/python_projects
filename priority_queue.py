"""
Module: priority_queue
Purpose: Implement a priority queue where each item has a priority value
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-03"

from typing import Any, List, Tuple
from heapq import heappush, heappop
import language_constants as lc
from enum import IntEnum
from translation import translator, available_languages, LocaleError


class Priorities(IntEnum):
    LOW_PRIORITY = 1
    MEDIUM_PRIORITY = 3
    HIGH_PRIORITY = 5


class PriorityQueue:
    """
    A priority queue

    Attributes:
    _queue (list[tuple[int, int, Any]) : an internal list storing queue items
    _index (int) : counter to preserve insertion order when priorities are equal
    """

    def __init__(self) -> None:
        """Initialises an instance of Queue."""
        self._queue: list[tuple[int, int, Any]] = []
        self._index: int = 0

    def __len__(self) -> int:
        "Returns the number of items in the queue"
        return len(self._queue)

    def __str__(self):
        """Returns a string representation of the items in the queue"""
        return f"{self._queue}"

    def __iter__(self):
        """Makes the class iterable, sorted by priority."""
        sorted_by_priority = sorted(self._queue)
        return iter(item for _, _, item in sorted_by_priority)

    def enqueue(self, item: Any, priority: Priorities) -> None:
        """Add item with given priority to queue. Highest priority = largest number"""
        heappush(self._queue, (-priority.value, self._index, item))
        self._index += 1

    def dequeue(self) -> Any:
        """Remove and return item with the highest priority."""
        if len(self) == 0:
            raise ValueError(translator._(lc.ERROR_UNDERFLOW))
        _, _, item = heappop(self._queue)
        return item

    def is_empty(self) -> bool:
        """Returns True if there are no items in the queue, else returns False."""
        return len(self) == 0

    def peek(self) -> Any:
        """Look at the next item to dequeue without removing it."""
        _, _, item = self._queue[0]
        return item


if __name__ == "__main__":
    q = PriorityQueue()
    for language in available_languages:
        translator.set_locale(language)
        q.enqueue("Low priority task", Priorities.LOW_PRIORITY)
        q.enqueue("High priority task", Priorities.HIGH_PRIORITY)
        q.enqueue("Medium priority task", Priorities.MEDIUM_PRIORITY)
        print(f"{translator._(lc.QUEUE_PEEK)} {q.peek()}")
        while not q.is_empty():
            q.dequeue()
            print(f"{translator._(lc.QUEUE_LENGTH)} {len(q)}")
        if q.is_empty():
            print(f"{translator._(lc.QUEUE_IS_EMPTY)}")
        print(f"{'_' * 20}")
    try:
        invalid_code = "du-MY"
        translator.set_locale(invalid_code)
    except Exception as e:
        print(f"{e}")
