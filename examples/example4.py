from app.my_asyncio import Scheduler
from app.my_asyncio.system_calls import GetTid


def coroutine_1() -> None:
    """
    Coroutine that prints messages and suspends with 'yield'.

    Yields:
        SystemCall: A GetTid call to retrieve the task identifier.
    """
    my_tid: int = yield GetTid()
    for _ in range(5):
        print(f"I'm coroutine with id: {my_tid}")
        yield


def main() -> None:
    """
    Main coroutine that creates a new task, waits for it to finish, and then prints a message.

    Yields:
        SystemCall: A NewTask call to launch a new task.
        SystemCall: A WaitTask call to wait for the child task to finish.
    """
    mytid = yield GetTid()
    for _ in range(10):
        print(f"I'm main  with id: {mytid}")
        yield


if __name__ == '__main__':
    # Create an instance of the scheduler
    sched = Scheduler()

    # Create the main and coroutine task and add it to the scheduler
    sched.create_task(task=main())
    sched.create_task(task=coroutine_1())

    # Start the scheduler's event loop
    sched.run_event_loop()
