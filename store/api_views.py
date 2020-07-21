from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from store.serializers import ProductSerializer
from store.models import Product

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # setting up filtering by ID
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
