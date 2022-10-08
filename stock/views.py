from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import DjangoModelPermissions
from .permissions import CustomModelPermission
from .serializers import (
    BrandProductsSerializer,
    BrandSerializer,
    CategoryProductsSerializer, 
    CategorySerializer, 
    FirmSerializer, 
    ProductSerializer, 
    TransactionSerializer
)
from .models import (
    Category, 
    Brand, 
    Product, 
    Firm, 
    Transaction
)


#   GET, POST, PUT, PATCH, DELETE
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductsSerializer
        else:
            return super().get_serializer_class()


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return BrandProductsSerializer
        else:
            return super().get_serializer_class()


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name']


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['firm', 'transaction_type', 'product']
    search_fields = ['firm']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

