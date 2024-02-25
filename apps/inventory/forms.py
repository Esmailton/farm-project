from django.forms import ModelForm
from apps.inventory.models import Category, ColumnSpace, Inventory, LineSpace, MeasureType, ProductInventory, Product, Shelf, Street 


class StreetForm(ModelForm):
    class Meta:
        model = Street
        fields =['name', 'inventory', 'description']

class ShelfForm(ModelForm):
    class Meta:
        model= Shelf
        fields = ['name', 'street']
    ...

class LineSpaceForm(ModelForm):
    class Meta:
        model = LineSpace
        fields = [
            'line',
            'shelf'
        ]

class ColumnSpaceForm(ModelForm):
    class Meta:
        model = ColumnSpace
        fields = [
            'column',
            'shelf'
        ]

class ProductInventoryForm(ModelForm):
    class Meta:
        model = ProductInventory
        fields = ['street', 'shelf','line_space', 'column_space', 'quantity', 'reorder_point']

class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ['name', 'description']

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price', 
            'picture', 
            'bar_code',
            'qr_code', 
            'internal_code', 
            'category', 
            'measuretype',
        ]

class MeasureTypeForm(ModelForm):
    
    class Meta:
        model = MeasureType
        fields = [
                    'name', 
                    'description', 
                    'acronym', 
                    'measure_type'
                ]

class InventoryForm(ModelForm):
    
    class Meta:
        model = Inventory
        fields = [
                'name',
                'farm'
                ]