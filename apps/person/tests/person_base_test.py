from faker import Faker
from ..models import Email, Person, Phone
from apps.address.tests.address_base_test import FakeDataFactory as address_create


class FakeDataFactory:
    def __init__(self):
        self.fake = Faker()
        self.address = address_create()

    def create_person(self):
        name = self.fake.name()
        document = self.fake.random_number(digits=11)
        rg = (self.fake.random_number(digits=11),)
        birth_date = self.fake.date_time_between(start_date="-20y", end_date="now")
        addresses = self.address.create_address()
        return Person.objects.create(
            name=name,
            document=document,
            rg=rg,
            birth_date=birth_date,
            addresses=addresses,
        )

    def create_email(self):
        email = self.fake.email()
        person = self.create_person()
        return Email.objects.create(email=email, person=person, type="1")

    def create_phone(self):
        phone = str(self.fake.random_number(digits=11))
        person = self.create_person()
        return Phone.objects.create(phone=phone, person=person, type="1")
