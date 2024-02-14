from faker import Faker
from apps.person.tests.person_base_test import FakeDataFactory as person_create
from apps.farm.models import Department, Farm
from apps.address.tests.address_base_test import FakeDataFactory as address_create


class FakeDataFactory:
    def __init__(self):
        self.fake = Faker("pt_BR")
        self.person = person_create()
        self.address = address_create()

    def create_department(self):
        department = self.fake.text(max_nb_chars=5)
        description = self.fake.text(max_nb_chars=50)
        return Department.objects.create(department=department, description=description)

    def create_farm(self):
        name = self.fake.company()
        owner = self.person.create_person()
        manager = self.person.create_person()
        latitude = self.fake.latitude()
        longitude = self.fake.longitude()
        location = self.address.create_address()
        size_hc = self.fake.random_number(digits=4)
        departments = self.create_department()
        farm = Farm.objects.create(
            name=name,
            owner=owner,
            manager=manager,
            latitude=latitude,
            longitude=longitude,
            location=location,
            size_hc=size_hc,
        )
        farm.departments.add(departments)

        return farm
