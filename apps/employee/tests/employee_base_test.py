from faker import Faker
from apps.employee.models import Position, Employee
from apps.person.tests.person_base_test import FakeDataFactory as person_fake
from apps.farm.tests.farm_base_test import FakeDataFactory as farm_fake


class FakeDataFactory:
    def __init__(self):
        self.fake = Faker("pt_BR")
        self.person = person_fake()
        self.farm = farm_fake()

    def create_position(self):
        position = self.fake.job()
        description = self.fake.text(max_nb_chars=50)
        return Position.objects.create(position=position, description=description)

    def create_employee(self):
        person = self.person.create_person()
        department = self.farm.create_department()
        position = self.create_position()
        status = "2"
        farm = self.farm.create_farm()
        return Employee.objects.create(
            person=person,
            department=department,
            position=position,
            status=status,
            farm=farm,
        )
