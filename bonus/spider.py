from animal import Animal


class Spider(Animal):
    def __init__(self):
        super().__init__(8)

    def eat(self):
        print("The spider eats a fly.")