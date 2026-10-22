from animal import Animal
from pet import Pet
from spider import Spider
from cat import Cat
from fish import Fish


print("Test 1: Animals (same calls, each class answers its own way)")
for animal in [Spider(), Cat("Tom"), Fish()]:
    animal.walk()
    animal.eat()

print("Test 2: Pets (expect Tom, Fluffy, Nemo)")
for pet in [Cat("Tom"), Cat(), Fish()]:
    print(pet.getName())
    pet.play()

print("Test 3: setName")
fish = Fish()
fish.setName("Bubbles")
print(fish.getName())

print("Test 4: Which ones are Pets? (expect False True True)")
print(isinstance(Spider(), Pet), isinstance(Cat(), Pet), isinstance(Fish(), Pet))

print("Test 5: Abstract classes cannot be created")
try:
    Animal(4)
except TypeError as e:
    print("Animal:", e)

try:
    Pet()
except TypeError as e:
    print("Pet:", e)

print("Test 6: Bad input is rejected")
try:
    Cat("   ")
except ValueError as e:
    print("Cat:", e)