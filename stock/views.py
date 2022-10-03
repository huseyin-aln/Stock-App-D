from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework import viewsets
from .models import Category, Brand, Product, Firm, Transaction


#   GET, POST, PUT, PATCH, DELETE
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
