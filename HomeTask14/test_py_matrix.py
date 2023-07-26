import pytest
from matrix import Matrix

@pytest.fixture
def matrix1():
    return Matrix([[1, 2, 3], [4, 5, 6], [13, 14, 15]])

@pytest.fixture
def matrix2():
    return Matrix([[7, 8, 9], [10, 11, 12], [16, 17, 18]])

def test_add(matrix1, matrix2):
    sumatrix = matrix1.add(matrix2)
    assert sumatrix == Matrix([[8, 10, 12], [14, 16, 18], [29, 31, 33]])
    sumatrix = matrix2.add(matrix1)
    assert sumatrix == Matrix([[8, 10, 12], [14, 16, 18], [29, 31, 33]])

def test_err(matrix1):
        with pytest.raises(ValueError):
            matrix_ = matrix1.multiply(1)     

def test_mul(matrix1, matrix2):
    mulmatrix = matrix1.multiply(matrix2)
    assert mulmatrix == Matrix([[75, 81, 87],[174, 189, 204],[471, 513, 555]])

def test_transpose(matrix1):
      assert str(matrix1.transpose()) == str(Matrix([[1, 4, 13], [2, 5, 14], [3, 6, 15]]))

if __name__ == "__main__":
    pytest.main(['-v'])