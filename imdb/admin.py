# обычные модули для панели администрирования
from django.contrib import admin
from .models import Imdb, ImdbImport
# обслуживание импорта
import csv
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

class ImdbAdmin(admin.ModelAdmin):
    list_display = ("product_id", "code", "description", "category", "brand", "manufacturer", "status")

admin.site.register(Imdb,ImdbAdmin)
