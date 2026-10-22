from animal import Animal
from pet import Pet


class Cat(Animal, Pet):
    def __init__(self, name: str = "Fluffy"):
        super().__init__(4)
        self._name = None
        self.setName(name)

    def getName(self) -> str:
        return self._name

    def setName(self, name: str):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string")
        self._name = name

    def play(self):
        print(f"{self._name} plays with a ball of yarn.")

    def eat(self):
        print("The cat eats tuna.")