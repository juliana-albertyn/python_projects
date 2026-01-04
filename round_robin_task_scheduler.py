"""
Module: round_robin_task_scheduler
Purpose: Simulates a CPU scheduling algorithm using a circular queue to manage tasks.
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-03"

from typing import Any
from circular_queue import CircularQueue
import language_constants as lc
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


class TaskScheduler(CircularQueue):
    """
    A circular queue to manage tasks.

    Attributes:
    _capacity (int) : the maximum number of elements allowed
    _time_slice (int) : fixed amount of time each task is allowed to run
    _current_task (Any) : task currently being executed
    _completed_tasks (list[tuple[Any, int, int]]) : list of tasks that have been completed
    """

    def __init__(self, capacity: int, time_slice: int) -> None:
        """Initialises an instance of TaskScheduler."""
        super().__init__(capacity)
        self._time_slice = time_slice
        self._current_task = None
        self._completed_tasks: list[Any] = []

    def add_task(self, task: Any, burst_time: int) -> None:
        """Add a new task with its required execution time to the scheduler."""
        if (task is None) or (burst_time <= 0):
            raise ValueError(_(lc.TASK_INVALID))
        time_remaining = burst_time
        self.enqueue((task, burst_time, time_remaining))

    def execute_task(self, task):
        """Simulate execution of a task for one time slice."""
        self._current_task = task
        if __debug__:
            print(f"{_(lc.EXECUTING)} {self._current_task}")

    def schedule(self):
        """Run the round-robin loop, with each task getting a time slice."""
        if self._length == 0:
            raise ValueError(_(lc.QUEUE_IS_EMPTY))
        while not self.is_empty():
            task, burst_time, time_remaining = self.dequeue()
            slice = self._time_slice
            while slice > 0 and time_remaining > 0:
                self.execute_task(task)
                slice -= 1
                time_remaining -= 1
                if time_remaining == 0:
                    break  # else the loop is repeated more times than necessary
            if time_remaining > 0:
                self.enqueue((task, burst_time, time_remaining))
            else:
                self._completed_tasks.append((task, burst_time))

    def report(self):
        """A summary of the completed tasks in order of completion,
        and their turnaround times."""
        print(f"\n{_(lc.TASKS_COMPLETED)}: ({len(self._completed_tasks)})")
        for index, (task, burst_time) in enumerate(self._completed_tasks):
            print(f"{index+1}. {task} ({burst_time})")


if __name__ == "__main__":
    try:
        schedule = TaskScheduler(6, 2)
        schedule.add_task("Task A", 11)
        schedule.add_task("Task B", 5)
        schedule.add_task("Task C", 2)
        schedule.add_task("Task D", 7)
        schedule.add_task("Task E", 3)
        schedule.schedule()
        schedule.report()
    except ValueError as e:
        print(e)
    except OverflowError as e:
        print(e)
