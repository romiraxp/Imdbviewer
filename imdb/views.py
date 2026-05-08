import csv
from django.shortcuts import render, redirect
from .models import Imdb
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from .forms import UploadCSVForm
from django.contrib import messages


# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import UploadFileForm

# def upload_file(request):
#     if request.method == "POST":
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES["file"])
#             return HttpResponseRedirect("/success/url/")
#     else:
#         form = UploadFileForm()
#     return render(request, "upload.html", {"form": form})

def upload_csv(request):

    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Это не CSV-файл')
                return redirect('imdb:upload_csv')
            # COPY users FROM csv_file WITH(FORMAT CSV, HEADER true, DELIMITER ',', ENCODING 'UTF8', NULL 'NA');
            # Декодируем файл и читаем его с помощью csv.reader
            # handle_uploaded_file(csv_file)

            file_data = csv_file.read().decode('utf-8').splitlines()
            # file_data = csv_file.read(chunksize=chunksize)
            # for chunk in csv_file.chunks():
            #     print(chunk)
            objs = []
            csv_data = csv.DictReader(file_data)
            cnt=0
            # for row_item in csv_data:
            #     cnt += 1
            # print(cnt)
            chunksize = 10000

            # print("--1",len(objs))
            for row in csv_data:
                if len(objs) <= chunksize:
                    objs.append(Imdb(
                        product_id=row['product_id'],
                        code=row['code'],
                        description=row['description'],
                        category=row['category'],
                        brand=row['brand'],
                        manufacturer=row['manufacturer'],
                        status=row['status']
                    ))
                else:
                    objs.append(Imdb(
                        product_id=row['product_id'],
                        code=row['code'],
                        description=row['description'],
                        category=row['category'],
                        brand=row['brand'],
                        manufacturer=row['manufacturer'],
                        status=row['status']
                    ))
                    Imdb.objects.bulk_create(objs)
                    objs = []
            Imdb.objects.bulk_create(objs)
            messages.success(request, 'CSV файл загружен и обработан.')
            return redirect('imdb:upload_csv')
    else:
        form = UploadCSVForm()
    return render(request, 'imdb/upload_csv.html', {'form': form})

# def handle_uploaded_file(f):
#     with open("some/file/name.txt", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def delete_confirm(request):
    return render(request, 'imdb/imdb_confirm_delete.html')
def delete_all(request):
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

@login_required
def index(request):
    imdb_list = Imdb.objects.all().order_by('description')
    cat_list = Imdb.objects.values('category').order_by('category').distinct()
    brand_list = Imdb.objects.values('brand').order_by('brand').distinct()
    mnf_list = Imdb.objects.values('manufacturer').order_by('manufacturer').distinct()
    imdb_records_cnt = Imdb.objects.all().count()
    public_date = Imdb.objects.values('pub_date').distinct()
    if public_date:
        context = {
            'imdb_records_cnt':imdb_records_cnt,
            'title':"Товаров в базе",
            'public_date':public_date[0]['pub_date'].date(),
        }
    else:
        context = {
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

        if not product_search and not barcode_search and not descr_search and not ctgr_search and not brnd_search and not mnf_search and not sts_search:
            imdb_list_filtered = Imdb.objects.filter(status__contains=0)
            context.update(
                {
                    'message': 'Пожалуйста, выберите критерии поиска',
                })
        else:
            imdb_list_filtered = Imdb.objects.filter(product_id__contains=product_search,
                                                     code__contains=barcode_search,
                                                     description__icontains=descr_search,
                                                     category__icontains=ctgr_search,
                                                     brand__icontains=brnd_search,
                                                     manufacturer__icontains=mnf_search,
                                                     status__contains=sts_search)[:10000]

        imdb_records_cnt = imdb_list_filtered.count()
        context.update(
                {
                    'imdb_list_filtered': imdb_list_filtered,
                    'imdb_records_cnt':imdb_records_cnt,
                }),
    return render(request, 'imdb/index.html', context)
