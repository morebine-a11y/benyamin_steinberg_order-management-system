from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def setName(self, name: str):
        pass

    @abstractmethod
    def play(self):
        pass