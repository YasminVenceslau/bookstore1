
# product/serializers/product_serializer.py
from rest_framework import serializers
from product.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'stock']
