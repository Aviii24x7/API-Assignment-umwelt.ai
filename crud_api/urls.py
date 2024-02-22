from django.urls import path
from .views import *


# for drf_yasg // from documentation
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Umwelt Assignment API",
      default_version='v1',
      description="Inventory management!!",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Our URLS
urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<id>', CategoryPKView.as_view(), name='category-retrieve-update-destroy'),
    
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<id>', ProductPKView.as_view(), name='product-retrieve-update-destroy'),

    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<id>', OrderPKView.as_view(), name='order-retrieve-update-destroy'),
    
    # drf_yasg
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
