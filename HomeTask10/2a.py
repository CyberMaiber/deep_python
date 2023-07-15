# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if side1 == side2 == side3:
            self.triangle_type = "равносторонний"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            self.triangle_type = "равнобедренный"
        else:
            self.triangle_type = "разносторонний"
    
    def info(self):
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")
        print(f"Тип треугольника: {self.triangle_type}")

triangle1 = Triangle(5, 5, 5)
triangle2 = Triangle(4, 4, 6)
triangle3 = Triangle(3, 4, 5)

triangle1.info()
print()
triangle2.info()
print()
triangle3.info()