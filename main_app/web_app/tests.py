from django.test import TestCase, RequestFactory
from web_app.models import Category, Manufacturer, Product, ProductImage
from rest_framework import status
from web_app.views import get_all_categories, get_all_manufacturers, get_all_products, \
    get_all_products_by_category, get_all_products_by_manufacturer


class MarketTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name='Test Category', category_image='test_category_image.jpg')
        self.manufacturer = Manufacturer.objects.create(manufacturer_name='Test Manufacturer')
        self.product = Product.objects.create(
            product_name='Test Product',
            product_manufacturer=self.manufacturer,
            product_in_stock=True,
            product_description='Test description',
            product_price=10.99
        )
        self.product.categories.add(self.category)
        self.product_image = ProductImage.objects.create(product=self.product, image='test_image.jpg')
        self.factory = RequestFactory()

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_manufacturer_str(self):
        self.assertEqual(str(self.manufacturer), 'Test Manufacturer')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_image_str(self):
        self.assertEqual(str(self.product_image), 'test_image.jpg')

    def test_get_categories(self):
        categories = Category.get_categories()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0]['category_name'], 'Test Category')

    def test_get_manufacturers(self):
        manufacturers = Manufacturer.get_manufacturers()
        self.assertEqual(len(manufacturers), 1)
        self.assertEqual(manufacturers[0]['manufacturer_name'], 'Test Manufacturer')

    def test_get_products(self):
        products = Product.get_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]['product_name'], 'Test Product')

    def test_get_all_categories(self):
        request = self.factory.get('/api/categories/')
        response = get_all_categories(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_manufacturers(self):
        request = self.factory.get('/api/manufacturers/')
        response = get_all_manufacturers(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products(self):
        request = self.factory.get('/api/products/')
        response = get_all_products(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_by_category(self):
        request = self.factory.post('/api/get-all-products-by-category/', {"id": 5})
        response = get_all_products_by_category(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_products_by_manufacturer(self):
        request = self.factory.post('/api/get-all-products-by-manufacturer/', {'id': 6})
        response = get_all_products_by_manufacturer(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_missing_category_id(self):
        request = self.factory.post('/api/get-all-products-by-category/', {})
        response = get_all_products_by_category(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_manufacturer_id(self):
        request = self.factory.post('/api/get-all-products-by-manufacturer/', {})
        response = get_all_products_by_manufacturer(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_category_id(self):
        request = self.factory.post('/api/get-all-products-by-category/', {'id': 'invalid_id'})
        response = get_all_products_by_category(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_manufacturer_id(self):
        request = self.factory.post('/api/get-all-products-by-manufacturer/', {'id': 'invalid_id'})
        response = get_all_products_by_manufacturer(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
