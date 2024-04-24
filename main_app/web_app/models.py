from django.db import models


class Category(models.Model):

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    category_name = models.CharField(verbose_name='Название категории', unique=True, max_length=255)
    category_image = models.ImageField(upload_to='images/', verbose_name='Картинка категории')
    
    def get_categories():
        categories = Category.objects.values().order_by('pk')
        return categories

    def __str__(self):
        return self.category_name


class Manufacturer(models.Model):
    
    class Meta:
        db_table = 'manufacturers'
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    manufacturer_name = models.CharField(verbose_name='Название производителя', max_length=255)

    def get_manufacturers():
        manufacturers = Manufacturer.objects.values().order_by('pk')
        print(manufacturers)
        return manufacturers

    def __str__(self):
        return self.manufacturer_name


class Product(models.Model):
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def serialize(self):
        return {
            'id': self.pk,
            'product_name': self.product_name,
            'product_manufacturer': self.product_manufacturer.manufacturer_name,
            'product_in_stock': self.product_in_stock,
            'product_description': self.product_description,
            'product_price': self.product_price,
            'categories': [category.category_name for category in self.categories.all()],
            'images': [image.image.url for image in self.images.all()],
        }
        
    product_name = models.CharField(verbose_name='Название товара', max_length=255)
    product_manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель товара', on_delete=models.CASCADE)
    product_in_stock = models.BooleanField(verbose_name='Товар в наличии', default=False)
    product_description = models.TextField(verbose_name='Описание товара')
    product_price = models.DecimalField(verbose_name='Цена товара', max_digits=7, decimal_places=2)
    categories = models.ManyToManyField(Category, verbose_name='Категории товара', related_name='categories')

    def get_products():
        products_list = []
        product_objects = Product.objects.prefetch_related(
            'categories', 'images').order_by('pk')

        for product_object in product_objects:
            product_dict = {
                'id': product_object.pk,
                'product_name': product_object.product_name,
                'product_manufacturer': product_object.product_manufacturer.manufacturer_name,
                'product_in_stock': product_object.product_in_stock,
                'product_description': product_object.product_description,
                'product_price': product_object.product_price,
                'categories': list(product_object.categories.values_list('category_name', flat=True)),
                'images': list(product_object.images.values_list('image', flat=True))
            }
            products_list.append(product_dict)

        return products_list

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    
    class Meta:
        db_table = 'product_images'
        verbose_name = 'Картинка товара'
        verbose_name_plural = 'Картинки товаров'
    
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка товара')

    def __str__(self):
        return self.image.url[1:] if self.image else "No image"
