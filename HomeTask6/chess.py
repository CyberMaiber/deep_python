import random

def random_queens():
    queens = []
    for i in range(8):
        row = random.randint(1, 8)
        queens.append((i+1, row))
    return queens

def is_attacking(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return True
    return False

def has_attacking_queens(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if is_attacking(queens[i][0], queens[i][1], queens[j][0], queens[j][1]):
                return True
    return False