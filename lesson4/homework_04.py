adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

#solution
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)
print("-" * 100)

# task 02 ==
""" Замініть .... на пробіл"""

#solution
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)
print("-" * 100)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами."""

#solution
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)
print("-" * 100)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера 'h'"""

#solution
character_h = adwentures_of_tom_sawer.count('h')
print(f"There are {character_h} times in the text")

print("-" * 100)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
#solution
list_words = adwentures_of_tom_sawer.split()
istitle_words = sum(1 for word in list_words if word[0].isupper())
print(f"There are {istitle_words} title words.")
print("-" * 100)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
#solution
first_word_Tom = adwentures_of_tom_sawer.find("Tom")
second_word_Tom = adwentures_of_tom_sawer.find("Tom", first_word_Tom + 1)
print(f"Word Tom second time is on {second_word_Tom} position")
print("-" * 100)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
#solution
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
for sentence in adwentures_of_tom_sawer_sentences:
    print(sentence)
print(adwentures_of_tom_sawer_sentences)

print("-" * 100)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
#solution
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
lower_fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
print(lower_fourth_sentence)

print("-" * 100)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
#solution
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(f"Some sentence begin from 'By the time'")
    else:
        continue
print("-" * 100)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
last_sentence = adwentures_of_tom_sawer_sentences[-1]
words_in_last_sentence = last_sentence.split()
print(f"The number of quantity of words in last sentence are: {len(words_in_last_sentence)}")


