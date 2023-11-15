import factory
from .models import MyModel

class MyModelFactory(factory.Factory):
    class Meta:
        model = MyModel

    name = factory.Faker('word')
    description = factory.Faker('text')
