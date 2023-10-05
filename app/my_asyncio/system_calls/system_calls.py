# pylint: disable=W0107,E1101

from __future__ import annotations
from abc import ABC, abstractmethod


class SystemCallsInterface(ABC):
    """
    Abstract base class for system call interfaces.
    """

    @abstractmethod
    def handler(self):
        """
        Abstract method to handle the system call.
        """

        pass


class GetTid(SystemCallsInterface):
    """
    System call to get the task ID.
    """

    def handler(self):
        """
        Handle the GetTid system call.

        Set the sendval of the task to the task's ID and schedule the task.
        """

        self.task.sendval: int = self.task.tid
        self.sched.schedule(task=self.task)
