from abc import ABC, abstractmethod
from collections.abc import Callable


class Calculation(ABC):
    def __init__(self, a: float, b: float,
                 operation: Callable[[float, float], float]):
        self.a = a
        self.b = b
        self.operation = operation

    @classmethod
    def create(cls, a, b, operation):
        # Class method creates a concrete calculation.
        return cls(a, b, operation)

    @abstractmethod
    def execute(self) -> float:  # pragma: no cover
        # Abstract method requires implementation.
        pass


class ArithmeticCalculation(Calculation):
    def execute(self) -> float:
        # Instance method uses stored values.
        return self.operation(self.a, self.b)
