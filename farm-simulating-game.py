import random

# Define Crop class
class Crop:
    def __init__(self, name, growth_rate, water_need, light_need):
        self.name = name
        self.growth_rate = growth_rate
        self.water_need = water_need
        self.light_need = light_need
        self.age = 0
        self.height = 0
        self.status = "seed"

    def grow(self, water, light):
        self.age += 1
        if water >= self.water_need and light >= self.light_need:
            self.height += self.growth_rate
            self.status = "mature"
        else:
            self.status = "seed"

    def needs(self):
        return f"Water need: {self.water_need}\nLight need: {self.light_need}"

    def get_status(self):
        return f"Age: {self.age}\nHeight: {self.height}\nStatus: {self.status}"

# Define Farm class
class Farm:
    def __init__(self):
        self.crops = []

    def add_crop(self, crop):
        self.crops.append(crop)

    def simulate_day(self):
        for crop in self.crops:
            crop.grow(random.randint(1, 10), random.randint(1, 10))

# Create crops
wheat = Crop("Wheat", 2, 5, 5)
corn = Crop("Corn", 3, 6, 4)
potato = Crop("Potato", 4, 4, 6)

# Create farm and add crops
farm = Farm()
farm.add_crop(wheat)
farm.add_crop(corn)
farm.add_crop(potato)

# Simulate a day and print crop status
farm.simulate_day()
for crop in farm.crops:
    print(f"Crop: {crop.name}")
    print(crop.needs())
    print(crop.get_status())
