from rest_framework import serializers
from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    # Somente leitura → retorna os dados completos da categoria
    category = CategorySerializer(read_only=True, many=True)

    # Escrita → permite IDs de categoria, mas agora é opcional
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        many=True,
        required=False,   # não é obrigatório
        allow_empty=True  # pode ser lista vazia []
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]

    def create(self, validated_data):
        # Se não vier nada, usa lista vazia
        category_data = validated_data.pop("categories_id", [])
        product = Product.objects.create(**validated_data)

        # Só adiciona categorias se realmente tiver
        if category_data:
            for category in category_data:
                product.category.add(category)

        return product
