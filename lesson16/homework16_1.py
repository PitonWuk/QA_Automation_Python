"""
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department, а клас Developer -
атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє
керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Employee):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


def test_team_lead_attributes():
    team_lead = TeamLead("Alice", 90000, "IT", "Python", 5)
    assert team_lead.name == "Alice"
    assert team_lead.salary == 90000
    assert team_lead.department == "IT"
    assert team_lead.programming_language == "Python"
    assert team_lead.team_size == 5
    print("All tests passed!")


test_team_lead_attributes()
