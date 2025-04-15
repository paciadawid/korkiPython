class Animal:

    def __init__(self, species, name, weight):
        self.species = species
        self.name = name
        self.weight = weight

    def make_a_sound(self):
        sound = self.get_a_sound(self.species)
        print(sound)

    def get_a_sound(self, species):
        if species == "cat":
            return "meow"
        elif species == "dog":
            return "bark"
        else:
            return "unknown"

class Dog(Animal):

    def __init__(self, name, weight, breed):
        super().__init__("dog", name, weight)
        self.breed = breed

    def calculate_food(self):
        return self.weight * 10 / 1000


kot = Animal("cat", "Stefan", 6)
borsuk = Animal("badger", "Andrzej", 20)

print(kot.weight)
kot.make_a_sound()

jamnik = Dog("Jan", 50, "jamnik")
print(jamnik.calculate_food())