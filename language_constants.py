"""
Module: language_constants
Purpose: Centralised message strings for units in python_projects.
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-03"

import gettext

_ = gettext.gettext

## General ##
EXECUTING = "Executing"

## Queues ##

# Queue descriptions for debugging
QUEUE = "Queue"
COUNT = "Count"  # used in demo output
HEAD = "Head"
TAIL = "Tail"

# Queue status messages
EMPTY_QUERY = "Empty?"
FULL_QUERY = "Full?"
QUEUE_IS_EMPTY = "Queue is empty"
QUEUE_IS_FULL = "Queue is full"

# Queue operations
QUEUE_LENGTH = "Length"  # used in API/peek messagges
QUEUE_PEEK = "Peek"
QUEUE_ENQUEUE = "Enqueue"
QUEUE_DEQUEUE = "Dequeue"

# Queue error messages
ERROR_OVERFLOW = "Cannot enqueue: queue is full"
ERROR_UNDERFLOW = "Cannot dequeue: queue is empty"

## Task scheduler ##
TASK_INVALID = "Task and time allocated must be supplied"
TASKS_COMPLETED = "Tasks completed"
