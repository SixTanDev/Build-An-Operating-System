def coroutine() -> None:
    """
    Coroutine that prints messages and suspends with 'yield'.
    """

    print("Our first Coroutine wrapped in a task 1")
    yield
    print("Our first Coroutine wrapped in a task 1")
    yield


if __name__ == '__main__':
    # Importing the Task class from the my_asyncio module
    from app.my_asyncio.task import Task

    # Create our first task
    task_1 = Task(coroutine=coroutine())

    # Running the coroutine within the task
    print("Running task 1:")
    task_1.run()
    task_1.run()
