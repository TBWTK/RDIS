from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Storage, InventoryType, StorageLocation


def main_view(request):
    stuff = Storage.objects.filter(inventory__type__user=request.user.id, inventory__is_active=True)
    return render(request, 'table.html', {'stuff': stuff})


def update_view(request, value):
    item = Storage.objects.get(id_storage=value)
    type_inventory = InventoryType.objects.filter(user=request.user.id)
    locations = StorageLocation.objects.all()
    return render(request, 'update.html', {'item': item,  'type_inventory': type_inventory, 'locations': locations})


def search_view(request):
    pass


def add_view(request):
    pass


def my_view(request, pk):
    storage = Storage.objects.get(pk=pk)
    return render(request, 'my_template.html', {'object': storage})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('warehouse:main')
        else:
            messages.error(request, "Данные не верны, пожалуйста повторите вход")
            return redirect('warehouse:login')
    else:
        return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Вы вышли из системы, чтобы воспользоваться сайтом войдите снова")
    return redirect('warehouse:login')
