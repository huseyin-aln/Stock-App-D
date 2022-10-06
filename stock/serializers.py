from rest_framework import serializers
from .models import Category, Brand, Product, Firm, Transaction


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('name',)


# class ProductSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#     category_id = serializers.IntegerField(write_only=True)
#     brand = serializers.StringRelatedField()
#     brand_id = serializers.IntegerField(write_only=True)
#     class Meta: 
#         model = Product
#         fields = (
#             'name',
#             'category',
#             'category_id',
#             'brand',
#             'brand_id',
#             'stock'
#         )

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
   
    class Meta: 
        model = Product
        fields = "__all__"


class FirmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Firm
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"