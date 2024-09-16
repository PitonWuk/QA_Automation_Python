# task 7
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті


def sum_even_numbers(sum_of_numbers):
    return sum(number for number in lst1 if number % 2 == 0)


# task 8
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими


def list_str(lst2):
    return [i for i in lst1 if isinstance(i, str)]

# task 9
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


def unique_characters(users_string):
    return True if len(set(users_string)) > 10 else False



# task 10
"""Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def part_of_pay(number):
    return number * 6


