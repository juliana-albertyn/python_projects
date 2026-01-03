# Project 3 (Intermediate–Advanced): Queue Using Two Stacks

### Goal
Implement a **Queue** using **two Stack objects**. This demonstrates how you can simulate FIFO behavior (queue) using LIFO structures (stacks).

---

### Requirements

1. **Stack class**  
   - Implement a simple stack with:
     - `push(element)`  
     - `pop()`  
     - `peek()`  
     - `is_empty()`  

2. **Queue class (using two stacks)**  
   - Maintain two stacks:
     - `stack_in` → for enqueue operations.  
     - `stack_out` → for dequeue operations.  

3. **Operations**
   - `enqueue(element)` → push onto `stack_in`.  
   - `dequeue()` →  
     - If `stack_out` is empty, move all elements from `stack_in` to `stack_out`.  
     - Then pop from `stack_out`.  
   - `peek()` →  
     - If `stack_out` is empty, move elements from `stack_in` to `stack_out`.  
     - Return the top of `stack_out`.  
   - `is_empty()` → return `True` if both stacks are empty.  
   - `__len__()` → return the total number of elements across both stacks.

4. **Complexity**
   - `enqueue` → O(1).  
   - `dequeue` → Amortized O(1).  
     - Occasionally O(n) when transferring elements, but overall average is O(1).  

5. **Demonstration**
   - Enqueue several items.  
   - Dequeue them one by one, showing FIFO order.  
   - Show that `peek()` works correctly.  
   - Verify `is_empty()` and `__len__()`.

---

### Why This Project Matters
- Reinforces the difference between **amortized complexity** and worst‑case complexity.  
- Shows how abstract data types can be layered on top of each other.  
- Builds intuition for designing efficient data structures.

---
*Project concept suggested by Microsoft Copilot.*