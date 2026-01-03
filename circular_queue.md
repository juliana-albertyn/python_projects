# Project 5: Circular Queue (using a fixed-size array)
This introduces modular arithmetic and buffer management, which are key concepts for efficient data structures.

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

## Internationalisation Exercise

### Goal  
Demonstrate how projects can adapt to different languages and regional formats using Python’s **`gettext`** (for translations) and **`locale`** (for formatting).

---

### Exercise Outline
1. **Add metadata strings for translation**  
   - Wrap user‑facing messages (like `"Queue is empty"`, `"Length"`, `"Peek"`) in `_()` so they can be translated.

   ```python
   import gettext
   _ = gettext.gettext

   if q.is_empty():
       print(_("Queue is empty"))
   ```

2. **Provide translations**  
   - Create `.po` files for at least two languages (e.g. English and Afrikaans).  
   - Translate key phrases like:
     - `"Queue is empty"` → `"Waglys is leeg"`  
     - `"Length"` → `"Lengte"`  
     - `"Peek"` → `"Kyk"`  

3. **Demonstrate locale formatting**  
   - Show currency or date formatting in South African English (`en_ZA`) vs another locale.  
   - Example:
     ```python
     import locale
     locale.setlocale(locale.LC_ALL, "en_ZA.UTF-8")
     print(locale.currency(1234.56))  # R1,234.56
     ```

4. **Run demo in two languages**  
   - Switch between English and Afrikaans translations.  
   - Show that the same queue operations print messages in different languages.

---

## Why This Matters
- Shows **regionally adapted software** — a key consulting skill.  
- Demonstrates awareness of **i18n/l10n best practices**.  
- Adds a unique dimension to your portfolio beyond pure data structures.

---
*Project concept suggested by Microsoft Copilot.*