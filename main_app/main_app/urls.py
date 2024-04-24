from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from main_app.settings import os
from django.urls import path, re_path
from web_app import views


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="API for \"any market\"",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   url=os.getenv("BACKEND_ADDR"),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/get-all-categories', views.get_all_categories, name='get-all-categories'),
    path('api/get-all-manufacturers', views.get_all_manufacturers, name='get-all-manufacturers'),
    path('api/get-all-products', views.get_all_products, name='get-all-products'),
    path('api/get-all-products-by-manufacturer', views.get_all_products_by_manufacturer, name='get-all-products-by-manufacturer'),
    path('api/get-all-products-by-category', views.get_all_products_by_category, name='get-all-products-by-category'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
