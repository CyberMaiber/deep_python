# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Fish(Animal):
    def __init__(self, name, age, fins):
        super().__init__(name, age)
        self.fins = fins
    
    def info(self):
        super().info()
        print(f"Fins: {self.fins}")

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan
    
    def info(self):
        super().info()
        print(f"Wingspan: {self.wingspan}")

class Mammal(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self.weight = weight
    
    def info(self):
        super().info()
        print(f"Weight: {self.weight}")

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, **kwargs):
        if animal_type == "Fish":
            return Fish(name, age, kwargs.get("fins"))
        elif animal_type == "Bird":
            return Bird(name, age, kwargs.get("wingspan"))
        elif animal_type == "Mammal":
            return Mammal(name, age, kwargs.get("weight"))
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Пример использования классов и класса-фабрики
fish = AnimalFactory.create_animal("Fish", "Nemo", 2, fins=4)
bird = AnimalFactory.create_animal("Bird", "Eagle", 5, wingspan=2.5)
mammal = AnimalFactory.create_animal("Mammal", "Lion", 8, weight=200)

fish.info()
print()
bird.info()
print()
mammal.info()