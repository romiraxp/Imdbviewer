import csv
from django.shortcuts import render, redirect
from .models import Imdb
from django.contrib import messages
# from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm
# , RegisterForm)
# from rest_framework import generics
# from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView


from .forms import UploadCSVForm
from django.contrib import messages

def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Это не CSV-файл')
                return redirect('imdb:upload_csv')

            # Декодируем файл и читаем его с помощью csv.reader
            file_data = csv_file.read().decode('utf-8').splitlines()
            # reader = csv.reader(file_data)

            # Предполагаем, что в CSV есть заголовки, соответствующие полям модели
            # header = next(reader)
            # for row in reader:
                # Здесь можно обработать строку и создать или обновить объекты модели
                # print(row)  # Пример вывода
            #     with open('imdbviewer/media/uploads/imdb_template.csv', 'r', newline='', encoding='utf-8') as file:
            objs = []
            csv_data = csv.DictReader(file_data)
            for row in csv_data:
                objs.append(Imdb(
                # item, created = Imdb.objects.update_or_create(
                    product_id=row['product_id'],
                    code=row['code'],
                    description=row['description'],
                    category=row['category'],
                    brand=row['brand'],
                    manufacturer=row['manufacturer'],
                    status=row['status']
                ))
            Imdb.objects.bulk_create(objs)
            messages.success(request, 'CSV файл загружен и обработан.')
            return redirect('imdb:upload_csv')
    else:
        form = UploadCSVForm()
    return render(request, 'imdb/upload_csv.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'registration/login.html', {'form': form})
#
# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'imdb/register.html', {'form': form})
#
# def logout_view(request):
#     logout(request)
#     return redirect('login')
#
# @login_required
# def home_view(request):
#     return render(request, 'imdb/index.html')
# def delete_records(request):
#     post = Imdb.objects.all()
#     context = {'post': post}
#
#     if request.method == 'GET':
#         return render(request, 'imdb/confirm_delete.html', context)
#     elif request.method == 'POST':
#         post.delete()
#         messages.success(request, 'The post has been deleted successfully.')
#         return redirect('home')

def delete_confirm(request):
    # imdb_delete = Imdb.objects.filter(code__icontains="888").delete()
    # imdb_delete = Imdb.objects.all().delete()
    # imdb_list = Imdb.objects.all().order_by('description')
    # cat_list = Imdb.objects.values('category').order_by('category').distinct()
    # brand_list = Imdb.objects.values('brand').order_by('brand').distinct()
    # mnf_list = Imdb.objects.values('manufacturer').order_by('manufacturer').distinct()
    # imdb_records_cnt = imdb_delete[0]
    # context = {
    #     'imdb_list':imdb_list,
    #     'cat_list':cat_list,
    #     'brand_list':brand_list,
    #     'mnf_list':mnf_list,
    #     'imdb_records_cnt':imdb_records_cnt,
    #     'title':"Товаров удалено в базе",
    # }
    return render(request, 'imdb/imdb_confirm_delete.html')
    # return redirect('home')
def delete_all(request):
    # imdb_delete = Imdb.objects.filter(code__icontains="888").delete()
    imdb_delete = Imdb.objects.all().delete()
    imdb_list = Imdb.objects.all().order_by('description')
    cat_list = Imdb.objects.values('category').order_by('category').distinct()
    brand_list = Imdb.objects.values('brand').order_by('brand').distinct()
    mnf_list = Imdb.objects.values('manufacturer').order_by('manufacturer').distinct()
    imdb_records_cnt = imdb_delete[0]
    context = {
        'imdb_list':imdb_list,
        'cat_list':cat_list,
        'brand_list':brand_list,
        'mnf_list':mnf_list,
        'imdb_records_cnt':imdb_records_cnt,
        'title':"Товаров удалено в базе",
    }
    # return render(request, 'imdb/index.html', context)
    return redirect('imdb:home')

def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="imdb_template.csv"'

    writer = csv.writer(response)
    writer.writerow(['product_id', 'code', 'description', 'category', 'brand', 'manufacturer', 'status'])

    imdb_list = Imdb.objects.all()
    for item in imdb_list:
        writer.writerow([item.product_id, item.code, item.decription, item.category, item.brand, item.manufacturer, item.status])

    return response
# def imdb_list(request):
#     with open('imdbviewer/media/uploads/imdb_template.csv', 'r', newline='', encoding='utf-8') as file:
#         csv_data = csv.DictReader(file)
#         for row in csv_data:
#             # print(row)
#             item, created = Imdb.objects.update_or_create(
#                 product_id=row['product_id'],
#                 code=row['code'],
#                 description=row['description'],
#                 category=row['category'],
#                 brand=row['brand'],
#                 manufacturer=row['manufacturer'],
#                 status=row['status']
#             )
#     return render(request, 'imdb/index.html')

    # students = []
    # with open('media/students.csv', 'r', encoding='utf-8') as file:
    #     csv_data = csv.DictReader(file)
    #     for row in csv_data:
    #         students.append(row)
    # return render(request, 'student_list.html', {'students': students})


# if not os.path.isfile(csv_file):
#     print('file not found!')
#     return

                   # class ImdbDeleteView(DeleteView):
#     model = Imdb
#
#     def delete(self, request, *args, **kwargs):
#         """
#         Call the delete() method on the fetched object and then redirect to the
#         success URL.
#         """
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         return HttpResponseRedirect(success_url)
#     # can specify success url
#     # url to redirect after successfully
#     # deleting object
#     success_url = "/"

    # template_name = "imdb/imdb_confirm_delete.html"

@login_required
def index(request):
    imdb_list = Imdb.objects.all().order_by('description')
    cat_list = Imdb.objects.values('category').order_by('category').distinct()
    brand_list = Imdb.objects.values('brand').order_by('brand').distinct()
    mnf_list = Imdb.objects.values('manufacturer').order_by('manufacturer').distinct()
    imdb_records_cnt = Imdb.objects.all().count()
    public_date = Imdb.objects.values('pub_date').distinct()
    # date_only = public_date['pub_date'].date()
    if public_date:
        context = {
            'imdb_list':imdb_list,
            'cat_list':cat_list,
            'brand_list':brand_list,
            'mnf_list':mnf_list,
            'imdb_records_cnt':imdb_records_cnt,
            'title':"Товаров в базе",
            'public_date':public_date[0]['pub_date'].date(),
        }
    else:
        context = {
            'imdb_list':imdb_list,
            'cat_list':cat_list,
            'brand_list':brand_list,
            'mnf_list':mnf_list,
            'imdb_records_cnt':imdb_records_cnt,
            'title':"Товаров в базе",
            'public_date':"0",
        }
    if request.method == "POST":
        context.update({'title': "Товаров найдено"})
        product_search = request.POST.get('product', None)
        barcode_search = request.POST.get('barcode', None)
        descr_search = request.POST.get('description', None)
        ctgr_search = request.POST.get('category', None)
        brnd_search = request.POST.get('brand', None)
        mnf_search = request.POST.get('manufacturer', None)
        sts_search = request.POST.get('status', None)
        if product_search:
            imdb_list_filtered = Imdb.objects.filter(product_id__contains=product_search)
            imdb_records_cnt = Imdb.objects.filter(product_id__contains=product_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        elif barcode_search:
            imdb_list_filtered = Imdb.objects.filter(code__contains=barcode_search)
            imdb_records_cnt = Imdb.objects.filter(code__contains=barcode_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        elif descr_search:
            imdb_list_filtered = Imdb.objects.filter(description__icontains=descr_search)
            imdb_records_cnt = Imdb.objects.filter(description__icontains=descr_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        elif ctgr_search:
            imdb_list_filtered = Imdb.objects.filter(category__icontains=ctgr_search)
            imdb_records_cnt = Imdb.objects.filter(category__icontains=ctgr_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        elif brnd_search:
            imdb_list_filtered = Imdb.objects.filter(brand__icontains=brnd_search)
            imdb_records_cnt = Imdb.objects.filter(brand__icontains=brnd_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        elif mnf_search:
            imdb_list_filtered = Imdb.objects.filter(manufacturer__icontains=mnf_search)
            imdb_records_cnt = Imdb.objects.filter(manufacturer__icontains=mnf_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        elif sts_search:
            imdb_list_filtered = Imdb.objects.filter(status__contains=sts_search)
            imdb_records_cnt = Imdb.objects.filter(status__contains=sts_search).count()
            context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
            return render(request, 'imdb/index.html', context)
        else:
            context.update(
                {
                    'message': 'Пожалуйста, выберите критерии поиска',
                    'title': "Товаров в базе",
                })
            return render(request, 'imdb/index.html', context)
    return render(request, 'imdb/index.html', context)