import pytest
from product.models import Product, Category

@pytest.mark.django_db
def test_create_product_with_category():
    # cria uma categoria
    cat = Category.objects.create(name="Ficção")
    
    # cria um produto e associa a categoria
    product = Product.objects.create(title="Livro Teste", price=50)
    product.categories.add(cat)
    product.save()

    # asserts
    assert product.title == "Livro Teste"
    assert product.id is not None
    assert cat in product.categories.all()
