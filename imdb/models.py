from django.db import models
from django.contrib.auth.models import User
import datetime

from django.db import models
from django.utils import timezone

class Imdb(models.Model):
    product_id = models.CharField(max_length=10, verbose_name="ИД Продукта ")
    code = models.CharField(max_length=14, verbose_name="Штрих- код")
    description = models.CharField(max_length=200, verbose_name="Описание")
    category = models.CharField(max_length=50, verbose_name="Категория")
    brand = models.CharField(max_length=100, verbose_name="Бренд")
    manufacturer = models.CharField(max_length=80, verbose_name="Производитель")
    status = models.CharField(max_length=8, verbose_name="Статус")
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class ImdbImport(models.Model):
    csv_file = models.FileField(upload_to='uploads/')
    date_added = models.DateTimeField(auto_now_add=True)