from django.contrib.auth.models import User
from product.factories import ProductFactory
from order.models import Order

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("pystr")

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)
    
    class Meta:
        model = Order