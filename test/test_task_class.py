import unittest
from app.my_asyncio.task import Task


def simple_coroutine():
    """
        One simple coroutine
    """
    for _ in range(2):
        yield


class TestTask(unittest.TestCase):
    """
    Test cases for the Task class.
    """

    def setUp(self):
        """
        Set up a Task instance with a simple_coroutine.
        """
        self.coroutine = simple_coroutine()
        self.task = Task(self.coroutine)

    def test_task_creation(self):
        """
        Test the creation of a Task instance.
        """
        self.assertIsInstance(self.task, Task)
        self.assertEqual(self.task.tid, Task.taskid)
        self.assertEqual(self.task.coroutine, self.coroutine)
        self.assertIsNone(self.task.sendval)

    def test_invalid_coroutine(self):
        """
        Test creating a Task with an invalid coroutine.
        """
        with self.assertRaises(TypeError):
            _ = Task(None)

    def test_multiple_task_creation(self):
        """
        Test creating multiple Task instances with unique tids.
        """
        coroutine2 = simple_coroutine()
        task2 = Task(coroutine2)
        self.assertNotEqual(self.task.tid, task2.tid)

    def test_task_id_increment(self):
        """
        Test that the task ID increments correctly.
        """
        task1 = Task(simple_coroutine())
        task2 = Task(simple_coroutine())
        self.assertNotEqual(task1.tid, task2.tid)
