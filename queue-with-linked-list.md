## Project 2 (Intermediate Level): **Queue Using a Linked List**

### Requirements
1. **Node class**  
   - Each node should store:
     - `element` (the data)
     - `next` (pointer to the next node)

2. **Queue class**  
   - Maintain two pointers:
     - `head` → the front of the queue  
     - `tail` → the back of the queue  
   - Keep track of `length` (number of elements).

3. **Methods to implement**
   - `enqueue(element)` → add to the tail.  
   - `dequeue()` → remove from the head.  
   - `peek()` → return the head element without removing it.  
   - `is_empty()` → return `True` if length is 0.  
   - `__len__()` → return the number of elements.

4. **Complexity**
   - All operations should run in **O(1)** time because you’re maintaining both `head` and `tail`.

5. **Demonstration**
   - Enqueue a few items, peek at the front, dequeue them one by one, and print results.  
   - Show that `is_empty()` and `__len__()` behave correctly.

---

### Why This Project Matters
- Reinforces linked list traversal and pointer manipulation.  
- Shows how abstract data types (queue) can be implemented differently depending on the underlying structure.  
- Demonstrates how design choices affect time complexity.
  
---
*Project concept suggested by Microsoft Copilot.*