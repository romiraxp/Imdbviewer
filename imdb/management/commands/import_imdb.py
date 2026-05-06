# import json
import csv
import os
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from imdb.models import Imdb
import datetime


class Command(BaseCommand):
    help = 'Заполнение БД данными из Json файла'
    def add_arguments(self, parser):
        pass

    # def handle(self, *args, **options):
    #     with open('fixtures/books.json', 'r', encoding='UTF-8') as json_file:
    #         books = json.load(json_file)
    #         # print(books)
    #         #list(csv.DictReader(file, delimiter=';'))
    #     for book in books:
    #         # print(book)
    #         # TODO: Добавьте сохранение модели
    #         book_name = Book.objects.create(
    #             id = book['pk'],
    #             name = book['fields']['name'],
    #             author = book['fields']['author'],
    #             pub_date = book['fields']['pub_date'],
    #             #slug = slugify(book['fields']['name']),
    #         )
    #         book_name.save

    def handle(self, *args, **options):

        csv_file ='C:\Podkorytro01\PythonProjects\IMDBViewer\pythonProject1\imdb\imdbview\media\imdb_template.csv'

        if not os.path.isfile(csv_file):
            print('file not found!')
            return

        with open(csv_file, newline='', encoding='utf-8') as file:
            csv_data = csv.DictReader(file)
            for row in csv_data:
                print(row)
                item, created = Imdb.objects.update_or_create(
                    product_id = row['product_id'],
                    code = row['code'],
                    description = row['description'],
                    category = row['category'],
                    brand = row['brand'],
                    manufacturer = row['manufacturer'],
                    status = row['status']
                )
                # imdb_name.save
        # return render(request, 'index.html', {'imdbBase': imdbBase})
