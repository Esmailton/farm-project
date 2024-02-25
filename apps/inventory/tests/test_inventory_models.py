from django.core.exceptions import ValidationError
from django.test import TestCase
from parameterized import parameterized
from .inventory_base_test import FakeDataFactory


class LineSpaceModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.line_space = self.factory.create_line_space()
    
    @parameterized.expand([
            ('line', 150)
        ])

    def test_field_line_space_max_length(self, field, max_length):
        setattr(self.line_space, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.line_space.full_clean()

    def test_line_space_representation(self):
        self.assertEqual(
            self.line_space.line,
            str(self.line_space)
        )

    def test_line_space_get_absolute_url(self):
        self.assertEqual(f'/line_space/detail/{self.line_space.id}/', self.line_space.get_absolute_url())


class ShelfModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.shelf = self.factory.create_shelf()
    
    @parameterized.expand([
            ('name', 150)
        ])

    def test_field_Shelf_max_length(self, field, max_length):
        setattr(self.shelf, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.shelf.full_clean()

    def test_Shelf_representation(self):
        self.assertEqual(
            self.shelf.name,
            str(self.shelf)
        )

    def test_shelf_get_absolute_url(self):
        self.assertEqual(f'/shelf/detail/{self.shelf.id}/', self.shelf.get_absolute_url())


class ColumnSpaceModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.column_space = self.factory.create_column_space()
    
    @parameterized.expand([
            ('column', 150)
        ])

    def test_field_columnSpace_max_length(self, field, max_length):
        setattr(self.column_space, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.column_space.full_clean()

    def test_column_space_representation(self):
        self.assertEqual(
            self.column_space.column,
            str(self.column_space)
        )

    def test_columnSpace_get_absolute_url(self):
        self.assertEqual(f'/column_space/detail/{self.column_space.id}/', self.column_space.get_absolute_url())


class InventoryModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.inventory = self.factory.create_inventory()
    
    @parameterized.expand([
            ('name', 150)
        ])

    def test_field_inventory_max_length(self, field, max_length):
        setattr(self.inventory, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.inventory.full_clean()

    def test_column_space_representation(self):
        self.assertEqual(
            self.inventory.name,
            str(self.inventory)
        )

    def test_inventory_get_absolute_url(self):
        self.assertEqual(f'/inventory/detail/{self.inventory.id}/', self.inventory.get_absolute_url())


class StreetModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.street = self.factory.create_street()
    
    @parameterized.expand([
            ('name', 150)
        ])

    def test_field_street_max_length(self, field, max_length):
        setattr(self.street, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.street.full_clean()

    def test_street_representation(self):
        self.assertEqual(
            self.street.name,
            str(self.street)
        )

    def test_street_get_absolute_url(self):
        self.assertEqual(f'/street/detail/{self.street.id}/', self.street.get_absolute_url())


class ProductInventoryModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.product_inventory = self.factory.create_product_inventory()

    def test_product_inventory_representation(self):
        self.assertEqual(
            f"{self.product_inventory.product} - {self.product_inventory.quantity}",
            str(self.product_inventory)
        )

    def test_product_inventory_get_absolute_url(self):
        self.assertEqual(f'/product_inventory/detail/{self.product_inventory.id}/', self.product_inventory.get_absolute_url())

class CategoryModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.category = self.factory.create_category()
    
    @parameterized.expand([
            ('name', 100)
        ])

    def test_field_category_max_length(self, field, max_length):
        setattr(self.category, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_category_representation(self):
        self.assertEqual(
            self.category.name,
            str(self.category)
        )

    def test_category_get_absolute_url(self):
        self.assertEqual(f'/category/detail/{self.category.id}/', self.category.get_absolute_url())


class MeasureTypeModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.measure_type = self.factory.create_measure_type()

    @parameterized.expand([
        ('name', 100),
        ('measure_type', 100),
        ('acronym', 4),
    ])

    def test_fields_measure_type_max_length(self, field, max_length):
        setattr(self.measure_type, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.measure_type.full_clean()
    
    def test_measure_type_representation(self):
        self.assertEqual(
            self.measure_type.name,
            str(self.measure_type)
        )

    def test_measure_type_get_absolute_url(self):
        self.assertEqual(
            f'/measure_type/detail/{self.measure_type.id}/',
            self.measure_type.get_absolute_url()
        )


class ProductModelTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.product = self.factory.create_product()

    @parameterized.expand([
        ('name', 100)
    ])

    def test_fields_product_max_length(self, field, max_length):
        setattr(self.product, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.product.full_clean()
    
    def test_product_representation(self):
        self.assertEqual(
            self.product.name,
            str(self.product)
        )

    def test_product_get_absolute_url(self):
        self.assertEqual(
            f'/product/detail/{self.product.id}/',
            self.product.get_absolute_url()
        )