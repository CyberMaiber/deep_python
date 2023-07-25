# Возьмите 1-3 задачи из тех что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы-исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонам отрицательной длины.

class InvalidTriangleError(Exception):
    pass

class NegativeLengthError(InvalidTriangleError):
    def __init__(self, length):
        self.length = length
    def __str__(self):
        return f"Отрицательная длина стороны: {self.length}"

class ZeroLengthError(InvalidTriangleError):
    def __init__(self, length):
        self.length = length
    def __str__(self):
        return f"Нулевая длина стороны: {self.length}"

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.triangle_type = self.check_triangle_type()

    def check_triangle_type(self):
        if self.side1 <= 0:
            raise NegativeLengthError(self.side1)
        if self.side2 <= 0:
            raise NegativeLengthError(self.side2)
        if self.side3 <= 0:
            raise NegativeLengthError(self.side3)
        if self.side1 + self.side2 <= self.side3 or self.side1 + self.side3 <= self.side2 or self.side2 + self.side3 <= self.side1:
            raise InvalidTriangleError("Треугольник с такими сторонами не может существовать")
        if self.side1 == self.side2 and self.side2 == self.side3:
            return "Равносторонний треугольник"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"


try:
    side1 = float(input("Введите длину первой стороны: "))
    side2 = float(input("Введите длину второй стороны: "))
    side3 = float(input("Введите длину третьей стороны: "))
    triangle = Triangle(side1, side2, side3)
    print("Тип треугольника:", triangle.triangle_type)
except InvalidTriangleError as err:
    print("Ошибка создания треугольника:", err)
except ValueError:
    print("Ошибка ввода: некорректное значение длины стороны")

