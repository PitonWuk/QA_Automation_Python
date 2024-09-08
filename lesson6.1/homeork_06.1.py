# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

users_string = input("Enter any string, please: ")

unique_characters = set(users_string)

quantity_unique_characters = len(unique_characters)

print(True if quantity_unique_characters > 10 else False)

