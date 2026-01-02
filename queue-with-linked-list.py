""" "
Project 2 (Intermediate Level): Queue Using a Linked List

Implement a queue using a linked list
"""
__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-02"

from typing import Any, Optional


class Node:
    """
    This class contains an element, and a pointer to the next element in the queue.

    Attributes:
    next (int) : Pointer to the next node in the list.
    """

    def __init__(self, element: Any) -> None:
        """Creates an instance of the Node class, and
        sets the element

        Args:
        element (None | None): Pointer to the element contained in the node.
        """
        self._element = element
        self._next: Optional["Node"] = None

    def __str__(self) -> str:
        """Returns a str representation of the element."""
        return str(self._element)

    @property
    def next(self) -> Optional["Node"]:
        """Getter for the _next attribute"""
        return self._next

    @next.setter
    def next(self, node: Optional["Node"]) -> None:
        """Setter for the _next attribute"""
        self._next = node

    @property
    def element(self) -> Any:
        """Getter for the element attribute"""
        return self._element

    @element.setter
    def element(self, element: Any) -> None:
        """Setter for the element attribute"""
        self._element = element


class Queue:
    """A singly linked list of elements"""

    def __init__(self) -> None:
        """
        Creates an instance of Queue

        Attributes
        head (Node | None): The first node in the queue
        tail (Node | None): The last node in the queue
        length (int): The number of items in the queue
        """
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0

    def __len__(self) -> int:
        """Returns the number of items in the queue"""
        return self.length

    def enqueue(self, element) -> None:  # O(1)
        """Adds a node containing the element to the back of the queue"""
        node = Node(element)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            self.length += 1
            return
        if self.tail is None:
            raise RuntimeError("Tail should never be None here")
        self.tail.next = node
        self.tail = node
        self.length += 1

    def dequeue(self) -> Any:  # O(1)
        """Removes a node containing the element from the front of the queue, and returns the element"""
        if self.head is None:
            raise ValueError("The queue is empty")
        head_node = self.head
        self.head = head_node.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return head_node.element

    def peek(self) -> Any:  # O(1)
        """Returns the element from the front of the queue"""
        if self.head is None:
            raise ValueError("The queue is empty")
        return self.head.element

    def is_empty(self) -> bool:  # O(1)
        """Returns True if the queue is empty, else returns false"""
        return self.length == 0


q = Queue()
q.enqueue("apple")
print(f"Length {len(q)}")
q.enqueue("banana")
print(f"Length {len(q)}")
q.enqueue("cherry")
print(f"Length {len(q)}")
print(f"Peeked {q.peek()}")
print(f"Length {len(q)}")
print(f"Removed {q.dequeue()}")
print(f"Length {len(q)}")
print(f"Peeked {q.peek()}")
print(f"Queue is empty {q.is_empty()}")
