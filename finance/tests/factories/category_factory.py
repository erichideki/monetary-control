import factory
from finance.models import Category
from .user_factory import UserFactory

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    user = factory.SubFactory(UserFactory)
    name = factory.Faker("word")
    type = "EXPENSE" 