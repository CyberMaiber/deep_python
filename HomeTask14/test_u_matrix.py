import unittest

from matrix import Matrix

class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])
        self.matrix2 = Matrix([[7, 8, 9], [10, 11, 12], [16, 17, 18]])

    def test_instance (self):
        self.assertIsInstance(self.matrix1, Matrix)

    def test_add(self):
        sumatrix = Matrix([[8, 10, 12], [14, 16, 18], [29, 31, 33]])
        self.assertEqual(self.matrix1.add(self.matrix2), sumatrix)
        self.assertEqual(self.matrix2.add(self.matrix1), sumatrix)

    def test_err(self):
        with self.assertRaises(ValueError):
            matrix_ = self.matrix1.multiply(1)         

if __name__ == '__main__':
    unittest.main(verbosity=10)