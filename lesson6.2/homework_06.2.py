# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    word_with_h = input("Enter the word with 'h/H' character: ").lower()

    if 'h' in word_with_h:
        print("Done. Very good!")
        break
    else:
        print("There is no 'h'. Please, enter the word with 'h' or 'H' characters: ")






