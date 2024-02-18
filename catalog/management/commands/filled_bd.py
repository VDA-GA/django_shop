from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read(model):
        with open('data.json', 'r', encoding='utf-8') as file:
            list_data = json.load(file)
            return [i for i in list_data if i['model'] == model]

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        product_for_create = []
        category_for_create = []
        category_list = Command.json_read('catalog.category')
        product_list = [i['fields'] for i in Command.json_read('catalog.product')]

        for category in category_list:
            category_for_create.append(Category(pk=category['pk'], **category['fields']))

        Category.objects.bulk_create(category_for_create)

        for product in product_list:
            product_for_create.append(
                Product(title=product['title'], description=product['description'], picture=product['picture'],
                        category=Category.objects.get(pk=product['category']), price=product['price'],
                        created_at=product['created_at'], updated_at=product['updated_at']))

        Product.objects.bulk_create(product_for_create)
