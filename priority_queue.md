# Project 6: Priority Queue (Heap-based)

## 🎯 Objective
Implement a **priority queue** where each item has a priority value. Instead of FIFO order, items are dequeued based on their priority (highest first). This extends your queue knowledge into a more advanced and widely used structure.

---

## Attributes
- **`_queue`** → internal list (heap) storing tuples `(priority, index, item)`.  
- **`_index`** → counter to preserve insertion order when priorities are equal.  

---

## Methods
- **`enqueue(item, priority)`**  
  Add an item with a given priority into the queue.  
  - Uses `heapq.heappush`.  
  - Invert priority (`-priority`) for max‑heap behaviour.  

- **`dequeue()`**  
  Remove and return the item with the highest priority.  
  - Uses `heapq.heappop`.  
  - If empty, return error message.  

- **`is_empty()`**  
  Return `True` if no items are in the queue.  

- **`__len__()`**  
  Return the number of items currently in the queue.  

- *(Optional)* **`peek()`**  
  Look at the next item to be dequeued without removing it.  

---

## Demo Block
Sequence of operations to test the priority queue:

1. `enqueue("Low priority task", priority=1)`  
2. `enqueue("High priority task", priority=5)`  
3. `enqueue("Medium priority task", priority=3)`  
4. Loop: while not `is_empty()`, call `dequeue()`  

---

## Expected Output (English)
```
Enqueue Low priority task
Enqueue High priority task
Enqueue Medium priority task
Dequeue High priority task
Dequeue Medium priority task
Dequeue Low priority task
```

---

## Extensions
- Add **stable ordering** for equal priorities.  
- Implement **peek()**.  

---
*Project concept suggested by Microsoft Copilot.*