import pytest

from product.models import Product, Category


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Titulo",
        description="Descrição",
        price=999
    )

    assert product.title == "Titulo"
    assert product.description == "Descrição"
    assert product.price == 999
    assert product.id is not None