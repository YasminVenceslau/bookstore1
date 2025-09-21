import pytest
from product.models.category import Category
from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    # Criar um objeto Category de teste
    category = Category.objects.create(
        title="Ficção",
        slug="ficcao",
        description="Categoria de livros de ficção",
        active=True
    )

    # Serializar o objeto
    serializer = CategorySerializer(category)
    data = serializer.data

    # Verificar se os campos estão corretos
    assert data['title'] == "Ficção"
    assert data['slug'] == "ficcao"
    assert data['description'] == "Categoria de livros de ficção"
    assert data['active'] is True
