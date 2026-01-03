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
import gettext
import language_constants as lc

lang = gettext.translation("messages", localedir="locales", languages=["en_ZA"])
# lang = gettext.translation("messages", localedir="locales", languages=["af_ZA"])
# lang = gettext.translation("messages", localedir="locales", languages=["zu_ZU"])
# lang = gettext.translation("messages", localedir="locales", languages=["es_ES"])
# lang = gettext.translation("messages", localedir="locales", languages=["pt_PT"])
# lang = gettext.translation("messages", localedir="locales", languages=["fr_FR"])
lang.install()
_ = lang.gettext


class Queue:
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

    def enqueue(self, item: Any, priority: int) -> None:
        """Add item with given priority to queue. Highest priority = largest number"""
        heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        print(f"{_(lc.QUEUE_ENQUEUE)} {item}")

    def dequeue(self) -> Any:
        """Remove and return item with the highest priority."""
        if len(self) == 0:
            raise ValueError(_(lc.ERROR_UNDERFLOW))
        priority, index, item = heappop(self._queue)
        print(f"{_(lc.QUEUE_DEQUEUE)} {item}")
        return item

    def is_empty(self) -> bool:
        """Returns True if there are no items in the queue, else returns False."""
        return len(self) == 0

    def peek(self) -> Any:
        """Look at the next item to dequeue without removing it."""
        priority, index, item = self._queue[0]
        return item


q = Queue()
q.enqueue("Low priority task", priority=1)
q.enqueue("High priority task", priority=5)
q.enqueue("Medium priority task", priority=3)
print(f"{_(lc.QUEUE_PEEK)} {q.peek()}")
while not q.is_empty():
    q.dequeue()
if q.is_empty():
    print(f"{_(lc.QUEUE_IS_EMPTY)}")
else:
    print(f"{_(lc.QUEUE_LENGTH)} {len(q)}")
