# Task 1
from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
