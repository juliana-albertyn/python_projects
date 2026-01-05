# Project 7: Round‑Robin Task Scheduler

## Objective  
Simulate a **CPU scheduling algorithm** using a circular queue to manage tasks. Each task gets a fixed time slice before moving to the back of the queue.  

---

## Attributes  
- **`_queue`** → circular queue storing tasks waiting to be scheduled.  
- **`_time_slice`** → fixed amount of time each task is allowed to run.  
- **`_current_task`** → reference to the task currently being executed.  
- **`_completed_tasks`** → list of tasks that have finished execution.  

---

## Methods  
- **`add_task(task, burst_time)`**  
  Add a new task with its required execution time to the scheduler.  

- **`schedule()`**  
  Run the round‑robin loop: each task gets a time slice, then moves to the back of the queue if not finished.  

- **`execute_task(task)`**  
  Simulate execution of a task for one time slice, decrementing its remaining burst time.  

- **`is_empty()`**  
  Return `True` if no tasks remain in the queue.  

- **`__len__()`**  
  Return the number of tasks currently in the queue.  

- **`peek()`** *(optional)*  
  Look at the next task scheduled without removing it.  

- **`report()`**  
  Display a summary of completed tasks and their turnaround times.  

---

## Demo Block (Operations)  
1. Add several tasks with different burst times.  
2. Call `schedule()` to run the round‑robin simulation.  
3. Print reports showing task completion order and turnaround times.  

---
*Project concept suggested by Microsoft Copilot.*