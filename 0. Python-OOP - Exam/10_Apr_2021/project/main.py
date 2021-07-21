from project.controller import Controller
from project.decoration.plant import Plant

a = Controller()
print(a.add_aquarium("SaltwaterAquarium", "Underworld"))
print(a.add_aquarium("FreshwaterAquarium", "Swamp"))
print(a.add_fish("Underworld", "FreshwaterFish", "Nemo", "Clownfish", 13.40))
print(a.add_fish("Underworld", "SaltwaterFish", "Nemo", "Clownfish", 13.40))
print(a.add_aquarium("FreshwaterAquarium", "Riverworld"))
print(a.add_fish("Riverworld", "FreshwaterFish", "Emerald", "Catfish", 7.32))
print(a.add_fish("Underworld", "SweetwaterFish", "Diamond", "Catfish", 3.50))
print(a.add_decoration("Plant"))
print(a.insert_decoration("Riverworld", "Plant"))
print(a.insert_decoration("Underworld", "Plant"))
print(a.add_decoration("Plant"))
print(a.add_decoration("Plant"))
print(a.insert_decoration("Underworld", "Plant"))
print(a.insert_decoration("Underworld", "Plant"))
print(a.feed_fish("Riverworld"))
print(a.feed_fish("Underworld"))
print(a.calculate_value("Riverworld"))
# print(a.add_fish("Riverworld", "FreshwaterFish", "", "Species", 20))
# print(a.add_fish("Riverworld", "FreshwaterFish", "Name", "", 20))
# print(a.add_fish("Riverworld", "FreshwaterFish", "Name", "Species", - 10))
print(a.report())
