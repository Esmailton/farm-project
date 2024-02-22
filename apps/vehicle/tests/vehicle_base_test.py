from faker import Faker
from apps.vehicle.models import Vehicle, VehicleModel, Brand, Fleet, FleetCategory
import random
from apps.farm.tests.farm_base_test import FakeDataFactory as farm_create


class FakeDataFactory:
    def __init__(self):
        self.fake = Faker("pt_BR")
        self.farm = farm_create()

    def create_brand(self):
        brands_car = [
            "Toyota",
            "Honda",
            "Ford",
            "Chevrolet",
            "Volkswagen",
            "Nissan",
            "BMW",
            "Mercedes-Benz",
            "Audi",
            "Hyundai",
            "Kia",
            "Subaru",
            "Volvo",
            "Mazda",
            "Fiat",
            "Jeep",
            "Tesla",
            "Porsche",
            "Lexus",
            "Land Rover",
        ]
        name = random.choice(brands_car)
        description = self.fake.text(max_nb_chars=50)
        return Brand.objects.create(name=name, description=description)

    def create_vehicle_model(self):
        name = self.fake.word()
        description = self.fake.text(max_nb_chars=50)
        return VehicleModel.objects.create(name=name, description=description)

    def create_fleet_category(self):
        name = self.fake.text(max_nb_chars=10)
        description = self.fake.text(max_nb_chars=50)
        return FleetCategory.objects.create(name=name, description=description)

    def create_fleet(self):
        name = self.fake.text(max_nb_chars=10)
        description = self.fake.text(max_nb_chars=150)
        category = self.create_fleet_category()
        return Fleet.objects.create(
            name=name, description=description, category=category
        )

    def create_vehicle(self):
        name = self.fake.word()
        type = "1"
        brand = self.create_brand()
        model = self.create_vehicle_model()
        year_of_manufacture = 2024
        serial_number = self.fake.random_number(digits=30)
        plate = "PLT-7976"
        hour_meter = "983"
        mileage = "334234"
        status = "1"
        farm = self.farm.create_farm()
        color = "red"
        fleet = self.create_fleet()
        return Vehicle.objects.create(
            name=name,
            type=type,
            brand=brand,
            model=model,
            year_of_manufacture=year_of_manufacture,
            serial_number=serial_number,
            plate=plate,
            hour_meter=hour_meter,
            mileage=mileage,
            status=status,
            farm=farm,
            color=color,
            fleet=fleet,
        )
