# product/serializers.py
from rest_framework import serializers
from models.product import Product  # Importa apenas o Product
# Se precisar da Category
from .models.category import Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "price", "category"]
