# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst1 = [12, 54, 1, 5, 8, 77, 45, 66]
sum_of_numbers = sum(number for number in lst1 if number % 2 == 0)
print(f"The sum of even numbers is: {sum_of_numbers}")

