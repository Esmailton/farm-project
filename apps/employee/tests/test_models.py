from django.core.exceptions import ValidationError
from django.test import TestCase
from parameterized import parameterized

from .employee_base_test import FakeDataFactory


class PositionModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.position = self.factory.create_position()

    @parameterized.expand(
        [
            ("position", 50),
        ]
    )
    def test_position_fields_max_length(self, field, max_length):
        setattr(self.position, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.position.full_clean()

    def test_position_representation(self):
        self.assertEqual(str(self.position), self.position.position)

    def test_position_get_absolute_url(self):
        self.assertEqual(
            f"/position/{self.position.id}/detail/", self.position.get_absolute_url()
        )


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.employee = self.factory.create_employee()

    @parameterized.expand(
        [
            ("status", 3),
        ]
    )
    def test_employee_fields_max_length(self, field, max_length):
        setattr(self.employee, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.employee.full_clean()

    def test_employee_representation(self):
        self.assertEqual(str(self.employee), self.employee.person.name)

    def test_employee_get_absolute_url(self):
        self.assertEqual(
            f"/employee/{self.employee.id}/detail/", self.employee.get_absolute_url()
        )
