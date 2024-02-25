from django.test import TestCase
from apps.inventory.tests.inventory_base_test import FakeDataFactory
from django.urls import reverse
from uuid import uuid4
from ..models import ColumnSpace, LineSpace, Product, Category, MeasureType, Inventory, ProductInventory, Shelf, Street


class ProductUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.product = self.factory.create_product()

    def test_product_create_url(self):
        url_product = reverse('inventory:product_create')
        self.assertEqual(url_product, '/product/create/')

    def test_product_list_url(self):
        url_product = reverse('inventory:product_list')
        self.assertEqual(url_product, '/product/list/')

    def test_product_detail_url(self):
        product_id = uuid4()
        url_product_detail = reverse('inventory:product_detail', kwargs={'pk': product_id})
        self.assertEqual(url_product_detail, f'/product/detail/{product_id}/')
    
    def test_product_update_url(self):
        product_id = uuid4()
        url_product_update = reverse('inventory:product_update', kwargs={'pk': product_id})
        self.assertEqual(url_product_update, f'/product/update/{product_id}/')

    def test_product_delete_url(self):
        product_id = uuid4()
        url_product_update = reverse('inventory:product_delete', kwargs={'pk': product_id})
        self.assertEqual(url_product_update, f'/product/delete/{product_id}/')


class StreetUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.street = self.factory.create_street()

    def test_street_create_url(self):
        url_street = reverse('inventory:street_create')
        self.assertEqual(url_street, '/street/create/')

    def test_street_list_url(self):
        url_street = reverse('inventory:street_list')
        self.assertEqual(url_street, '/street/list/')

    def test_street_detail_url(self):
        street_id = uuid4()
        url_street_detail = reverse('inventory:street_detail', kwargs={'pk': street_id})
        self.assertEqual(url_street_detail, f'/street/detail/{street_id}/')
    
    def test_street_update_url(self):
        street_id = uuid4()
        url_street_update = reverse('inventory:street_update', kwargs={'pk': street_id})
        self.assertEqual(url_street_update, f'/street/update/{street_id}/')

    def test_street_delete_url(self):
        street_id = uuid4()
        url_street_update = reverse('inventory:street_delete', kwargs={'pk': street_id})
        self.assertEqual(url_street_update, f'/street/delete/{street_id}/')

class ShelfUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.shelf = self.factory.create_shelf()

    def test_shelf_create_url(self):
        url_shelf = reverse('inventory:shelf_create')
        self.assertEqual(url_shelf, '/shelf/create/')

    def test_shelf_list_url(self):
        url_shelf = reverse('inventory:shelf_list')
        self.assertEqual(url_shelf, '/shelf/list/')

    def test_shelf_detail_url(self):
        shelf_id = uuid4()
        url_shelf_detail = reverse('inventory:shelf_detail', kwargs={'pk': shelf_id})
        self.assertEqual(url_shelf_detail, f'/shelf/detail/{shelf_id}/')
    
    def test_shelf_update_url(self):
        shelf_id = uuid4()
        url_shelf_update = reverse('inventory:shelf_update', kwargs={'pk': shelf_id})
        self.assertEqual(url_shelf_update, f'/shelf/update/{shelf_id}/')

    def test_shelf_delete_url(self):
        shelf_id = uuid4()
        url_shelf_update = reverse('inventory:shelf_delete', kwargs={'pk': shelf_id})
        self.assertEqual(url_shelf_update, f'/shelf/delete/{shelf_id}/')

class LineSpaceUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.line_space = self.factory.create_line_space()

    def test_line_space_create_url(self):
        url_line_space = reverse('inventory:line_space_create')
        self.assertEqual(url_line_space, '/line_space/create/')

    def test_line_space_list_url(self):
        url_line_space = reverse('inventory:line_space_list')
        self.assertEqual(url_line_space, '/line_space/list/')

    def test_line_space_detail_url(self):
        line_space_id = uuid4()
        url_line_space_detail = reverse('inventory:line_space_detail', kwargs={'pk': line_space_id})
        self.assertEqual(url_line_space_detail, f'/line_space/detail/{line_space_id}/')
    
    def test_line_space_update_url(self):
        line_space_id = uuid4()
        url_line_space_update = reverse('inventory:line_space_update', kwargs={'pk': line_space_id})
        self.assertEqual(url_line_space_update, f'/line_space/update/{line_space_id}/')

    def test_line_space_delete_url(self):
        line_space_id = uuid4()
        url_line_space_update = reverse('inventory:line_space_delete', kwargs={'pk': line_space_id})
        self.assertEqual(url_line_space_update, f'/line_space/delete/{line_space_id}/')


class ColumnSpaceUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.column_space = self.factory.create_column_space()

    def test_column_space_create_url(self):
        url_column_space = reverse('inventory:column_space_create')
        self.assertEqual(url_column_space, '/column_space/create/')

    def test_column_space_list_url(self):
        url_column_space = reverse('inventory:column_space_list')
        self.assertEqual(url_column_space, '/column_space/list/')

    def test_column_space_detail_url(self):
        column_space_id = uuid4()
        url_column_space_detail = reverse('inventory:column_space_detail', kwargs={'pk': column_space_id})
        self.assertEqual(url_column_space_detail, f'/column_space/detail/{column_space_id}/')
    
    def test_column_space_update_url(self):
        column_space_id = uuid4()
        url_column_space_update = reverse('inventory:column_space_update', kwargs={'pk': column_space_id})
        self.assertEqual(url_column_space_update, f'/column_space/update/{column_space_id}/')

    def test_column_space_delete_url(self):
        column_space_id = uuid4()
        url_column_space_update = reverse('inventory:column_space_delete', kwargs={'pk': column_space_id})
        self.assertEqual(url_column_space_update, f'/column_space/delete/{column_space_id}/')


class ProductInventoryUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.product_inventory = self.factory.create_product_inventory()

    def test_product_inventory_create_url(self):
        url_product_inventory = reverse('inventory:product_inventory_create')
        self.assertEqual(url_product_inventory, '/product_inventory/create/')

    def test_product_inventory_list_url(self):
        url_product_inventory = reverse('inventory:product_inventory_list')
        self.assertEqual(url_product_inventory, '/product_inventory/list/')

    def test_product_inventory_detail_url(self):
        product_inventory_id = uuid4()
        url_product_inventory_detail = reverse('inventory:product_inventory_detail', kwargs={'pk': product_inventory_id})
        self.assertEqual(url_product_inventory_detail, f'/product_inventory/detail/{product_inventory_id}/')
    
    def test_product_inventory_update_url(self):
        product_inventory_id = uuid4()
        url_product_inventory_update = reverse('inventory:product_inventory_update', kwargs={'pk': product_inventory_id})
        self.assertEqual(url_product_inventory_update, f'/product_inventory/update/{product_inventory_id}/')

    def test_product_inventory_delete_url(self):
        product_inventory_id = uuid4()
        url_product_inventory_update = reverse('inventory:product_inventory_delete', kwargs={'pk': product_inventory_id})
        self.assertEqual(url_product_inventory_update, f'/product_inventory/delete/{product_inventory_id}/')


class inventoryViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.product = self.factory.create_product()

    def test_product_view_return_status_code_200(self):
        url = reverse('inventory:product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:product_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_return_status_code_200(self):
        product_id = Product.objects.first().id
        url_product_detail = reverse('inventory:product_detail', kwargs={'pk': product_id})
        response = self.client.get(url_product_detail)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_render_correct_template(self):
        product_id = Product.objects.first().id
        url = reverse('inventory:product_detail', kwargs={'pk': product_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_detail.html')

    def test_product_view_create_render_correct_template(self):
        url = reverse('inventory:product_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_form.html')

    def test_product_view_update_render_correct_template(self):
        product= Product.objects.all().last()
        url = reverse('inventory:product_update', kwargs={'pk': product.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_form.html')

    def test_product_detail_return_404(self):
        product_id = uuid4()
        url_product_detail = reverse('inventory:product_detail', kwargs={'pk': product_id})
        response = self.client.get(url_product_detail)
        self.assertEqual(response.status_code, 404)


class CategorytUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.category = self.factory.create_category()

    def test_category_create_url(self):
        url_category = reverse('inventory:category_create')
        self.assertEqual(url_category, '/category/create/')

    def test_category_list_url(self):
        url_category = reverse('inventory:category_list')
        self.assertEqual(url_category, '/category/list/')

    def test_category_detail_url(self):
        category_id = uuid4()
        url_category_detail = reverse('inventory:category_detail', kwargs={'pk': category_id})
        self.assertEqual(url_category_detail, f'/category/detail/{category_id}/')
    
    def test_category_update_url(self):
        category_id = uuid4()
        url_category_update = reverse('inventory:category_update', kwargs={'pk': category_id})
        self.assertEqual(url_category_update, f'/category/update/{category_id}/')

    def test_category_delete_url(self):
        category_id = uuid4()
        url_category_update = reverse('inventory:category_delete', kwargs={'pk': category_id})
        self.assertEqual(url_category_update, f'/category/delete/{category_id}/')


class CategoryViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.category = self.factory.create_category()

    def test_category_view_return_status_code_200(self):
        url = reverse('inventory:category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:category_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_return_status_code_200(self):
        category_id = Category.objects.first().id
        url_category_detail = reverse('inventory:category_detail', kwargs={'pk': category_id})
        response = self.client.get(url_category_detail)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_render_correct_template(self):
        category_id = Category.objects.first().id
        url = reverse('inventory:category_detail', kwargs={'pk': category_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category/category_detail.html')

    def test_category_view_create_render_correct_template(self):
        url = reverse('inventory:category_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category/category_form.html')

    def test_category_view_update_render_correct_template(self):
        category= Category.objects.all().last()
        url = reverse('inventory:category_update', kwargs={'pk': category.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category/category_form.html')

    def test_category_detail_return_404(self):
        category_id = uuid4()
        url_category_detail = reverse('inventory:category_detail', kwargs={'pk': category_id})
        response = self.client.get(url_category_detail)
        self.assertEqual(response.status_code, 404)

class MeasureTypetUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.measure_type = self.factory.create_measure_type()

    def test_measure_type_create_url(self):
        url_measure_type = reverse('inventory:measure_type_create')
        self.assertEqual(url_measure_type, '/measure_type/create/')

    def test_measure_type_list_url(self):
        url_measure_type = reverse('inventory:measure_type_list')
        self.assertEqual(url_measure_type, '/measure_type/list/')

    def test_measure_type_detail_url(self):
        measure_type_id = uuid4()
        url_measure_type_detail = reverse('inventory:measure_type_detail', kwargs={'pk': measure_type_id})
        self.assertEqual(url_measure_type_detail, f'/measure_type/detail/{measure_type_id}/')

    def test_measure_type_update_url(self):
        measure_type_id = uuid4()
        url_measure_type_update = reverse('inventory:measure_type_update', kwargs={'pk': measure_type_id})
        self.assertEqual(url_measure_type_update, f'/measure_type/update/{measure_type_id}/')

    def test_measure_type_delete_url(self):
        measure_type_id = uuid4()
        url_measure_type_update = reverse('inventory:measure_type_delete', kwargs={'pk': measure_type_id})
        self.assertEqual(url_measure_type_update, f'/measure_type/delete/{measure_type_id}/')


class MeasureTypeViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.measure_type = self.factory.create_measure_type()

    def test_measure_type_view_return_status_code_200(self):
        url = reverse('inventory:measure_type_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_measure_type_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:measure_type_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_measure_type_detail_view_return_status_code_200(self):
        measure_type_id = MeasureType.objects.first().id
        url_measure_type_detail = reverse('inventory:measure_type_detail', kwargs={'pk': measure_type_id})
        response = self.client.get(url_measure_type_detail)
        self.assertEqual(response.status_code, 200)

    def test_measure_type_detail_view_render_correct_template(self):
        measure_type_id = MeasureType.objects.first().id
        url = reverse('inventory:measure_type_detail', kwargs={'pk': measure_type_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'measure_type/measure_type_detail.html')

    def test_measure_type_view_create_render_correct_template(self):
        url = reverse('inventory:measure_type_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'measure_type/measure_type_form.html')

    def test_measure_type_view_update_render_correct_template(self):
        measure_type= MeasureType.objects.all().last()
        url = reverse('inventory:measure_type_update', kwargs={'pk': measure_type.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'measure_type/measure_type_form.html')

    def test_measure_type_detail_return_404(self):
        measure_type_id = uuid4()
        url_measure_type_detail = reverse('inventory:measure_type_detail', kwargs={'pk': measure_type_id})
        response = self.client.get(url_measure_type_detail)
        self.assertEqual(response.status_code, 404)


class InventoryViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.inventory = self.factory.create_inventory()

    def test_inventory_view_return_status_code_200(self):
        url = reverse('inventory:inventory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_inventory_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:inventory_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_view_return_status_code_200(self):
        inventory_id = Inventory.objects.first().id
        url_inventory_detail = reverse('inventory:inventory_detail', kwargs={'pk': inventory_id})
        response = self.client.get(url_inventory_detail)
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_view_render_correct_template(self):
        inventory_id = Inventory.objects.first().id
        url = reverse('inventory:inventory_detail', kwargs={'pk': inventory_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'inventory/inventory_detail.html')

    def test_inventory_view_create_render_correct_template(self):
        url = reverse('inventory:inventory_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'inventory/inventory_form.html')

    def test_inventory_view_update_render_correct_template(self):
        inventory= Inventory.objects.all().last()
        url = reverse('inventory:inventory_update', kwargs={'pk': inventory.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'inventory/inventory_form.html')

    def test_inventory_detail_return_404(self):
        inventory_id = uuid4()
        url_inventory_detail = reverse('inventory:inventory_detail', kwargs={'pk': inventory_id})
        response = self.client.get(url_inventory_detail)
        self.assertEqual(response.status_code, 404)


class StreetViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.street = self.factory.create_street()

    def test_street_view_return_status_code_200(self):
        url = reverse('inventory:street_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_street_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:street_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_street_detail_view_return_status_code_200(self):
        street_id = Street.objects.first().id
        url_street_detail = reverse('inventory:street_detail', kwargs={'pk': street_id})
        response = self.client.get(url_street_detail)
        self.assertEqual(response.status_code, 200)

    def test_street_detail_view_render_correct_template(self):
        street_id = Street.objects.first().id
        url = reverse('inventory:street_detail', kwargs={'pk': street_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'street/street_detail.html')

    def test_street_view_create_render_correct_template(self):
        url = reverse('inventory:street_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'street/street_form.html')

    def test_street_view_update_render_correct_template(self):
        street= Street.objects.all().last()
        url = reverse('inventory:street_update', kwargs={'pk': street.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'street/street_form.html')

    def test_street_detail_return_404(self):
        street_id = uuid4()
        url_street_detail = reverse('inventory:street_detail', kwargs={'pk': street_id})
        response = self.client.get(url_street_detail)
        self.assertEqual(response.status_code, 404)


class ShelfViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.shelf = self.factory.create_shelf()

    def test_shelf_view_return_status_code_200(self):
        url = reverse('inventory:shelf_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_shelf_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:shelf_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_shelf_detail_view_return_status_code_200(self):
        shelf_id = Shelf.objects.first().id
        url_shelf_detail = reverse('inventory:shelf_detail', kwargs={'pk': shelf_id})
        response = self.client.get(url_shelf_detail)
        self.assertEqual(response.status_code, 200)

    def test_shelf_detail_view_render_correct_template(self):
        shelf_id = Shelf.objects.first().id
        url = reverse('inventory:shelf_detail', kwargs={'pk': shelf_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shelf/shelf_detail.html')

    def test_shelf_view_create_render_correct_template(self):
        url = reverse('inventory:shelf_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shelf/shelf_form.html')

    def test_shelf_view_update_render_correct_template(self):
        shelf= Shelf.objects.all().last()
        url = reverse('inventory:shelf_update', kwargs={'pk': shelf.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'shelf/shelf_form.html')

    def test_shelf_detail_return_404(self):
        shelf_id = uuid4()
        url_shelf_detail = reverse('inventory:shelf_detail', kwargs={'pk': shelf_id})
        response = self.client.get(url_shelf_detail)
        self.assertEqual(response.status_code, 404)


class LineSpaceViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.line_space = self.factory.create_line_space()

    def test_line_space_view_return_status_code_200(self):
        url = reverse('inventory:line_space_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_line_space_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:line_space_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_line_space_detail_view_return_status_code_200(self):
        line_space_id = LineSpace.objects.first().id
        url_line_space_detail = reverse('inventory:line_space_detail', kwargs={'pk': line_space_id})
        response = self.client.get(url_line_space_detail)
        self.assertEqual(response.status_code, 200)

    def test_line_space_detail_view_render_correct_template(self):
        line_space_id = LineSpace.objects.first().id
        url = reverse('inventory:line_space_detail', kwargs={'pk': line_space_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'line_space/line_space_detail.html')

    def test_line_space_view_create_render_correct_template(self):
        url = reverse('inventory:line_space_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'line_space/line_space_form.html')

    def test_line_space_view_update_render_correct_template(self):
        line_space= LineSpace.objects.all().last()
        url = reverse('inventory:line_space_update', kwargs={'pk': line_space.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'line_space/line_space_form.html')

    def test_line_space_detail_return_404(self):
        line_space_id = uuid4()
        url_line_space_detail = reverse('inventory:line_space_detail', kwargs={'pk': line_space_id})
        response = self.client.get(url_line_space_detail)
        self.assertEqual(response.status_code, 404)


class ColumnSpaceViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.column_space = self.factory.create_column_space()

    def test_column_space_view_return_status_code_200(self):
        url = reverse('inventory:column_space_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_column_space_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:column_space_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_column_space_detail_view_return_status_code_200(self):
        column_space_id = ColumnSpace.objects.first().id
        url_column_space_detail = reverse('inventory:column_space_detail', kwargs={'pk': column_space_id})
        response = self.client.get(url_column_space_detail)
        self.assertEqual(response.status_code, 200)

    def test_column_space_detail_view_render_correct_template(self):
        column_space_id = ColumnSpace.objects.first().id
        url = reverse('inventory:column_space_detail', kwargs={'pk': column_space_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'column_space/column_space_detail.html')

    def test_column_space_view_create_render_correct_template(self):
        url = reverse('inventory:column_space_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'column_space/column_space_form.html')

    def test_column_space_view_update_render_correct_template(self):
        column_space= ColumnSpace.objects.all().last()
        url = reverse('inventory:column_space_update', kwargs={'pk': column_space.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'column_space/column_space_form.html')

    def test_column_space_detail_return_404(self):
        column_space_id = uuid4()
        url_column_space_detail = reverse('inventory:column_space_detail', kwargs={'pk': column_space_id})
        response = self.client.get(url_column_space_detail)
        self.assertEqual(response.status_code, 404)


class ProductInventoryViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.product_inventory = self.factory.create_product_inventory()

    def test_product_inventory_view_return_status_code_200(self):
        url = reverse('inventory:product_inventory_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_inventory_view_create_method_post_return_status_code_200(self):
        url = reverse('inventory:product_inventory_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_product_inventory_detail_view_return_status_code_200(self):
        product_inventory_id = ProductInventory.objects.first().id
        url_product_inventory_detail = reverse('inventory:product_inventory_detail', kwargs={'pk': product_inventory_id})
        response = self.client.get(url_product_inventory_detail)
        self.assertEqual(response.status_code, 200)

    def test_product_inventory_detail_view_render_correct_template(self):
        product_inventory_id = ProductInventory.objects.first().id
        url = reverse('inventory:product_inventory_detail', kwargs={'pk': product_inventory_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product_inventory/product_inventory_detail.html')

    def test_product_inventory_view_create_render_correct_template(self):
        url = reverse('inventory:product_inventory_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product_inventory/product_inventory_form.html')

    def test_product_inventory_view_update_render_correct_template(self):
        product_inventory= ProductInventory.objects.all().last()
        url = reverse('inventory:product_inventory_update', kwargs={'pk': product_inventory.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product_inventory/product_inventory_form.html')

    def test_product_inventory_detail_return_404(self):
        product_inventory_id = uuid4()
        url_product_inventory_detail = reverse('inventory:product_inventory_detail', kwargs={'pk': product_inventory_id})
        response = self.client.get(url_product_inventory_detail)
        self.assertEqual(response.status_code, 404)