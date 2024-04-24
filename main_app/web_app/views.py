from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from web_app.models import *
from web_app.serializers import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


@swagger_auto_schema(
    methods=['get'],
    responses={status.HTTP_200_OK: CategorySerializer},
    operation_description='Get all categories',
    operation_id='get_all_categories',
    tags=['Market'],
)
@api_view(['GET'])
def get_all_categories(request):
    if request.method == 'GET':
        all_categories = Category.get_categories()
        return Response(all_categories, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@swagger_auto_schema(
    methods=['get'],
    responses={status.HTTP_200_OK: ManufacturerSerializer},
    operation_description='Get all manufacturers',
    operation_id='get_all_manufacturers',
    tags=['Market'],
)
@api_view(['GET'])
def get_all_manufacturers(request):
    if request.method == 'GET':
        all_manufacturers = Manufacturer.get_manufacturers()
        return Response(all_manufacturers, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@swagger_auto_schema(
    methods=['get'],
    responses={status.HTTP_200_OK: ProductSerializer},
    operation_description='Get all products',
    operation_id='get_all_products',
    tags=['Market'],
)
@api_view(['GET'])
def get_all_products(request):
    if request.method == 'GET':
        all_products = Product.get_products()
        return Response(all_products, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@swagger_auto_schema(
    methods=['post'],
    responses={status.HTTP_200_OK: ProductSerializer(many=True)},
    operation_description='Get all products by manufacturer',
    operation_id='get_all_products_by_manufacturer',
    request_body=ProductsByManufacturerSerializer,
    tags=['Market'],
)
@api_view(['POST'])
def get_all_products_by_manufacturer(request):

    serializer = ProductsByManufacturerSerializer(data=request.data)

    if request.method == 'POST':
        if serializer.is_valid():
            manufacturer_id = request.data['id']
            try:
                products = Product.objects.filter(product_manufacturer_id=manufacturer_id)
                
                if not products:
                    raise ObjectDoesNotExist
                
                serialized_products = [product.serialize() for product in products]
                return Response(serialized_products, status=status.HTTP_200_OK)
            except Exception:
                return Response({'error': 'Manufacturer not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['post'],
    responses={status.HTTP_200_OK: ProductSerializer(many=True)},
    operation_description='Get all products by category',
    operation_id='get_all_products_by_category',
    request_body=ProductsByCategorySerializer,
    tags=['Market'],
)
@api_view(['POST'])
def get_all_products_by_category(request):

    serializer = ProductsByCategorySerializer(data=request.data)

    if request.method == 'POST':
        if serializer.is_valid():
            category_id = request.data['id']
            try:
                category = Category.objects.get(pk=category_id)
                products = Product.objects.filter(categories=category)
                
                if not products:
                    raise ObjectDoesNotExist
                
                serialized_products = [product.serialize() for product in products]
                return Response(serialized_products, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_404_NOT_FOUND)
