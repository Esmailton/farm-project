from django.test import TestCase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from apps.workshop.tests.workshop_base_test import FakeDataFactory


class WorkshopModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.workshop = self.factory.create_workshop()

    @parameterized.expand(
        [
            ("name", 50),
        ]
    )
    def test_workshop_fields_max_length(self, field, max_length):
        setattr(self.workshop, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.workshop.full_clean()

    def test_workshop_representation(self):
        self.assertEqual(str(self.workshop), self.workshop.name)

    def test_workshop_get_absolute_url(self):
        self.assertEqual(
            f"/workshop/{self.workshop.id}/detail/", self.workshop.get_absolute_url()
        )
