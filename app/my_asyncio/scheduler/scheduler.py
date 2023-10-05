from __future__ import annotations
from typing import Generator
from queue import Queue
from app.my_asyncio.task import Task
from app.my_asyncio.system_calls import SystemCallsInterface


class Scheduler:
    """
    A simple coroutine-based scheduler.

    This class provides functionality to create and schedule Task

    Example:
        >>> def simple_coroutine():
        ...    while True:
        ...        value = yield
        ...        print("Received value:", value)

        >>> sched: Scheduler = Scheduler()
        >>> sched.create_task(task=simple_coroutine())
        >>> sched.run_event_loop()

    """

    def __init__(self) -> None:
        """
        Initialize a new instance of the Scheduler class.
        """

        self.ready: Queue = Queue()
        self.taskmap: dict = {}

    def schedule(self, task: Task) -> None:
        """
        Schedule a task for execution.

        Args:
            task (Task): The task to be scheduled for execution.
        """

        self.ready.put(task)

    def create_task(self, task: Generator[any, any, any]) -> int:
        """
        Create a new task and add it to the scheduler.

        Args:
            task (Generator[any, any, any]): The generator representing the task's coroutine.

        Returns:
            int: The unique task identifier assigned to the created task.
        """

        new_task: Task = Task(coroutine=task)
        self.taskmap[new_task.tid]: Task = new_task
        self.schedule(new_task)
        return new_task.tid

    def exit(self, task: Task) -> None:
        """
        Handle the exit of a task.

        Args:
            task (Task): The task that has completed and is exiting.
        """

        print(f"Task {task.tid} completed")
        del self.taskmap[task.tid]

    def run_event_loop(self) -> None:
        """
        Main event loop for the scheduler.

        This loop iterates through the tasks in the scheduler and runs them one by one.
        """

        while self.taskmap:
            task: Task = self.ready.get()
            try:
                result: SystemCallsInterface | any = task.run()
                if isinstance(result, SystemCallsInterface):
                    result.task: Task = task
                    result.sched: Scheduler = self
                    result.handler()
                    continue
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)
