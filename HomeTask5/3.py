# Создайте функцию генератор чисел Фибоначчи

def fibonacci(a=1, b=2):
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci(0, 1)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
