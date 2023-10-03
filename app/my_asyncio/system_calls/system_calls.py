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
