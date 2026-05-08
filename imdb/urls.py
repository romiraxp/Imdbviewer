from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'imdb'
urlpatterns = [
    path('', views.index, name='home'),
]
urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('delete/', views.delete_all, name='delete_all'),
    path('delete_conf/', views.delete_confirm, name='delete_conf'),
    path('generate-csv/', views.generate_csv, name='generate_csv'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]