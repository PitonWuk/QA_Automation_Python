"""
Генератори:

Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
Ітератори:

Реалізуйте ітератор для зворотного виведення елементів списку.
Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
Декоратори:

Напишіть декоратор, який логує аргументи та результати викликаної функції.
Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

"""

# Generators
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Iterators


class ReverseIterator:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


class EvenNumbersIterator:

    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        current_value = self.current
        self.current += 2
        return current_value

# Decorators


def logger(func):

    def wrapper(*args, **kwargs):
        print(f"Calling a function: {func.__name__}")
        print(f"Arguments: {args}, Named arguments: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")

        return result

    return wrapper


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An exception has arisen: {e}")
            return None

    return wrapper


