"""
Module: multilingual_to_do_list_manager
Purpose: A to-do list manager, based on a priority queue, that supports multiple languages
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-04"

from typing import Any, Optional, cast
from enum import IntEnum
import time
from datetime import date, datetime, timezone
import priority_queue as queue
import language_constants as lc
import gettext
from pathlib import Path
from translation import translator, available_languages

counter: int = 0


class ToDoList(queue.PriorityQueue):
    """
    A multilingual to-do list manager.

    Attributes:
    _list_name (str) : A description for this ToDoList
    _locale (str) : current language setting for display
    _completed (list[str]) : list of completed tasks id's
    """

    class Task:
        """A task to add to a to-do list.

        Attributes
        _task_id (str) : An unique ID for task
        _description (str) : a description of task
        _created_at (datetime) : datetime on which the task was created
        _priority (Priorities) : high/medium/low priority
        _date_completed (datetime) : datetime on which the task was marked as completed
        """

        def __init__(
            self,
            description: str,
            priority: queue.Priorities = queue.Priorities.MEDIUM_PRIORITY,
        ) -> None:
            """Initialises an instance of Task"""
            if not description.strip():
                raise ValueError(f"{lc.DESCRIPTION_EMPTY}")
            # use global counter so that tasks created at the same time have different IDs
            global counter
            self._task_id = f"TASK-{int(time.time())}-{counter}"
            counter += 1
            self._created_at = datetime.now(timezone.utc)
            self._description = description
            self._priority = priority
            self._date_completed: Optional[datetime] = None

        def __str__(self) -> str:
            """Returns a string representation of a Task."""

            if self._date_completed:
                completed_local = self._date_completed.astimezone().strftime("%d %B %Y")
                result = f"{self._description} ({translator._(lc.TASK_COMPLETED)} {completed_local})"
            else:
                priority_str = self.priority_value_as_str(self._priority)
                result = f"{self._description} ({translator._(lc.PRIORITY)}: {priority_str})"
            return result
            
        def __repr__(self) -> str:
            """Returns a string representation of a Task for debugging and inspection."""
            created_local = self._created_at.astimezone().strftime("%d %B %Y")
            result = f"{self._task_id} {created_local}"
            if self._date_completed:
                completed_local = self._date_completed.astimezone().strftime("%d %B %Y")
                result += f"{self._description} ({translator._(lc.TASK_COMPLETED)} {completed_local}"
            else:
                priority_str = self.priority_value_as_str(self._priority)
                result += f"{self._description} ({translator._(lc.PRIORITY)}: {priority_str}"
            return result

        def priority_value_as_str(self, priority: queue.Priorities) -> str:
            """Return the translated str value of the Priority passed in"""
            match priority:
                case queue.Priorities.LOW_PRIORITY:
                    return f"{translator._(lc.LOW)}"
                case queue.Priorities.MEDIUM_PRIORITY:
                    return f"{translator._(lc.MEDIUM)}"
                case queue.Priorities.HIGH_PRIORITY:
                    return f"{translator._(lc.HIGH)}"

        def complete(self) -> None:
            """Mark a task as completed."""
            self._date_completed = datetime.now(timezone.utc)

    def __init__(self, list_name: str) -> None:
        """Initialises an instance of ToDoList."""
        super().__init__()
        self._list_name = list_name
        self._completed: list[ToDoList.Task] = []
        self._locale = translator._language_code

    def enqueue(self, item: Any, priority: queue.Priorities) -> None:
        """Add task to priority queue"""
        super().enqueue(item, priority)

    def dequeue(self) -> Task:
        """Remove the first task, based on priority, from the queue and return it."""
        try:
            return super().dequeue()
        except ValueError:  # underflow error
            raise

    def add_task(
        self,
        description: str,
        priority: queue.Priorities = queue.Priorities.MEDIUM_PRIORITY,
    ) -> None:
        """Add a task to the priority queue."""
        task = ToDoList.Task(description, priority)
        self.enqueue(task, priority)

    def next_task(self) -> Optional[Task]:
        """Show the next task on the todo list"""
        if len(self) > 0:
            return super().peek()
        else:
            return None

    def complete_task(self) -> None:
        """Mark a task as completed, and add it to the completed list."""
        try:
            task = self.dequeue()
            if task:
                task.complete()
                self._completed.append(task)
        except ValueError as e:
            raise (e)

    def list_tasks(self, todo: bool = True) -> str:
        """Return a string representation of the tasks in priority sequence.

        Arguments
        todo (bool): If True, lists all the tasks to do, else lists all
        the completed tasks
        """
        result = ""
        if todo:
            if len(self._queue) > 0:
                result = f"{'*' * 5} {self._list_name} {'*' * 5}\n"
                for index, task in enumerate(self):
                    result += f"{index+1}. {task}\n"
        else:
            if len(self._completed) > 0:
                result += f"{'*' * 5} {self._list_name} - {translator._(lc.TASK_COMPLETED)} {'*' * 5}\n"
                for index, task in enumerate(self._completed):
                    result += f"{index+1}. {task}\n"
        return result

    def status(self) -> str:
        """Returns a string, giving the number of tasks todo and tasks completed"""
        return f"{self._list_name}: {len(self)} {translator._(lc.TASK_TODO)}, {len(self._completed)} {translator._(lc.TASK_COMPLETED)}"


if __name__ == "__main__":

    # create instance
    todo = ToDoList("My python learning roadmap")
    # add 5 tasks of different priority in any sequenece
    todo.add_task("Testing & automation", queue.Priorities.LOW_PRIORITY)
    todo.add_task("File handling")
    todo.add_task("Core language & data structures", queue.Priorities.HIGH_PRIORITY)
    todo.add_task("Internationalisation (i18n)", queue.Priorities.MEDIUM_PRIORITY)
    todo.add_task("Exceptions & exception handling", queue.Priorities.HIGH_PRIORITY)

    # show current status
    print(f"\n{todo.status()}")

    # cycle through available languages
    for language_code in available_languages:
        print(f"\n{'=' * 10} {language_code} {'-' * 10}")
        translator.set_locale(language_code)

        print(f"{todo.list_tasks()}")

        # complete a task
        if len(todo) > 0:
            try:
                print(f"✅ {todo.next_task()}")
                todo.complete_task()
            except ValueError as e:
                print(f"{e}")
        else:
            print(f"{todo.status()}")

        # list the tasks to do
        print(f"{todo.list_tasks()}")

        # list the completed tasks
        print(f"{todo.list_tasks(False)}")
