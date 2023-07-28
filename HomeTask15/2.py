# Возьмите 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import sys

class InvalidTriangleError(Exception):
    pass

class NegativeLengthError(InvalidTriangleError):
    def __init__(self, length):
        self.length = length
    def __str__(self):
        return f"Отрицательная, либо нулевая длина стороны: {self.length}"

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

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='Hometask15\\triangle.log', filemode='a', encoding='utf-8', level=logging.INFO)
    try:
        if len(sys.argv) != 4:
            side1 = float(input("Введите длину первой стороны: "))
            side2 = float(input("Введите длину второй стороны: "))
            side3 = float(input("Введите длину третьей стороны: "))
        else:
            side1,side2,side3 = [float(sys.argv[i]) for i in range(1,4)]
        triangle = Triangle(side1, side2, side3)
        logging.info("Тип треугольника: " + triangle.triangle_type)    
    except InvalidTriangleError as err:
        logging.error("Ошибка создания треугольника: " + err.__str__())
    except ValueError:
        logging.error("Ошибка ввода: некорректное значение длины стороны")            

       