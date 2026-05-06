from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
# from django.views.generic import TemplateView
# from .views import ImdbDeleteView

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
    # path('load/', views.imdb_list, name='load'),
]

# path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
# path('logout/', views.logout_view, name='logout'),
# path('delete/', views.delete_records, name='delete_all')
# path('delete/', ImdbDeleteView.as_view(), name='delete_all'),
# path('<pk>/delete/', ImdbDeleteView.as_view()),
# path('<pk>/delete/', ImdbDeleteView.as_view(template_name='imdb/imdb_confirm_delete.html'), name='delete'),
    # path('load/', views.imdb_list, name='load'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', TemplateView.as_view(template_name='registration/logged_out.html'), name='logout'),
# path('', views.home_view, name='home'),
# path('special/', views.special_page_view, name='special_page'),
