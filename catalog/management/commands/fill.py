import os

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'name': "phone", 'about': "smartphone"},
            {'name': "beer", 'about': "irish luck"},
            {'name': "monitor", 'about': "seeeeeeeing to"},
            {'name': "mouse", 'about': "knock knock"}
        ]
        category_for_create = []
        for category in category_list:
            category_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(category_for_create)
        return os.system('python3 manage.py loaddata data.json')
