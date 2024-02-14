from faker import Faker
from apps.workshop.models import Workshop
from apps.farm.tests.farm_base_test import FakeDataFactory as createe_farm


class FakeDataFactory:
    def __init__(self):
        self.fake = Faker()
        self.farm = createe_farm()

    def create_workshop(self):
        name = self.fake.company_suffix()
        farm = self.farm.create_farm()
        return Workshop.objects.create(name=name, farm=farm)
