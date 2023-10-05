# pylint: disable=R0801
def coroutine_1() -> None:
    """
        Coroutine that prints a message and suspends with 'yield'.
    """
    for _ in range(3):
        print("¡I am the Coroutine 1!")
        yield


def coroutine_2() -> None:
    """
        Coroutine that prints a message and suspends with 'yield'.
    """
    for _ in range(5):
        print("¡I am the Coroutine 2!")
        yield


if __name__ == '__main__':
    from app.my_asyncio import Scheduler

    # Create an instance of the Scheduler
    sched = Scheduler()

    # Create tasks using the coroutines
    # This coroutine runs a finite number of times, so it won't raice a StopIteration error.
    sched.create_task(task=coroutine_1())

    # This coroutine runs a finite number of times, so it won't raice a StopIteration error.
    sched.create_task(task=coroutine_2())

    # Start the event loop of the scheduler
    sched.run_event_loop()
