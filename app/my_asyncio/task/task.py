from typing import Generator


class Task:
    """
    Class representing a task based on a coroutine.

    This class is used to create and manage tasks that encapsulate coroutines
    and allow controlled execution and communication.

    Example:
        >>> def simple_coroutine():
        ...    while True:
        ...        value = yield
        ...        print("Received value:", value)

        >>> task: Task = Task(simple_coroutine())
        >>> task.run()  # Start the execution of the coroutine
    """

    taskid: int = 0

    def __init__(self, coroutine: Generator[any, any, any]) -> None:
        """
        Initialize a new Task instance.

        Args:
            coroutine (generator): The coroutine to be associated with the task.
        """

        if not isinstance(coroutine, Generator):
            raise TypeError("coroutine must be a generator")

        Task.taskid += 1
        self.tid: int = Task.taskid
        self.coroutine: Generator[any, any, any] = coroutine
        self.sendval: any = None

    def run(self) -> any:
        """
        Execute the associated coroutine and send the specified value.

        Returns:
            Any: The value produced by the coroutine using 'yield'.
        """

        return self.coroutine.send(self.sendval)
