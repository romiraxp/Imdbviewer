# обычные модули для панели администрирования
from django.contrib import admin
from .models import Imdb, ImdbImport
# обслуживание импорта
import csv
# from .forms import ImdbImportForm
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
# admin.site.register(Group)
# admin.site.register(Permission)

# @admin.register(ImdbImport)
# class ImdbImportAdmin(admin.ModelAdmin):
#     list_display = ('csv_file', 'date_added')


# @admin.register(Imdb)
class ImdbAdmin(admin.ModelAdmin):
    list_display = ("product_id", "code", "description", "category", "brand", "manufacturer", "status")

admin.site.register(Imdb,ImdbAdmin)
# даем django(urlpatterns) знать
# о существовании страницы с формой
# иначе будет ошибка
#     def get_urls(self):
#         urls = super().get_urls()
#         urls.insert(-1, path('csv-upload/', self.upload_csv))
#         return urls
#
#
# # если пользователь открыл url 'csv-upload/'
# # то он выполнит этот метод
# # который работает с формой
#     def upload_csv(self, request):
#         if request.method == 'POST':
#         # т.к. это метод POST проводим валидацию данных
#             form = ImdbImportForm(request.POST, request.FILES)
#             if form.is_valid():
#             # ...
#             # какая-то ваша реализация обработки формы
#             # ...
#                 form_object = form.save()
#             # обработка csv файла
#                 with form_object.csv_file.open('r') as csv_file:
#                     rows = csv.reader(csv_file, delimiter=',')
#                 # if next(rows) != ['name', 'author', 'publish_date']:
#                 #     # обновляем страницу пользователя
#                 #     # с информацией о какой-то ошибке
#                 #     messages.warning(request, 'Неверные заголовки у файла')
#                 #     return HttpResponseRedirect(request.path_info)
#                     for row in rows:
#                     # print(row[2])
#                     # добавляем данные в базу
#                     # Imdb.objects.update_or_create(
#                     #     name=row[0],
#                     #     author=row[1],
#                     #     publish_date=row[2]
#                     # )
#                         item, created = Imdb.objects.update_or_create(
#                             product_id=row['product_id'],
#                             code=row['code'],
#                             description=row['description'],
#                             category=row['category'],
#                             brand=row['brand'],
#                             manufacturer=row['manufacturer'],
#                             status=row['status']
#                         )
#
#             # конец обработки файлы
#             # перенаправляем пользователя на главную страницу
#             # с сообщением об успехе
#             # возвращаем пользователя на главную с сообщением об успехе
#                 url = reverse('admin:index')
#                 messages.success(request, 'Файл успешно импортирован')
#                 return HttpResponseRedirect(url)
#     # если это не метод POST, то возвращается форма с шаблоном
#             form = ImdbImportForm()
#             return render(request, 'admin/csv_import_page.html', {'form': form})
#
