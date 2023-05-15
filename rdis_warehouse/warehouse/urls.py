from django.urls import path
from .views import logout_view, login_view, main_view, export_excel
from django.contrib import admin


app_name = 'school'

urlpatterns = [
    path('', main_view, name='main'),
    path('/admin/storage/<int:pk>/change/', admin.site.urls, name='update'),
    path('export/', export_excel, name='export_excel'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
