# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_numbers(x, y):
    return x + y


result = sum_numbers(4, 8)
print(f"Sum of numbers: {result}")




# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_numbers(list_numbers):
    return sum(list_numbers)/len(list_numbers) if len(list_numbers) > 0 else 0

list_numbers = [1, 55, 87, 5, 47, 22]
result = average_numbers(list_numbers)
print(f"Average of numbers: {result}")




# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(some_text):
    return some_text[::-1]

some_text = "Hello World!"
result = reverse_string(some_text)
print(f"Reverse string is: {result}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key=len) if words else None

words = ["test", "Hello", "World", "automation"]
result = longest_word(words)
print(f"The longest word is: {result}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті


def sum_even_numbers(sum_of_numbers):
    return sum(number for number in lst1 if number % 2 == 0)


lst1 = [12, 54, 1, 5, 8, 77, 45, 66]
result = sum_even_numbers(lst1)
print(f"The sum of even numbers is: {result}")

# task 8
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими


def list_str(lst2):
    return [i for i in lst1 if isinstance(i, str)]


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
result = list_str(lst1)
print(result)

# task 9
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


def unique_characters(users_string):
    return len(set(users_string))


users_string = input("Enter any string, please: ")
result = unique_characters(users_string)
print(True if result > 10 else False)


# task 10
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""


def part_of_pay(number):
    return number * 6


result = part_of_pay(1179)
print(f"The cost of the computer is: {result * 6} hrn.")
