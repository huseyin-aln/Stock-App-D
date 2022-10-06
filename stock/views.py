from django.shortcuts import render
from .serializers import BrandSerializer, CategorySerializer, FirmSerializer, ProductSerializer, TransactionSerializer
from rest_framework import viewsets
from .models import Category, Brand, Product, Firm, Transaction
from .permissions import IsStafforReadOnly


#   GET, POST, PUT, PATCH, DELETE
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsStafforReadOnly,)


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer