from django.core.exceptions import ValidationError
from django.test import TestCase
from parameterized import parameterized

from .farm_base_test import FakeDataFactory


class DepartmentModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.department = self.factory.create_department()

    @parameterized.expand(
        [
            ("department", 50),
        ]
    )
    def test_department_fields_max_length(self, field, max_length):
        setattr(self.department, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.department.full_clean()

    def test_department_representation(self):
        self.assertEqual(str(self.department), self.department.department)

    def test_department_get_absolute_url(self):
        self.assertEqual(
            f"/department/{self.department.id}/detail/",
            self.department.get_absolute_url(),
        )


class FarmModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.farm = self.factory.create_farm()

    @parameterized.expand(
        [
            ("latitude", 100),
            ("longitude", 100),
            ("name", 150),
        ]
    )
    def test_farm_fields_max_length(self, field, max_length):
        setattr(self.farm, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.farm.full_clean()

    def test_farm_representation(self):
        self.assertEqual(str(self.farm), self.farm.name)

    def test_farm_get_absolute_url(self):
        self.assertEqual(f"/farm/{self.farm.id}/detail/", self.farm.get_absolute_url())
