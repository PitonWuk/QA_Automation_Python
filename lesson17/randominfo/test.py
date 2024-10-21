
from faker import Faker
import randominfo as ri

fake = Faker()


class Person:
    def __init__(self) -> None:
        self.first_name = ri.get_first_name()
        self.last_name = ri.get_last_name()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.gender = ri.get_gender(self.first_name)
        self.country = fake.country()
        self.address = fake.address()


person1 = Person()

print(f"Full Name: {person1.full_name}")
print(f"Gender: {person1.gender}")
print(f"Country: {person1.country}")
print(f"Address: {person1.address}")
