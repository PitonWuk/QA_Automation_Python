"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об'єкт цього класу,
представляючи студента. Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.

"""


class Student:
    def __init__(self, name, surname, age, average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def get_info(self):
        return (f"Student: {self.name} {self.surname}, Age: {self.age}, Average grade: {self.average_grade}")


student = Student("Nik", "Petrenko", 23, 88.3)
print(student.get_info())

student.update_average_grade(91.2)
print(student.get_info())





