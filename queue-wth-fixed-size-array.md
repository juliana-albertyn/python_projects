## Project 5: Circular Queue (using a fixed-size array)
This one introduces modular arithmetic and buffer management, which are key concepts for efficient data structures.

---

## Goal  
Implement a **Queue** using a **fixed-size array** (list) with wrap‑around indexing, also known as a **circular buffer**.

---

## Requirements

### 1. Attributes
- `queue_items`: a list of fixed size (capacity).  
- `capacity`: maximum number of elements allowed.  
- `head`: index of the front element.  
- `tail`: index where the next element will be inserted.  
- `length`: current number of elements.

### 2. Operations
- `enqueue(element)`  
  - Add element at `tail`.  
  - Increment `tail` using modular arithmetic:  
    \[
    \text{tail} = (\text{tail} + 1) \mod \text{capacity}
    \]  
  - Raise `OverflowError` if the queue is full.

- `dequeue()`  
  - Remove element at `head`.  
  - Increment `head` using modular arithmetic.  
  - Raise `ValueError` if the queue is empty.

- `peek()`  
  - Return element at `head` without removing it.  
  - Raise `ValueError` if empty.

- `is_empty()` → `True` if `length == 0`.  
- `is_full()` → `True` if `length == capacity`.  
- `__len__()` → return `length`.

### 3. Complexity
- All operations run in **O(1)** time.  
- This is more efficient than a list‑based queue that uses `pop(0)` (which is O(n)).

---

## Demonstration
- Create a queue with capacity 5.  
- Enqueue 5 items, show that it’s full.  
- Dequeue 2 items, then enqueue 2 more — indices should wrap around.  
- Show that FIFO order is preserved.  
- Test `peek`, `is_empty`, and `is_full`.

---

## Why This Project Matters
- Teaches **modular arithmetic** in indexing.  
- Shows how to manage **fixed-size buffers** (common in systems programming, networking, and embedded devices).  
- Reinforces the idea that the same ADT (queue) can be implemented with different trade‑offs.

---
