from rest_framework import serializers
from web_app.models import Category, Product, Manufacturer


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductsByManufacturerSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id']


class ProductsByCategorySerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ['id']
