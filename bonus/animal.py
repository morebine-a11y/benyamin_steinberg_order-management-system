from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, legs: int):
        if not isinstance(legs, int) or legs < 0:
            raise ValueError("legs must be a non-negative integer")
        self._legs = legs

    def walk(self):
        print(f"This animal walks on {self._legs} legs.")

    @abstractmethod
    def eat(self):
        pass