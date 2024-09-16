"""Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”"""

array_of_numbers = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_of_numbers(num):
    try:
        numbers = [int(i) for i in num.split(",")]
        return sum(numbers)
    except ValueError:
        print("Can not do that!")
        return None

for num in array_of_numbers:
    result = sum_of_numbers(num)
    if result is not None:
        print(f"Sum of numbers in the string'{num}: {result}")

