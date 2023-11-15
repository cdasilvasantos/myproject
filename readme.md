# Tutorial: Getting Started with Django
### Introduction
Welcome to our tutorial on building a Django backend with a database. In this tutorial, we'll cover the basics of Django, migrations, models, factories, seeding the database with fake data, and testing the database. This step-by-step guide will help other users in developing a solid foundation using Django. 

### Authors
- Chiara daSilva Santos
- Christian Wantong
- Michael Daniels

### Prerequisites
Ensure that you have the following installed on your system
- Python
- Pip (Python Package Installer)
- Django

To install Django, run the following command on terminal:
```
pip install django
```


#### Step 1: Setting up the Project
1. Create a Django Project:
```
django-admin startproject myproject
```

2. Navigate to Your Project:
```
cd my project
```

#### Step 2: Creating Migrations and Models
1. Create a Django App:
```
python manage.py startapp myapp
```
(you may need to change python to python3 depending on the version you are using)

3. Define a Model: Edit 'myapp/models.py' and run the following command:

```
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
```
3. Make Migrations:
```
python3 manage.py makemigrations
```

5. Apply Migrations:
```
python3 manage.py migrate
```

#### Step 3: Creating Factories and Seeding with Fake Data
1. Install Factory Boy:
```
pip3 install factory-boy
```

2. Define a Factory:
Create 'myapp/factories.py' and run the following command:

```
import factory
from .models import MyModel

class MyModelFactory(factory.Factory):
    class Meta:
        model = MyModel

    name = factory.Faker('word')
    description = factory.Faker('text')
```

3. Create seed.py in myapp and add the following:
```
from django.core.management.base import BaseCommand
from myapp.factories import MyModelFactory

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Seed 10 records
            MyModelFactory()
```

4. Run:
```
mkdir myapp/management
```

5. Run:
```
mkdir myapp/management/commands
```

6. Run:
```
touch myapp/management/commands/seed.py
```

7. Run:
```
python3 manage.py seed
```

#### Step 4: Testing the Database
1. Create 'myapp/tests.py' and add the following:
```
from django.test import TestCase
from .models import MyModel

class MyModelTests(TestCase):
    def test_database(self):
        count_before = MyModel.objects.count()

        # Create a new record
        MyModel.objects.create(name='Test Name', description='Test Description')

        count_after = MyModel.objects.count()
        self.assertEqual(count_after, count_before + 1)
```
2. Run:
```
python3 manage.py test
```


### Conclusion
You have completed the tutorial on building a Django backend with a database. You have learned how to create migrations, define modeles, use factories for fake data, seed the database, and write tests!
