def coroutine_1() -> None:
    """
    Coroutine that prints a message and suspends with 'yield'.
    """

    while True:
        print("¡I am the Coroutine 1!")
        yield


def coroutine_2() -> None:
    """
    Coroutine that prints a message and suspends with 'yield'.
    """

    while True:
        print("¡I am the Coroutine 2!")
        yield


if __name__ == '__main__':
    # Importación de la clase Scheduler desde el módulo my_asyncio
    from app.my_asyncio import Scheduler

    # Creación de una instancia del planificador (Scheduler)
    sched = Scheduler()

    # Creación de dos tareas utilizando las corrutinas
    sched.create_task(task=coroutine_1())
    sched.create_task(task=coroutine_2())

    # Inicio del bucle de eventos del planificador
    sched.run_event_loop()
