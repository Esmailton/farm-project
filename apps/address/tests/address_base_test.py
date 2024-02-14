from faker import Faker
from ..models import Address, City, Country, UF


class FakeDataFactory:
    def __init__(self):
        self.fake = Faker("pt_BR")

    def create_address(self):
        logradouro = self.fake.street_address()
        number = self.fake.building_number()
        zipcode = self.fake.postcode()
        neighborhood = self.fake.neighborhood()
        city = self.create_city()
        return Address.objects.create(
            logradouro=logradouro,
            number=number,
            zipcode=zipcode,
            neighborhood=neighborhood,
            city=city,
        )

    def create_city(self):
        name = self.fake.city()
        uf = self.create_uf()
        return City.objects.create(name=name, uf=uf)

    def create_uf(self):
        acronym = self.fake.state_abbr()
        country = self.create_country()
        existing_uf = UF.objects.filter(acronym=acronym).first()
        if existing_uf:
            return existing_uf
        name = self.fake.text(max_nb_chars=20)
        return UF.objects.create(name=name, acronym=acronym, country=country)

    def create_country(self):
        name = self.fake.country()
        existing_country = Country.objects.filter(name=name).first()
        if existing_country:
            return existing_country
        return Country.objects.create(name=name)
