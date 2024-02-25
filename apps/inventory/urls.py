from django.urls import path
from apps.inventory.views.product import product 
from apps.inventory.views.category import category 
from apps.inventory.views.measure_type import measure_type 
from apps.inventory.views.inventory import inventory 
from apps.inventory.views.street import street 
from apps.inventory.views.line_space import line_space 
from apps.inventory.views.column_space import column_space 
from apps.inventory.views.shelf import shelf 
from apps.inventory.views.product_inventory import product_inventory 

app_name = 'inventory'

urlpatterns = [
    path('product/list/', product.ProductListView.as_view(), name='product_list'),
    path('product/create/', product.ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<uuid:pk>/', product.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<uuid:pk>/', product.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<uuid:pk>/', product.ProductDeleteView.as_view(), name='product_delete'),

    path('category/list/', category.CategoryListView.as_view(), name='category_list'),
    path('category/create/', category.CategoryCreateView.as_view(), name='category_create'),
    path('category/detail/<uuid:pk>/', category.CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<uuid:pk>/', category.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<uuid:pk>/', category.CategoryDeleteView.as_view(), name='category_delete'),

    path('measure_type/list/', measure_type.MeasureTypeListView.as_view(), name='measure_type_list'),
    path('measure_type/create/', measure_type.MeasureTypeCreateView.as_view(), name='measure_type_create'),
    path('measure_type/detail/<uuid:pk>/', measure_type.MeasureTypeDetailView.as_view(), name='measure_type_detail'),
    path('measure_type/update/<uuid:pk>/', measure_type.MeasureTypeUpdateView.as_view(), name='measure_type_update'),
    path('measure_type/delete/<uuid:pk>/', measure_type.MeasureTypeDeleteView.as_view(), name='measure_type_delete'),

    path('inventory/list/', inventory.InventoryListView.as_view(), name='inventory_list'),
    path('inventory/create/', inventory.InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/detail/<uuid:pk>/', inventory.InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/update/<uuid:pk>/', inventory.InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory/delete/<uuid:pk>/', inventory.InventoryDeleteView.as_view(), name='inventory_delete'),

    path('street/list/', street.StreetListView.as_view(), name='street_list'),
    path('street/create/', street.StreetCreateView.as_view(), name='street_create'),
    path('street/detail/<uuid:pk>/', street.StreetDetailView.as_view(), name='street_detail'),
    path('street/update/<uuid:pk>/', street.StreetUpdateView.as_view(), name='street_update'),
    path('street/delete/<uuid:pk>/', street.StreetDeleteView.as_view(), name='street_delete'),

    path('shelf/list/', shelf.ShelfListView.as_view(), name='shelf_list'),
    path('shelf/create/', shelf.ShelfCreateView.as_view(), name='shelf_create'),
    path('shelf/detail/<uuid:pk>/', shelf.ShelfDetailView.as_view(), name='shelf_detail'),
    path('shelf/update/<uuid:pk>/', shelf.ShelfUpdateView.as_view(), name='shelf_update'),
    path('shelf/delete/<uuid:pk>/', shelf.ShelfDeleteView.as_view(), name='shelf_delete'),

    path('line_space/list/', line_space.LineSpaceListView.as_view(), name='line_space_list'),
    path('line_space/create/', line_space.LineSpaceCreateView.as_view(), name='line_space_create'),
    path('line_space/detail/<uuid:pk>/', line_space.LineSpaceDetailView.as_view(), name='line_space_detail'),
    path('line_space/update/<uuid:pk>/', line_space.LineSpaceUpdateView.as_view(), name='line_space_update'),
    path('line_space/delete/<uuid:pk>/', line_space.LineSpaceDeleteView.as_view(), name='line_space_delete'),

    path('column_space/list/', column_space.ColumnSpaceListView.as_view(), name='column_space_list'),
    path('column_space/create/', column_space.ColumnSpaceCreateView.as_view(), name='column_space_create'),
    path('column_space/detail/<uuid:pk>/', column_space.ColumnSpaceDetailView.as_view(), name='column_space_detail'),
    path('column_space/update/<uuid:pk>/', column_space.ColumnSpaceUpdateView.as_view(), name='column_space_update'),
    path('column_space/delete/<uuid:pk>/', column_space.ColumnSpaceDeleteView.as_view(), name='column_space_delete'),

    path('product_inventory/list/', product_inventory.ProductInventoryListView.as_view(), name='product_inventory_list'),
    path('product_inventory/create/', product_inventory.ProductInventoryCreateView.as_view(), name='product_inventory_create'),
    path('product_inventory/detail/<uuid:pk>/', product_inventory.ProductInventoryDetailView.as_view(), name='product_inventory_detail'),
    path('product_inventory/update/<uuid:pk>/', product_inventory.ProductInventoryUpdateView.as_view(), name='product_inventory_update'),
    path('product_inventory/delete/<uuid:pk>/', product_inventory.ProductInventoryDeleteView.as_view(), name='product_inventory_delete'),

]