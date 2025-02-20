class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species.lower() == 'mammal':
            self.mammals.append(name)
        elif species.lower() == 'fish':
            self.fishes.append(name)
        elif species.lower() == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1
    def get_info(self, species):
        result = ""
        if species.lower() == 'mammal':
            result = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species.lower() == 'fish':
            result = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species.lower() == 'bird':
            result = f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
number = int(input())
zoo = Zoo(zoo_name)

for _ in range(number):
    current_species, current_name = input().split()
    zoo.add_animal(current_species, current_name)

animal_type = input()
print(zoo.get_info(animal_type))