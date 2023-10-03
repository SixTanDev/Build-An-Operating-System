import unittest
from app.my_asyncio import Scheduler
from app.my_asyncio.task import Task


def simple_coroutine():
    yield
    yield


def simple_coroutine_1():
    yield


def simple_coroutine_2():
    yield


class TestScheduler(unittest.TestCase):

    def setUp(self):
        """
        Set up a Scheduler instance.
        """
        self.scheduler = Scheduler()

    def test_scheduler_creation(self):
        """
        Test the creation of a Scheduler instance.
        """
        self.assertIsInstance(self.scheduler, Scheduler)

    def test_create_task(self):
        """
        Test creating and adding tasks to the scheduler.
        """
        task_id = self.scheduler.create_task(simple_coroutine())
        self.assertTrue(task_id in self.scheduler.taskmap)

    def test_schedule_task(self):
        """
        Test scheduling a task for execution.
        """
        task = Task(simple_coroutine())
        self.scheduler.schedule(task)
        scheduled_task = self.scheduler.ready.get()
        self.assertEqual(scheduled_task, task)

    def test_run_event_loop(self):
        """
        Test running the event loop of the scheduler.
        """

        def simple_coroutine_with_value():
            value = yield
            self.assertEqual(value, "TestValue")

        task = Task(simple_coroutine_with_value())
        task.sendval = "TestValue"
        self.scheduler.schedule(task)
        self.scheduler.run_event_loop()
        self.assertFalse(self.scheduler.taskmap)

    def test_stop_iteration_handling(self):
        """
        Test handling of StopIteration when a task is completed.
        """

        def simple_coroutine():
            yield
            raise StopIteration("Task Completed")

        task = Task(simple_coroutine())
        self.scheduler.schedule(task)
        self.scheduler.run_event_loop()
        self.assertFalse(self.scheduler.taskmap)
