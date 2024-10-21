"""
Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від
нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""

from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return 4 * self.__side_length


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


figures = [
    Square(4),
    Circle(3),
    Rectangle(5, 7)
]

for figure in figures:
    print(f"Figure: {figure.__class__.__name__}")
    print(f"Square: {figure.area():.2f}")
    print(f"Perimeter: {figure.perimeter():.2f}")
    print()
