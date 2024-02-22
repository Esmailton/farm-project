from django.core.exceptions import ValidationError
from django.test import TestCase
from parameterized import parameterized

from .vehicle_base_test import FakeDataFactory


class VehicleTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.vehicle = self.factory.create_vehicle()

    @parameterized.expand(
        [
            ("name", 150),
            ("type", 3),
            ("serial_number", 150),
            ("plate", 15),
            ("color", 3),
        ]
    )
    def test_vehicle_fields_max_length(self, field, max_length):
        setattr(self.vehicle, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.vehicle.full_clean()

    def test_vehicle_representation(self):
        self.assertEqual(str(self.vehicle), self.vehicle.name)

    def test_vehicle_get_absolute_url(self):
        self.assertEqual(
            f"/vehicle/{self.vehicle.id}/detail/",
            self.vehicle.get_absolute_url(),
        )


class BrandTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.brand = self.factory.create_brand()

    @parameterized.expand(
        [
            ("name", 150),
            ("description", 255),
        ]
    )
    def test_brand_fields_max_length(self, field, max_length):
        setattr(self.brand, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.brand.full_clean()

    def test_brand_representation(self):
        self.assertEqual(str(self.brand), self.brand.name)

    def test_brand_get_absolute_url(self):
        self.assertEqual(
            f"/brand/{self.brand.id}/detail/",
            self.brand.get_absolute_url(),
        )


class FleetCategoryTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.create_fleet_category = self.factory.create_fleet_category()

    @parameterized.expand(
        [
            ("name", 150),
        ]
    )
    def test_fleet_fields_max_length(self, field, max_length):
        setattr(self.create_fleet_category, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.create_fleet_category.full_clean()

    def test_fleet_category_representation(self):
        self.assertEqual(
            str(self.create_fleet_category.name),
            self.create_fleet_category.name,
        )

    def test_fleet_get_absolute_url(self):
        self.assertEqual(
            f"/fleet_category/{self.create_fleet_category.id}/detail/",
            self.create_fleet_category.get_absolute_url(),
        )


class FleetTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.fleet = self.factory.create_fleet()

    @parameterized.expand(
        [
            ("name", 150),
        ]
    )
    def test_fleet_fields_max_length(self, field, max_length):
        setattr(self.fleet, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.fleet.full_clean()

    def test_fleet_representation(self):
        self.assertEqual(str(self.fleet), self.fleet.name)

    def test_fleet_get_absolute_url(self):
        self.assertEqual(
            f"/fleet/{self.fleet.id}/detail/",
            self.fleet.get_absolute_url(),
        )


class VehicleModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.vehicle_model = self.factory.create_vehicle_model()

    @parameterized.expand(
        [
            ("name", 150),
        ]
    )
    def test_vehicle_model_fields_max_length(self, field, max_length):
        setattr(self.vehicle_model, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.vehicle_model.full_clean()

    def test_vehicle_model_representation(self):
        self.assertEqual(str(self.vehicle_model), self.vehicle_model.name)

    def test_vehicle_model_get_absolute_url(self):
        self.assertEqual(
            f"/vehicle_model/{self.vehicle_model.id}/detail/",
            self.vehicle_model.get_absolute_url(),
        )
