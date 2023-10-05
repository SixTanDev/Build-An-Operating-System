# pylint: disable=R0801
from time import sleep


def coroutine_1() -> None:
    """
        Coroutine that prints a message and suspends with 'yield'.
    """

    while True:
        sleep(2)
        print("¡I am the Coroutine 1!")
        yield


def coroutine_2():
    """
        Coroutine that prints a message and suspends with 'yield'.
    """

    for _ in range(3):
        print("¡I am the Coroutine 2!")
        yield


if __name__ == '__main__':
    from app.my_asyncio import Scheduler

    # Create an instance of the Scheduler
    sched = Scheduler()

    # Create tasks using the coroutines
    # This coroutine is an infinite loop without yielding,
    # which might lead to a StopIteration error.
    sched.create_task(task=coroutine_1())

    # This coroutine runs a finite number of times, so it won't face a StopIteration error.
    sched.create_task(task=coroutine_2())

    # Start the event loop of the scheduler
    sched.run_event_loop()
