from faker import Faker
from ..models import Category, ColumnSpace, Inventory,MeasureType,LineSpace, Product,ProductInventory,Shelf,Street
from apps.farm.tests.farm_base_test import FakeDataFactory as farm

class FakeDataFactory:
    def __init__(self):
        self.fake = Faker()
        self.farm = farm()

    def create_street(self):
        name = self.fake.word()
        description = self.fake.paragraph(nb_sentences=3)
        return Street.objects.create(
            name=name,
            description=description,
        )

    def create_shelf(self):
        name = self.fake.word()
        street = self.create_street()
        return Shelf.objects.create(
            name=name,
            street=street,
        )
    
    def create_line_space(self):
        line = self.fake.word()
        shelf = self.create_shelf()
        return LineSpace.objects.create(
            line=line,
            shelf=shelf,
        )
    
    def create_column_space(self):
        column = self.fake.word()
        shelf = self.create_shelf()
        return ColumnSpace.objects.create(
            column=column,
            shelf=shelf,
        )

    def create_inventory(self):
        name = self.fake.word()
        street = self.create_street()
        farm = self.farm.create_farm()
        return Inventory.objects.create(
            name=name,
            street=street,
            farm = farm
        )
    
    def create_category(self):
        name = self.fake.word()
        return Category.objects.create(name=name)

    def create_measure_type(self):
        name = self.fake.word()
        description = self.fake.text()
        acronym = 'EX'
        measure_type = 'Peso'
        return MeasureType.objects.create(name=name, description=description, acronym=acronym, measure_type=measure_type)

    def create_product(self):

        name = self.fake.word()
        description = self.fake.text()
        price = self.fake.random_int(min=1, max=100)
        picture = self.fake.file_path(depth=3)
        bar_code = self.fake.random_int(min=1, max=100)
        qr_code = self.fake.random_int(min=1, max=100)
        internal_code = self.fake.random_int(min=1, max=100)
        category= self.create_category()
        measuretype =self.create_measure_type()

        return Product.objects.create(
            name=name,
            description=description,
            price=price,
            picture=picture,
            bar_code=bar_code,
            qr_code=qr_code,
            internal_code=internal_code,
            category=category,
            measuretype=measuretype
        )

    def create_product_inventory(self):
        product = self.create_product()
        shelf = self.create_shelf()
        street = self.create_street()
        line_space = self.create_line_space()
        column_space = self.create_column_space()
        quantity = self.fake.random_number(digits=3)
        reorder_point = self.fake.random_number(digits=2)
        return ProductInventory.objects.create(
            product = product,
            shelf= shelf,
            street= street,
            line_space= line_space,
            column_space= column_space,
            quantity= quantity,
            reorder_point= reorder_point
        )
