from django.core.exceptions import ValidationError
from django.test import TestCase
from parameterized import parameterized

from .address_base_test import FakeDataFactory


class AddressModelTest(TestCase):
    def setUp(self):
        self.factory = FakeDataFactory()
        self.address = self.factory.create_address()

    @parameterized.expand(
        [
            ("logradouro", 150),
            ("zipcode", 9),
            ("neighborhood", 100),
        ]
    )
    def test_address_fields_max_length(self, field, max_length):
        setattr(self.address, field, "X" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.address.full_clean()

    def test_address_representation(self):
        self.assertEqual(str(self.address), self.address.logradouro)

    def test_address_get_absolute_url(self):
        self.assertEqual(
            f"/address/{self.address.id}/detail/", self.address.get_absolute_url()
        )
