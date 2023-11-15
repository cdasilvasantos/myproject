# myapp/management/commands/seed.py
from django.core.management.base import BaseCommand
from myapp.models import MyModel
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        for _ in range(10):  # Seed 10 records
            MyModel.objects.create(
                name=fake.word(),
                description=fake.text()
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
