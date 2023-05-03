from django.contrib import admin
from .models import StorageLocation, Workers, InventoryType, Inventory, Storage


@admin.register(StorageLocation)
class StorageLocationAdmin(admin.ModelAdmin):
    list_display = ['location_name']
    search_fields = ['location_name']


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['name', 'first_name', 'last_name']
    search_fields = ['name', 'first_name', 'last_name']


@admin.register(InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
    search_fields = ['type_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['type', 'inventory_name', 'inventory_number', 'specifications', 'is_active']
    search_fields = ['type', 'inventory_name', 'inventory_number', 'specifications', 'is_active']

    def get_queryset(self, request):
        qs = Inventory.objects.filter(type__user=request.user.id)
        return qs


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['location', 'inventory', 'worker', 'start_date', 'end_date', 'comment']
    search_fields = ['location', 'inventory', 'worker', 'start_date', 'end_date', 'comment']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(inventory__type__user=request.user)

