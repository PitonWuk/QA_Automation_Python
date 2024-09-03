#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal 
# on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter 
# which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're 
# sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland_corrected = '"Would you tell me, please, which way I ought to go from here?"\n"That depends ' \
    'a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then ' \
        'it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as ' \
            'an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quote_count = alice_in_wonderland_corrected.count("'")
print(single_quote_count)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland_corrected)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_black_sea = 436402
area_azov_sea = 37800
print(f"Azov and Black sea have area: {area_azov_sea + area_black_sea} square kilometers.")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
quantity_goods_together = 375291
first_and_second_stock = 250449
second_and_third_stock = 222950
third_stock = quantity_goods_together - first_and_second_stock
first_stock = quantity_goods_together - second_and_third_stock
second_stock = quantity_goods_together - first_stock + third_stock
print(f"There are goods on the: first stock - {first_stock}, second stock - {second_stock}, third stock - {third_stock} ")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
part_of_pay = 1179
print(f"The cost of the computer is: {part_of_pay * 6} hrn.")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
first_remainder = 8019 % 8
second_remainder = 9907 % 9
third_remainder = 2789 % 5
fourth_remainder = 7248 % 6
fifth_remainder = 7128 % 5
sixth_remainder = 19224 % 9
print(f"first reminder = {fifth_remainder}\nsecond remainder = {second_remainder}\nthird remainder = {third_remainder}"
      f"\nfourth remainder = {fourth_remainder}\nfifth remainder = {fifth_remainder}\nsixth remainder = {sixth_remainder}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza = 274 * 4
medium_pizza = 218 * 2
juice = 35 * 4
pie = 350
water = 21 * 3
print(f"General sum = {big_pizza + medium_pizza + juice + pie + water} hrn")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
quantity_photos = 232
quantity_photos_one_page = 8
print(f"The quantity of pages are: {quantity_photos / quantity_photos_one_page}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
general_distance = 1600
print(f"For such travel needs {general_distance / 100 * 9} liters of petrol."
      f"The family should buy petrol {(general_distance / 100 * 9) / 48} times.")