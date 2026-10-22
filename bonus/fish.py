from animal import Animal
from pet import Pet


class Fish(Animal, Pet):
    def __init__(self):
        super().__init__(0)
        self._name = None
        self.setName("Nemo")

    def getName(self) -> str:
        return self._name

    def setName(self, name: str):
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("name must be a non-empty string")
        self._name = name

    def play(self):
        print(f"{self._name} swims in circles.")

    def walk(self):
        super().walk()
        print("Just kidding! Fish can't walk.")

    def eat(self):
        print("The fish eats plankton.")