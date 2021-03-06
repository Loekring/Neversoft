class Item:
    # Baseklasse for alle gjenstandar
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "Foran deg ligg {}. Den {}.".format(self.name, self.description)


class Knife(Item):
    # Klassa for alle gjenstandar som er knivar
    def __init__(self, name, description, sharpness):
        super().__init__(name, description)
        self.sharpness = sharpness

    def __str__(self):
        return "Foran deg ligg {}. Den {}. \nKniven er {}.".format(self.name, self.description, self.sharpness)


class Food(Item):
    # Klassa for alle gjenstandar som er mat
    def __init__(self, name, description, nutritionAmount):
        super().__init__(name, description)
        self.nutritionAmount = nutritionAmount

    def __str__(self):
        return "Foran deg ligg {}. Den {}. \nEnergiinnhold: {} kJ/100g".format(self.name, self.description, int(self.nutritionAmount))


# Her ligg alle gjenstandane
brødkniv = Knife("ein brødkniv", "har noko rust på eggen", "veldig sløv")
bolle = Food("ein bolle", "er nybakt og lukta fyller rommet", 124)


# Diverse testar:
# print (kakespade)
# kakespade = Item("kakespade", "ser ut som ei kakespade")
# print(brødkniv.sharpness)
