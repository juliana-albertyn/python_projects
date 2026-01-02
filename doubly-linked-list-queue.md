

## Project 4: Doubly Linked List Queue (or Circular Queue)

### Goal  
Implement a **Queue** using a **doubly linked list** (or alternatively, a circular queue). This builds on your linked list knowledge and introduces bidirectional pointers.

---

### Requirements

1. **Node class**  
   - Each node stores:
     - `element` (the data)  
     - `next` (pointer to the next node)  
     - `prev` (pointer to the previous node)  

2. **Queue class**  
   - Maintain `head` (front) and `tail` (back).  
   - Keep track of `length`.  

3. **Operations**  
   - `enqueue(element)` → add to the tail.  
   - `dequeue()` → remove from the head.  
   - `peek()` → return the head element without removing it.  
   - `is_empty()` → return `True` if length is 0.  
   - `__len__()` → return the number of elements.  

4. **Complexity**  
   - All operations should run in O(1).  

5. **Demonstration**  
   - Enqueue several items, peek, dequeue, and print results.  
   - Show that `prev` pointers are correctly maintained.  
   - Verify `is_empty()` and `__len__()`.

---

### Why This Project Matters
- Reinforces linked list concepts with **bidirectional navigation**.  
- Prepares you for more advanced structures like **deques** and **circular buffers**.  
- Shows how design choices (single vs double links) affect flexibility and efficiency.

---
