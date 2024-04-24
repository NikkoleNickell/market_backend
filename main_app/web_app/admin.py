from django.contrib import admin
from web_app.models import Category, Product, Manufacturer, ProductImage
from django.utils.safestring import mark_safe


class ProductManufacturerInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('category_name', 'category_image')
    readonly_fields = ['preview']
    def preview(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.category_image.url}"/>')
    preview.allow_tags = True


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    readonly_fields = ['preview']
    def preview(self, obj):
        return mark_safe(f'<img width="200px" src="{obj.image.url}"/>')
    preview.allow_tags = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('product_name', 'product_in_stock')
    inlines = [ProductImageInline]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    
    list_display = ('manufacturer_name', )
    inlines = [ProductManufacturerInline]
