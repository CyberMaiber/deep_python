class Matrix:
    """
    Класс Matrix для работы с матрицами.
    """

    def __init__(self, matrix):
        """
        Инициализация объекта класса Matrix.

        Параметры:
        - matrix (list[list]): Матрица, представленная в виде списка списков.
        """
        self.matrix = matrix

    def __str__(self):
        """
        Возвращает строковое представление матрицы.

        Возвращает:
        - str: Строковое представление матрицы.
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        matrix_str = ""
        for i in range(rows):
            for j in range(cols):
                matrix_str += str(self.matrix[i][j]) + "\t"
            matrix_str += "\n"
        return matrix_str

    def __eq__(self, other):
        """
        Проверяет равенство двух матриц.

        Параметры:
        - other (Matrix): Другой объект класса Матрица.

        Возвращает:
        - bool: True, если матрицы равны, иначе False.
        """
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def add(self, other):
        """
        Складывает две матрицы.

        Параметры:
        - other (Matrix): Другой объект класса Матрица.

        Возвращает:
        - Matrix: Результат сложения матриц.
        >>> matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])
        >>> matrix2 = Matrix([[7, 8, 9], [10, 11, 12], [16, 17, 18]])
        >>> sumatrix = Matrix([[8, 10, 12], [14, 16, 18], [29, 31, 33]])
        >>> str(sumatrix) == str(matrix1.add(matrix2))
        True
        >>> str(sumatrix) == str(matrix2.add(matrix1))
        True
        """
        if isinstance(other, Matrix):
            rows = len(self.matrix)
            cols = len(self.matrix[0])
            result = [[0 for _ in range(cols)] for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)
        else:
            raise ValueError(
                "Невозможно сложить матрицу с другим типом объекта")

    def multiply(self, other):
        """
        Умножает две матрицы.

        Параметры:
        - other (Matrix): Другой объект класса Матрица.

        Возвращает:
        - Matrix: Результат умножения матриц.
        
        >>> matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])
        >>> matrix2 = Matrix([[7, 8, 9], [10, 11, 12], [16, 17, 18]])
        >>> multmatrix = Matrix([[75, 81, 87],[174, 189, 204],[471, 513, 555]])
        >>> str(matrix1.multiply(matrix2)) == str(multmatrix)
        True

        """
        if isinstance(other, Matrix):
            rows1 = len(self.matrix)
            cols1 = len(self.matrix[0])
            rows2 = len(other.matrix)
            cols2 = len(other.matrix[0])
            if cols1 != rows2:
                raise ValueError(
                    "Невозможно умножить матрицы с данными размерностями")
            result = [[0 for _ in range(cols2)] for _ in range(rows1)]
            for i in range(rows1):
                for j in range(cols2):
                    for k in range(cols1):
                        result[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return Matrix(result)
        else:
            raise ValueError(
                "Невозможно умножить матрицу на другой тип объекта")

    def transpose(self):
        """
        Транспонирует матрицу.

        Возвращает:
        - Matrix: Транспонированная матрица.
        >>> matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])
        >>> trmatrix = Matrix([[1, 4, 13], [2, 5, 14], [3, 6, 15]])
        >>> str(matrix1.transpose()) == str(trmatrix)
        True
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        transposed = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = self.matrix[i][j]
        return Matrix(transposed)


# Пример использования класса
# matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])
# matrix2 = Matrix([[7, 8, 9], [10, 11, 12], [16, 17, 18]])
# matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])

# print(matrix1)
# print(matrix2)

# print("Равенство матриц:")
# print(matrix1 == matrix2)
# print()

# print("Сложение матриц:")
# matrix_sum = matrix1.add(matrix2)
# print(matrix_sum)
# print()

# print("Умножение матриц:")
# matrix_mult = matrix1.multiply(matrix2)
# print(matrix_mult)

# print("Транспонирование матрицы:")
# matrix_transposed = matrix1.transpose()
# print(matrix_transposed)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)