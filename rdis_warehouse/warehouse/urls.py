from django.urls import path
from .views import logout_view, login_view, main_view, update_view
from django.contrib import admin


app_name = 'school'

urlpatterns = [
    path('', main_view, name='main'),
    path('/admin/storage/<int:pk>/change/', admin.site.urls, name='update'),
    path('/<int:value>/$', update_view, name='update'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
